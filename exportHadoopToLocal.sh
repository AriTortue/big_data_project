#! /bin/sh
hdfspath=/user/root/projet/ #Dossier du fichier à exporter
path=/home/sobun/ #Path du dossier d'import
echo "What is the filename?"
read filename
hdfs dfs -get $hdfspath$filename $path 
