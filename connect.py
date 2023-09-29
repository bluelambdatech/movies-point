import pypyodbc as odbc
import pandas as pd
from credentials import username, password

# variables 
server = 'moviessqlserver.database.windows.net'
database = 'movieslist'
odbc_driver = '{ODBC Driver 18 for SQL Server}'

conn_string = (
    f"Driver={odbc_driver};"
    f"Server=tcp:{server},1433;"
    f"Database={database};"
    f"Uid={username};"
    f"Pwd={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=60;")


# function to connect to sql db
def get_conn():
    ''' function to connect to sql db'''
    conn = odbc.connect(conn_string)
    return conn

sql_conn = get_conn()
print(sql_conn)