import os

import pyodbc
server = 'mysqlserver1414.database.windows.net'  #insert your azure server name
database = '*****'    #insert your sql database name
username = '****' # enter your user name
password = '{****}'  #enter your password
driver= '{ODBC Driver 18 for SQL Server}'


# establishes connection to azure sql database using pyodbc with the below credentials
with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP (1000) * FROM [SalesLT].[Product]")  # executes SQL query and is retreiving top 1000 rows from the table
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))  # fetches aand process results row by row and prints data from first 2 columns
            row = cursor.fetchone()