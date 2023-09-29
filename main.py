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

test_conn = get_conn()
print('connection successful')


def create_person_table():
    """ Table should be created here. """
    print("Creating a Table...")
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE Persons (
                ID int NOT NULL PRIMARY KEY IDENTITY,
                FirstName varchar(255),
                LastName varchar(255)
            );
        """)
        conn.commit()
        return conn
    except Exception as e:
        # Table may already exist
        print(e)
    return "Person API"

test_create = create_person_table()
print('Function exceution completed')


