import psycopg2
import os
import json

conn = None

def getConnection():
    global conn
    # If the connection is not defined, then this function defines it
    if (conn is None) or (not conn.closed is 0):
        # Getting json file
        file = open("creds.json", "r")
        data = json.load(file)

        # Getting login credentials
        database = data["myDB"]["DB"]
        username = data["myDB"]["DB_UN"]
        password = data["myDB"]["DB_PW"]
        hostname = data["myDB"]["DB_HN"]
        port     = data["myDB"]["DB_PORT"]

        # Closing the json file.
        file.close()

        # Setting up the connection
        conn = psycopg2.connect(database=database, user=username, password=password, host=hostname, port=port)
            
    # Returns the connection
    return conn

def closeConnection():
    # If the connection is not defined, then this function does nothing
    if (not conn is None) and (conn.closed is 0):
        conn.close()