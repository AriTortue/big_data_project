import pandas as pd
import numpy as np

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

from sklearn import metrics
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('punkt')

# Fonction pour pré-traiter le texte avant TFIDF
def pre_processing(X):
    documents = []
    stemmer = WordNetLemmatizer()

    for sen in range(0, len(X)):
        # Suppression des caractères spéciaux
        document = re.sub(r'\W', ' ', str(X[sen]))

        # Suppression des caractères seuls
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 

        # Espaces multiples => Espace unique
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Suppression du préfixe 'b'
        document = re.sub(r'^b\s+', '', document)

        document = re.sub(r'[0-9]+', '', document)

        # Passage en minuscule
        document = document.lower()

        # Lemmatisation
        document = document.split()

        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)

        documents.append(document)
    return documents

# Chargement des données
print("Chargement des données")
df = pd.read_json("data.json")
label = pd.read_csv("label.csv")
names = pd.read_csv('categories_string.csv')['0'].to_dict()
y = np.array(label['Category'])

# Séparation en 2 parties : entrainement et test
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3, random_state=0)

print("Préparation des données d'entraînement")
X_train = pre_processing(list(X_train['description']))
vectorizer = TfidfVectorizer(sublinear_tf=True,min_df=0.001, max_df=0.5,stop_words='english')
vectorizer.fit_transform(X_train)
X_train = vectorizer.transform(X_train)

# Entrainement du modèle
print("Entraînement du modèle")
model = LinearSVC(penalty="l2", dual=False,tol=1e-3)
model.fit(X_train,y_train)

predict = X_test.copy()
X_test = pre_processing(list(X_test['description']))
X_test = vectorizer.transform(X_test)

# Utilisation du modèle sur les données tests
print("Application du modèle aux données tests")
y_pred = model.predict(X_test)

# Affichage de la performance
score = metrics.accuracy_score(y_test, y_pred)
print("- Précision :   %0.3f" % score)
print("- Score macro F1 :   %0.3f" % (f1_score(y_test, y_pred, average='macro')))

# Calcul de la disparité selon le genre
predict['job']=y_pred
predict['job'] = predict['job'].map(names)
predict.to_csv(path_or_buf="predict.csv",index=False)
print("Fichier predict.csv créé")
people = pd.concat((predict['job'], predict['gender']), axis='columns')
counts = people.groupby(['job', 'gender']).size().unstack('gender')
counts['disparate_impact'] = counts[['M', 'F']].max(axis='columns') / counts[['M', 'F']].min(axis='columns')
counts.sort_values('disparate_impact', ascending=False)
counts['disparate_impact'].mean()
