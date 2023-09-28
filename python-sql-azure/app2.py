import os
import pyodbc, struct
from azure import identity

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def get_conn():
    server = 'mysqlserver1414.database.windows.net'
    database = 'mySampleDatabase'
    username = '*******'
    password = '{******}'
    driver = '{ODBC Driver 18 for SQL Server}'
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    return conn

@app.get("/")
def root():
    print("Root of Person API")
    try:
        conn = get_conn()
        cursor = conn.cursor()

        # Table should be created ahead of time in production app.
        cursor.execute("""
            CREATE TABLE Movies (
                rotten_tomatoes_link,
                movie_title varchar(255),
               movie_info varchar(255),
               critics_consensus varchar(255),
               content_rating varchar(255),
               genres varchar(255),
               directors varchar(255),
               authors varchar(255),
               actors varchar(255),
               original_release_date varchar(255),
               streaming_release_date varchar(255),
               runtime varchar(255),
               production_company varchar(255),
               tomatometer_status varchar(255),
               tomatometer_rating varchar(255),
               tomatometer_count varchar(255),
               audience_status varchar(255),
               rating varchar(255),
               tomatometer_top_critics_count varchar(255),
               tomatometer_fresh_critics_count varchar (255),
               tomatometer_rotten_critics_count varchar (255)
               
            );
        """)

        conn.commit()
    except Exception as e:
        # Table may already exist
        print(e)
    return "Movies API is created"
