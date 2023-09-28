import pypyodbc as odbc
#import pandas as pd
from credentials import username, password 

server = 'moviessqlserver.database.windows.net' #,1433'
database = 'movieslist'
odbc_driver = '{ODBC Driver 18 for SQL Server}'

conn_str = (
    f"Driver={odbc_driver};"
    f"Server=tcp:{server},1433;"
    f"Database={database};"
    f"Uid={username};"
    f"Pwd={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;")
print(conn_str)

conn = odbc.connect(conn_str)

