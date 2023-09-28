#This Python code demonstrates how to connect to a Microsoft Azure SQL Database using the pyodbc library.

import os  #imports python modules os for environment variables


#creating a connection string that contains info about the azure sql database i want to connect to including server address
#database name , authentication credentials

AZURE_SQL_CONNECTIONSTRING="Driver={ODBC Driver 18 for SQL Server};Server=tcp:mysqlserver1414.database.windows.net,1433;Database=mySampleDatabase;Uid=*****;Pwd=*****;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

os.environ["AZURE_SQL_CONNECTIONSTRING"] = AZURE_SQL_CONNECTIONSTRING  #sets environment variable and assigns the connection string to an environment variable named AZURE_SQL ***

connection_string = os.environ["AZURE_SQL_CONNECTIONSTRING"]

print(os.environ) #prints all environment variables to the console. For informational purposes and helps you verify that the AZURE_SQL_CONNECTIONSTRING variable has been set

print(os.environ.get('APPDATA'))
###prints the path to the user's application data directory. Again,
# it's for informational purposes and not directly related to the database connection###

import pyodbc
server = 'mysqlserver1414.database.windows.net'  #insert your azure server name
database = 'mySampleDatabase'    #insert your sql database name
username = '******' # enter your user name
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