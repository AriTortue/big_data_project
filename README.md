# big_data_project
Big Data Project / FISE 3 OPT INFO2

## **Objectifs**
Le but de ce projet est de prédire le métier recherché à partir d’un extrait de CV d’une personne. 
Il y a 28 catégories de postes.

D’abord, nous devons utiliser dans nos modèles la moyenne arithmétique des scores F1 de chaque classe. 

De plus, il nous faut prendre en compte le genre des personnes et limiter le biais de prédiction lié au genre.

## **Premier niveau d’analyse des données**
Nous avons accès à des données aux formats JSon et CSV.
Nous avons des informations sur le genre de chaque individu.

* *data.json:*
Association des descriptions des postes (chaîne de caractères) avec les identifiants des individus (entiers) et leur genre (chaîne de caractères).
217198 lignes, 3 colonnes.

* *label.csv:*
Association des identifiants des catégories de métiers (entiers) avec les identifiants des individus (entiers).
Couples d’entiers séparés par des virgules: int,int.
217198 lignes.

* *categories_string.csv:*
Association des labels des postes (chaînes de caractères) avec l’identifiant de la catégorie du poste qui y correspond (entier).
Couples de chaînes de caractères et entiers séparés par des virgules: string,int.
29 lignes.

## **Deuxième niveau d'analyse des données**
Mesures de fairness appliquées : 
* aux données labelisées du jeu de test 

* aux prédictions sur le jeu de test

Le but est de conclure si le modèle est plus biaisé que la réalité (écart entre les deux scores).

On compare donc la répartition des postes entre femmes et hommes dans les données d'origine et dans les données prédites.

## **Etapes à réaliser**
* Etape 0 : Données sur Hadoop.

* Etape 1 : Script pour récupérer les données en local.
  * Hdfs dfs -get … entre les systèmes de fichiers hdfs et Linux.
  * Protocole SCP entre les systèmes de fichiers de la VM Linux et de notre pc.
  
* Etape 2 : Script pour envoyer les données chiffrées sur une instance EC2.
  * Création de l’instance EC2.
  * Connexion SSH.
  * Installation de python et mise en place de la sécurité.
  * Création d’un bucket et transfert des données en SCP.
  
* Etape 3 : Mise en place d’un modèle d’apprentissage (script python).

* Etape 4 : Entraînement du modèle et création du fichier predict.csv
  * Script pour exporter les résultats dans un autre bucket.
  
* Etape 5 : Déplacement des données résultats vers une BDD NoSQL.
  * Mettre en place une base de données MongoDB.
  * Utilisation d'un script d'export vers MongoDB 
 
## Documentation annexe
* *AWS_README* : rapide description des étapes à mettre en place pour l'utilisation d'AWS dans le cadre du projet et explication de certains choix.
* *README_scripts* : description des cas d'utilisation de chacun des scripts.
* 
