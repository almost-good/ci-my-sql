import os
import datetime
import pymysql
import cryptography


# Get username from My Workspase
username = os.getenv('almost_good')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='KravaKravaKrava93!',
                            db='Chinook')


# * Cursor as DICT
""" 
    try:
        # Run a query
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM Genre;"
            cursor.execute(sql)
            for row in cursor:
                print(row)
            # * result = cursor.fetchall()
            # * print(result)
    finally:
        # Close the connection, regardless of whether the above was successful
        connection.close()
"""


# * Create the TABLE
"""
try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute('''CREATE TABLE IF NOT EXISTS `Friends` (name char(20), age int, DOB datetime);''')
        connection.commit()
        # Note that above will still display a warning (not error) 
        # if the table already exists
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""


# * Insert into table
"""
try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""


# * Execute Many
"""
try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
        ("Jim", 56, "1955-05-09 13:12:45"),
        ("Fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""


# * UPDATE
"""
try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""


# * ALTERNATE UPDATE
"""
try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
        (23, 'Bob'))
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""


# * UPDATE MANY
"""
try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
        (24, 'Jim'),
        (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""


# * DELETE
"""
try:
    # Run a query
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""


# * Alternate DELETE
"""
try:
    # Run a query
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'bob')
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""


# * DELETE MANY
"""
try:
    # Run a query
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['bob', 'Jim'])
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""


# * DELETE WHERE IN 

try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['Fred', 'Fred']
        # Prepare a string with the same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
