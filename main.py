import pypyodbc as odbc
import pandas as pd
from credential import username, password

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


# This function connects to the sql db
def get_conn():
    ''' function to connect to sql db'''
    conn = odbc.connect(conn_string)
    return conn

test_conn = get_conn()
print('SQL db connection successful')


# this function creates a table in the db
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
        # Items may already exist
        print(e)
    return "Person API"

test_create = create_person_table()
print('Table create function completed')


# this function inserts items into the table(s)
def insert_person():
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            """
            SET IDENTITY_INSERT Persons ON
            INSERT INTO Persons (
                ID, FirstName, LastName) 
                VALUES (1, 'Collins', 'Orighose');
                SET IDENTITY_INSERT Persons OFF
                """)
        conn.commit()
        return conn
    except Exception as e:
        # Table may already exist
        print(e)
    return "Person API"

test_insert = insert_person()
print("Table insert function completed")

# this function reads from the db
def get_persons():
    conn = get_conn()
    dfm = pd.read_sql("SELECT * FROM Persons", conn)
    return dfm

df = get_persons()
print(df)
print("4. Get persons function completed....")


