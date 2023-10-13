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
print('1. SQL db connection successful')


# this function creates a table in the db
def create_person_table():
    """ Table should be created here. """
    print("Creating a Table...")
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE User_Profile (
                ID int NOT NULL PRIMARY KEY IDENTITY,
                LastName varchar(255) NULL,
                FirstName varchar(255) NULL,
                Email varchar(255) NOT NULL,
                UserName varchar(255) NOT NULL,
                DateOfBirth varchar(50),
                Gender varchar(50),
            CONSTRAINT UC_User_Profile UNIQUE (Email, UserName)
            );
        """)
        conn.commit()
        return conn
        return conn
    except Exception as e:
        # Items may already exist
        print(e)
    return "Person API"

test_create = create_person_table()
print('2. Table create function completed')


# this function inserts items into the table(s)
def insert_table():
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            """
            SET IDENTITY_INSERT User_Profile ON
            INSERT INTO User_Profile (
                ID, LastName, FirstName, Email, UserName, DateOfBirth, Gender)
                VALUES (1, 'Doe', 'John', johndoe@aol.com, johndoe123, 01-10-1960, Male);
                SET IDENTITY_INSERT User_Profile OFF
                """)
        conn.commit()
        return conn
    except Exception as e:
        # Table may already exist
        print(e)
    return "Person API"

test_insert = insert_table()
print('3. Table insert function completed')

def alter_table():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        """
        ALTER TABLE User_Profile  
            ADD CONSTRAINT UC_User_Profile UNIQUE (Email, UserName);
            
            """)
    conn.commit()
    return conn


test_alter = alter_table()
print("4. Table alter function completed")

# this function reads from the db
def get_persons():
    conn = get_conn()
    dfm = pd.read_sql("SELECT * FROM Persons", conn)
    return dfm

df = get_persons()
print(df)
print("5. Get persons function completed....")


