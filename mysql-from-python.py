import os
import pymysql
import cryptography

# Get username from My Workspase
username = os.getenv('almost_good')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='KravaKravaKrava93!',
                            db='Chinook')


try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()