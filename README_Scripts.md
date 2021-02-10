# Utilisation des scripts

## 1) Installation des données sur Hadoop

Grâce au script [LocalToHadoop.sh](https://github.com/AriTortue/big_data_project/blob/main/exportLocalToHadoop.sh), nous pouvons poussés nos données dans Hadoop avec la commande hdfs dfs -put.
Il suffit juste de fournir le nom du fichier à exporter.

## 2) Récupération des données d'Hadoop

De la même manière grâce au script [HadoopToLocal.sh](https://github.com/AriTortue/big_data_project/blob/main/exportHadoopToLocal.sh), nous pouvons récupérer nos données avec la commande hdfs dfs -get.

## 3) Export des données vers l'EC2
En fournissant l'adresse IP de l'EC2, le path et le nom du fichier à exporter vers l'EC2 au script [exportEC2.sh](https://github.com/AriTortue/big_data_project/blob/main/exportEC2.sh), il s'occupera de pousser les données dans le cloud AWS via scp.
Cependant, nous avons dû mettre le chemin de la paire de clés en dur (ici, /home/sobun/bigdata avec bigdata le nom de la paire de clés) car nous avions des problèmes de sécurité en passant le chemin en variable.

## 4) Export des données traitées vers mongodb

Pour exporter nos données vers mongodb, nous avons utilisé le script [exportEC2toMongoDB.sh](https://github.com/AriTortue/big_data_project/blob/main/exportEC2toMongoDB.sh). Il faut fournir au script l'hostname de l'ec2, le port sur lequel mongodb est en cours d'exécution, le nom de la database, le nom de la collection et le chemin d'accès du fichier à importer.
