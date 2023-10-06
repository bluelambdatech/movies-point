import os
import pandas as pd
from dotenv import load_dotenv
#import pyodbc

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
