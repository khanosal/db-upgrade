# db-upgrade

This script will run sql scripts in specified folder against a database after converting the first three characters into an integer value and comparing that with a version set in a versionTable

Script should be executed one level above the directory specified by parameter:

  --directory-with-sql-scripts

The script runs in python 2.7 and works with mysql 5.7 it assumes you have the correct dependencies installed to import the following modules:

os,
argparse,
mysql.connector,
mysql.connector import errorcode

Run command:

python upgrade.py
