#! /bin/sh
path=/home/sobun/ #Path du fichier à exporter
hdfspath=/user/root/projet/ #Dossier d'import
echo "What is the filename?"
read filename
hdfs dfs -get $hdfspath$filename $path 
