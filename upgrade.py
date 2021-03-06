import os
import argparse
import mysql.connector
from mysql.connector import errorcode

# - './your-script.your-lang directory-with-sql-scripts username-for-the-db db-host db-name db-password'
parser = argparse.ArgumentParser(description='Process database credentials and script locations')
parser.add_argument('--directory-with-sql-scripts', required=True,
                    help='directory which sql scripts are held')

parser.add_argument('--username-for-the-db', required=True,
                    help='db-username')

parser.add_argument('--db-host', required=True,
                    help='db-username')

parser.add_argument('--db-name', required=True,
                     help='db-username')

parser.add_argument('--db-password', required=True,
                    help='db-username')

# parsing params and assigning them to variables
args = parser.parse_args()
sql_scripts_dir = args.directory_with_sql_scripts
db_user = args.username_for_the_db
db_host = args.db_host
db_name = args.db_name
db_password = args.db_password

# creating connection to mysql db using prams
cnx = mysql.connector.connect(user=db_user, password=db_password,
                              host=db_host,
                              database=db_name,
                              use_pure=False)

cursor = cnx.cursor()

# getting current version from versionTable and assigning it to variable version
query = ("SELECT * FROM versionTable")
cursor.execute(query)
version = cursor.fetchone()[0]
print 'current version = ',version

# sorts then loops through all files in provided directory
for filename in (sorted(os.listdir(sql_scripts_dir))):
    # converts first three chars of file name to integer then compares with current version
    script_version = int(filename[:3])
    if script_version > version:
        print 'searching for newer version'
        os.chdir(sql_scripts_dir)
        #parses then executes script from current file
        file = open(filename, 'r')
        sql = s = " ".join(file.readlines())
        cursor = cnx.cursor()
        print 'executing script',filename
        cursor.execute(sql)
        # updates versionTable with new version
        update_statement = ("UPDATE versionTable SET version = %(version)s")
        cursor.execute(update_statement, { 'version': script_version })
        cnx.commit()
        os.chdir("..")
        print 'updated current version to',script_version

cnx.close()
