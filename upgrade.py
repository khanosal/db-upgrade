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

# grabs sql_scripts_dir variable and prints ordered list of files
for filename in (sorted(os.listdir(sql_scripts_dir))):
    print filename

cnx = mysql.connector.connect(user=db_user, password=db_password,
                              host=db_host,
                              database=db_name,
                              use_pure=False)

cursor = cnx.cursor()

query = ("SELECT * FROM versionTable")

cursor.execute(query)

for (version) in cursor:
    print version

cursor.close()

cnx.close()

# for (first_name, last_name, hire_date) in cursor:
#   print("{}, {} was hired on {:%d %b %Y}".format(
#     last_name, first_name, hire_date))


# try:
#   cnx = mysql.connector.connect(user=db_user,
#                                 database=db_name)
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cnx.close()
