#! /bin/sh
echo "IP address of EC2?"
read address
echo "Path of file to export?"
read filepath
echo "What is the filename?"
read filename

scp -i /home/sobun/bigdata $filepath/$filename ec2-user@$address:/home/ec2-user
