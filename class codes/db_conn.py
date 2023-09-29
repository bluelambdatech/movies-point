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
    cursor.execute("""CREATE TABLE [MOVIES_POINT].[Person]
                    (
                        PersonId INT IDENTITY PRIMARY KEY,
                        FirstName NVARCHAR(128) NOT NULL,
                        MiddelInitial NVARCHAR(10),
                        LastName NVARCHAR(128) NOT NULL,
                        DateOfBirth DATE NOT NULL
                    )""")
    cursor.commit()
    cursor.close()


df = pd.DataFrame({
    "PersonId":[1, 2, 3, 4, 5],
    "FirstName": ["Omolewa11", "Bukola11", "David11", "Nene11", "Joseph11"],
    "MiddelInitial": ["Oq", "Bq", "Cq", "Oq", "Kq"],
    "LastName": ["Omolewa", "Bukola", "David", "Nene", "Joseph"],
    "DateOfBirth": ["2/3/2004", "2/3/2004", "2/3/2004", "2/3/2004", "2/3/2004"]
})

df.to_csv("data.csv")


def read_csv(file_name):
    for chunk in pd.read_csv(file_name, chunksize=10000):
        yield chunk

#
# for df in read_csv("large_file.csv"):
#     process_dataframe(df)


def read_data():
    sf = pd.read_csv("data.csv")
    cursor = get_conn().cursor()
    for index, row in sf.iterrows():
        cursor.execute("INSERT INTO [MOVIES_POINT].[Person] (FirstName, MiddelInitial, LastName, DateOfBirth) values(?,?, ?, ?)",
                       row.FirstName, row.MiddelInitial, row.LastName, row.DateOfBirth)
    cursor.commit()
    cursor.close()


read_data()

"INSERT INTO [MOVIES_POINT].[Person] (FirstName, MiddelInitial, LastName, DateOfBirth) values('Ogechi', 'O', 'Adaramola', '02/23/2023')"