# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 11:32:26 2017

@author: vimal
"""

#!/usr/bin/python
import MySQLdb ## No timezone support


db = MySQLdb.connect(host="localhost",    # hostname, localhost for testing
                     user="root",         # MySQL username
                     passwd="abc123",     # MySQL password
                     db="test")           # MySQL database name

# Creating a Cursor object.
cur = db.cursor()

# Use all the SQL you like
#cur.execute("SELECT  * FROM beerclub LIMIT 10")
cur.execute("DESC  beerclub ")
table_column_names = [];
# print all the first cell of all the rows
for row in cur.fetchall():
    print row[:1]
    table_column_names.append(row[:1])

print (table_column_names)
db.close()


####################### Method 2

import pymysql
import pymysql.cursors
import time   

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='abc123',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        #now = datetime.datetime()
        str_now = now.date().isoformat()
        print str_now
        # Create a new record
        cursor.execute("INSERT INTO test.beerclub (UserID, date, beers, cost) VALUES (%s, %s, %s, %s)", ('VIR', str_now, 1, 0))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        cursor.execute("SELECT *, FROM test.beerclub WHERE UserID=", "VIR")
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()