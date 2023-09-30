import pypyodbc as odbc
import pandas as pd
from credential import username, password

# variables
server = 'mysqlserver1414.database.windows.net'
database = 'mySampleDatabase'
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
print('SQL db connection successful this and that far')


#this function creates a table in the db
def create_movies_table():
     """ Table should be created here. """
     print("Creating a Table...")
     try:
         conn = get_conn()
         cursor = conn.cursor()
         cursor.execute("""
             CREATE TABLE Moviesss5 (
                rotten_tomatoes_link varchar(255),
                movie_title varchar(255),
                movie_info varchar(max),
                critics_consensus varchar(255),
                content_rating varchar(255),
                genres varchar(255),
                directors varchar(255),
                authors varchar(255),
                actors varchar(max),
                original_release_date varchar(255),
                streaming_release_date varchar(255),
                runtime varchar(255),
                production_company varchar(255),
                tomatometer_status varchar(255),
                tomatometer_rating varchar(255),
                tomatometer_count varchar(255),
                audience_status varchar(255),
                audience_rating varchar(255),
                audience_count varchar(255),
                tomatometer_top_critics_count varchar(255),
                tomatometer_fresh_critics_count varchar (255),
                tomatometer_rotten_critics_count varchar (255)

             );
         """)
         conn.commit()
         return conn
     except Exception as e:
         # Items may already exist
         print(e)
     return "Person API"

test_create = create_movies_table()
print('Table create function completed for Moviesss4')

import csv
csv_file_path = 'C:/Users/nened/Downloads/rotten_tomatoes_movies (1).csv'
df = pd.read_csv(csv_file_path)
print(df["movie_title"][0])


def clean(row):
    for r in row.index:
        row[r] = "".join("".join("".join("".join(str(row[r]).split('(')).split('-')).split(')')).split("'"))
        row[r] = "".join(row[r].split("--"))

    return row


df = df.apply(clean, axis=1)
def read_data():

    cursor = get_conn().cursor()
    for index, row in df.iterrows():
        print("OMO")
        cursor.execute("""
         INSERT INTO [Moviesss5](rotten_tomatoes_link, movie_title,movie_info, critics_consensus,
             content_rating, genres, directors, authors, actors, original_release_date, streaming_release_date, runtime,
             production_company, tomatometer_status, tomatometer_rating, tomatometer_count, audience_status, audience_rating,
             audience_count, tomatometer_top_critics_count, tomatometer_fresh_critics_count, tomatometer_rotten_critics_count)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?);
         """, (
            row.rotten_tomatoes_link, row.movie_title,row.movie_info, row.critics_consensus, row.content_rating,
            row.genres, row.directors, row.authors, row.actors, row.original_release_date, row.streaming_release_date, row.runtime,
            row.production_company, row.tomatometer_status, row.tomatometer_rating, row.tomatometer_count, row.audience_status,
            row.audience_rating, row.audience_count, row.tomatometer_top_critics_count, row.tomatometer_fresh_critics_count,
            row.tomatometer_rotten_critics_count))

        print(index)

        cursor.commit()

#          return conn
#      except Exception as e:
#      # Table may already exist
#          print(e)
#
#      return "Person API"
#
test_insert = read_data()
print("Table insert function completed")








# import csv
# csv_file_path = 'C:/Users/nened/Downloads/rotten_tomatoes_movies (1).csv'
# def populate_movies_table_from_csv():
#     """Populate the Movies_Project table with data from a CSV file."""
#     try:
#         conn = get_conn()
#         cursor = conn.cursor()
#         print("just checking")
#         # Open and read the CSV file
#         with open(csv_file_path, 'r', newline='') as csvfile:
#             csvreader = csv.reader(csvfile, delimiter=',')
#
#             # Skip the header row if it exists
#             # next(csvreader, None)
#         print(csvreader.line_num)
#
#         # Insert data from CSV into the table
#         for row in csvreader:
#             # cursor.execute("""
#             #                 INSERT INTO Movies_Project11 (
#             #                     rotten_tomatoes_link, movie_title, movie_info, critics_consensus,
#             #                     content_rating, genres, directors, authors, actors, original_release_date,
#             #                     streaming_release_date, runtime, production_company, tomatometer_status,
#             #                     tomatometer_rating, tomatometer_count, audience_status, audience_rating,
#             #                     audience_count, tomatometer_top_critics_count, tomatometer_fresh_critics_count ,
#             #                     tomatometer_rotten_critics_count
#             #                 ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#             #             """, tuple(row))
#             print(row)
#         conn.commit()
#         return conn
#     except Exception as e:
#         # Table may already exist
#         print(e)
#     return "Person API"
#
# populate_test = populate_movies_table_from_csv()
# print("Data population in Table successful")


# import pypyodbc as odbc
# import pandas as pd
# from credential import username, password
#
# # ... (other code)
#
# def create_movies_table():
#     """ Table should be created here. """
#     print("Creating a Table...")
#     try:
#         conn = get_conn()
#         cursor = conn.cursor()
#         cursor.execute("""
#             CREATE TABLE Moviesss (
#                rotten_tomatoes_link varchar(255),
#                movie_title varchar(255),
#                movie_info varchar(5000),
#                critics_consensus varchar(255),
#                content_rating varchar(255),
#                genres varchar(255),
#                directors varchar(255),
#                authors varchar(255),
#                actors varchar(255),
#                original_release_date varchar(255),
#                streaming_release_date varchar(255),
#                runtime varchar(255),
#                production_company varchar(255),
#                tomatometer_status varchar(255),
#                tomatometer_rating varchar(255),
#                tomatometer_count varchar(255),
#                audience_status varchar(255),
#                audience_rating varchar(255),
#                audience_count varchar(255),
#                tomatometer_top_critics_count varchar(255),
#                tomatometer_fresh_critics_count varchar (255),
#                tomatometer_rotten_critics_count varchar (255)
#             );
#         """)
#         conn.commit()
#         return conn
#     except Exception as e:
#         # Items may already exist
#         print(e)
#     return "Person API"
#
# test_create = create_movies_table()
# print('Table create function completed for Moviesss')
#
# import csv
# csv_file_path = 'C:/Users/nened/Downloads/rotten_tomatoes_movies (1).csv'
# df = pd.read_csv(csv_file_path)
#
# def read_data():
#     try:
#         conn = get_conn()
#         cursor = conn.cursor()
#         for index, row in df.iterrows():
#
#
#             try:
#                 cursor.execute("""
#                     INSERT INTO [Moviesss](rotten_tomatoes_link, movie_title, movie_info, critics_consensus,
#                         content_rating, genres, directors, authors, actors, original_release_date, streaming_release_date, runtime,
#                         production_company, tomatometer_status, tomatometer_rating, tomatometer_count, audience_status, audience_rating,
#                         audience_count, tomatometer_top_critics_count, tomatometer_fresh_critics_count, tomatometer_rotten_critics_count)
#                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
#                 """, (
#                     row.rotten_tomatoes_link, row.movie_title, row.movie_info, row.critics_consensus, row.content_rating,
#                     row.genres, row.directors, row.authors, row.actors, row.original_release_date, row.streaming_release_date, row.runtime,
#                     row.production_company, row.tomatometer_status, row.tomatometer_rating, row.tomatometer_count, row.audience_status,
#                     row.audience_rating, row.audience_count, row.tomatometer_top_critics_count, row.tomatometer_fresh_critics_count,
#                     row.tomatometer_rotten_critics_count
#                 ))
#                 conn.commit()
#             except Exception as e:
#                 # Log the problematic row
#                 print(e)
#         return conn
#     except Exception as e:
#         # Table may already exist
#         print(e)
#     return "Person API"
#
#cls

# test_insert = read_data()
# print("Table insert function completed")

