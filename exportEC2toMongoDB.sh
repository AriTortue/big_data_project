#! /bin/sh
echo "Hostname?"
read hostname
echo "Database name?"
read dbname
echo "Collection name?"
read cname
echo "Path of file to export?"
read filepath
echo "What is the filename?"
read filename

mongoimport --host $hostname --port 27017 --db $dbname --collection $cname --file $filepath/$filename
