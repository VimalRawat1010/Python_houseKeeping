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
tissue = [];
# print all the first cell of all the rows
for row in cur.fetchall():
    print row[:1]
    tissue.append(row[:1])

print (tissue)
db.close()


####################### Method 2

