import sqlite3
from sqlite3 import Error

# Create a connection


def create_connection(file_path):
    """
    Creates a database connection to the SQLite database specified by the 'path'.

    Parameters:
    - path - Provide path to a database file. A new database is created where non exists.

    Return:
    - Returns a Connection Object or None.
    """
    try:
        connection = sqlite3.connect(r'file_path')
    except Error as e:
        connection = None
        print(f'Error! Occured while creating a connection! --> {e}')
    return connection

# Read table from the database


def read_table(connection, command):
    """
    Queries all rows of the 'table' provided as a parameter.

    Parameters:
    - connection - Provide a connection object to the desired database.
    - table      - Give the name of the table to query from the database.

    Return:
    - A list of rows related to the queried table.
    """

    try:
        cur = connection.cursor()
        cur.execute(command)
        rows = cur.fetchball()
    except Error as e:
        rows = None
        print(f'This Error Occured while querying the {table} table! --> {e}')
    return rows
