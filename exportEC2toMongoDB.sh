#! /bin/sh

mongoimport --host "hostname de l'ec2" --port 27017 --db "nom de la database" --collection "nom de la collection" --file "chemin d'accès du fichier à importer"
