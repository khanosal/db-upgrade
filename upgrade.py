import os
import argparse
import mysql.connector
from mysql.connector import errorcode

# - './your-script.your-lang directory-with-sql-scripts username-for-the-db db-host db-name db-password'
parser = argparse.ArgumentParser(description='Process database credentials and script locations')
parser.add_argument('--directory_with_sql_scripts', required=True,
                    help='directory which sql scripts are held')

parser.add_argument('--username_for_the_db', required=True,
                    help='db-username')

parser.add_argument('--db_host', required=True,
                    help='db-username')

parser.add_argument('--db_name', required=True,
                     help='db-username')

parser.add_argument('--db_password', required=True,
                    help='db-username')

args = parser.parse_args()
sql_scripts_dir = args.directory_with_sql_scripts
db_user = args.username_for_the_db
db_host = args.db_host
db_name = args.db_name
db_password = args.db_password


cnx = mysql.connector.connect(user=db_user, password=db_password,
                              host=db_host,
                              database=db_name,
                              use_pure=False)

cursor = cnx.cursor()

query = ("SELECT * FROM versionTable")

cursor.execute(query)

version = cursor.fetchone()[0]

print 'current version = ',version

# for (version) in cursor:
#     print version

cursor.close()




# grabs sql_scripts_dir variable and prints ordered list of files
for filename in (sorted(os.listdir(sql_scripts_dir))):
    script_version = int(filename[:3])
    if script_version > version:
        print 'searching for newer version'
        os.chdir(sql_scripts_dir)
        file = open(filename, 'r')
        sql = s = " ".join(file.readlines())
        cursor = cnx.cursor()
        print 'executing script',filename
        cursor.execute(sql)
        cnx.commit()

        update_statement = ("UPDATE versionTable SET version = %(version)s")
        cursor.execute(update_statement, { 'version': script_version })

        os.chdir("..")
        print 'updated current version to',script_version

cnx.close()
