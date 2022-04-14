import sys
import psycopg2
import pandas as pd

postgres_params = {
    "host": "host",
    "database": "database",
    "user": "user",
    "password": "password"
}


def connect_postgresql(postgres_params=postgres_params):
    """ Connect to the PostgreSQL database server """
    db = postgres_params["database"]
    print(db)
    conn = None
    try:
        # connect to the PostgreSQL server
        print(f'Connecting to the {db} PostgreSQL database...')
        conn = psycopg2.connect(**postgres_params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn


def create_pandas_table(sql_query, database):
    table = pd.read_sql_query(sql_query, database)
    return table
