import os
import pandas as pd
from dotenv import load_dotenv
import pyodbc

load_dotenv()

server = f'{os.getenv("db_name")}.database.windows.net'
database = os.getenv("db_name")
username = "bluelambda"
password = os.getenv("password")
driver= '{ODBC Driver 18 for SQL Server}'


def get_conn():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    return conn


def create_table():
    #  create a cursor
    cursor = get_conn().cursor()
    cursor.execute("""CREATE TABLE [MOVIES_POINT].[USER_PROFILE]
                    (ID int NOT NULL PRIMARY KEY IDENTITY,
                    LastName varchar(255) NULL,
                    FirstName varchar(255) NULL,
                    Email varchar(255) NOT NULL,
                    UserName varchar(255) NOT NULL,
                    DateOfBirth varchar(50),
                    Gender varchar(50),
            CONSTRAINT UC_User_Profile UNIQUE (Email, UserName));""")
    cursor.commit()
    cursor.close()


def insert_into_table(LastName, FirstName, Email, UserName, DateOfBirth, Gender):
    cursor = get_conn().cursor()
    cursor.execute("INSERT INTO [MOVIES_POINT].[USER_PROFILE] (LastName, FirstName, Email, UserName, DateOfBirth, Gender) values(?,?, ?, ?, ?, ?)",
        LastName, FirstName, Email, UserName, DateOfBirth, Gender)

    cursor.commit()
    cursor.close()


def read_from_table(UserName):
    cursor = get_conn().cursor()
    print(UserName, "OMOLEWA")
    print(type(UserName))
    dfm = cursor.execute("SELECT * FROM [MOVIES_POINT].[USER_PROFILE] WHERE UserName = '%s'" % UserName)
    return dfm.fetchall()


# create_table()

#insert_into_table("Adaramola", "Omolewa", "omolewah@gmail.com", "omolewah", "02/28/2023", "Male")
#print(read_from_table("omolewah", "omolewah@gmail.com"))
# df = pd.DataFrame({
#     "PersonId":[1, 2, 3, 4, 5],
#     "FirstName": ["Omolewa11", "Bukola11", "David11", "Nene11", "Joseph11"],
#     "MiddelInitial": ["Oq", "Bq", "Cq", "Oq", "Kq"],
#     "LastName": ["Omolewa", "Bukola", "David", "Nene", "Joseph"],
#     "DateOfBirth": ["2/3/2004", "2/3/2004", "2/3/2004", "2/3/2004", "2/3/2004"]
# })
#
# df.to_csv("data.csv")
#
#
# def read_csv(file_name):
#     for chunk in pd.read_csv(file_name, chunksize=10000):
#         yield chunk
#
# #
# # for df in read_csv("large_file.csv"):
# #     process_dataframe(df)
#
#
# def read_data():
#     sf = pd.read_csv("data.csv")
#     cursor = get_conn().cursor()
#     for index, row in sf.iterrows():
#         cursor.execute("INSERT INTO [MOVIES_POINT].[Person] (FirstName, MiddelInitial, LastName, DateOfBirth) values(?,?, ?, ?)",
#                        row.FirstName, row.MiddelInitial, row.LastName, row.DateOfBirth)
#     cursor.commit()
#     cursor.close()
#
#
# read_data()
#
# "INSERT INTO [MOVIES_POINT].[Person] (FirstName, MiddelInitial, LastName, DateOfBirth) values('Ogechi', 'O', 'Adaramola', '02/23/2023')"
#
# def create_person_table():
#     """ Table should be created here. """
#     print("Creating a Table...")
#     try:
#         conn = get_conn()
#         cursor = conn.cursor()
#         cursor.execute("""
#             CREATE TABLE USER_PROFILE (
#                 ID int NOT NULL PRIMARY KEY IDENTITY,
#                 LastName varchar(255) NULL,
#                 FirstName varchar(255) NULL,
#                 Email varchar(255) NOT NULL,
#                 UserName varchar(255) NOT NULL,
#                 DateOfBirth varchar(50),
#                 Gender varchar(50),
#             CONSTRAINT UC_User_Profile UNIQUE (Email, UserName)
#             );
#         """)
#         conn.commit()
#         return conn
#         return conn
#     except Exception as e:
#         # Items may already exist
#         print(e)
#     return "Person API"
#
#
# # this function inserts items into the table(s)
# def insert_table():
#     try:
#         conn = get_conn()
#         cursor = conn.cursor()
#         cursor.execute(
#             """
#             SET IDENTITY_INSERT User_Profile ON
#             INSERT INTO User_Profile (
#                 ID, LastName, FirstName, Email, UserName, DateOfBirth, Gender)
#                 VALUES (1, 'Doe', 'John', johndoe@aol.com, johndoe123, 01-10-1960, Male);
#                 SET IDENTITY_INSERT User_Profile OFF
#                 """)
#         conn.commit()
#         return conn
#     except Exception as e:
#         # Table may already exist
#         print(e)
#     return "Person API"
#
#
# # this function reads from the db
# def get_persons():
#     conn = get_conn()
#     dfm = pd.read_sql("SELECT * FROM Persons", conn)
#     return dfm