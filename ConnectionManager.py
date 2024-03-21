import psycopg2
import os
import json

conn = None

def getConnection():
    global conn
    # If the connection is not defined, then this function defines it
    if (conn is None) or (not conn.closed is 0):
        # Getting login credentials
        database = os.environ["DB"]
        username = os.environ["DB_UN"]
        password = os.environ["DB_PW"]
        hostname = "sc2-cit-b112"
        port = "5432"

        # Setting up the connection
        conn = psycopg2.connect(database=database, user=username, password=password, host=hostname, port=port)
            
    # Returns the connection
    return conn

def closeConnection():
    # If the connection is not defined, then this function does nothing
    if (not conn is None) and (conn.closed is 0):
        conn.close()