# Documentation : Machine Learning

## Prétraitement

Dans l’étape de prétraitement, on supprime les caractères spéciaux, les caractères seuls, les
espaces multiples et on passe l’ensemble des textes en lettres minuscules.
On passe ensuite d’une information textuelle vers numérique avec la méthode TF-IDF

## Algorithmes

### Tests

Les algorithmes que nous avons testé sont : Random Forest, kNN, Perceptron​, Nearest Centroid et
avec pénalité L1 et L2 : SGD(​Stochastic Gradient Descent​) Classifier et SVM.

### Choix

L’algorithme choisi suite à cette phase de tests : SVM avec pénalité L2

## Résultats

### Performance

- Précision proche de 79%
- Temps d’entraînement et de classification pas trop grands
- Score F1 Macro : 0.716

### Biais de prédiction

- Disparate impact données réelles : 3.9
- DIsparate impact données prédites : 3.08

=> Aucun biais ajouté

