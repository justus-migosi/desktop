import sqlite3
from sqlite3 import Error


def create_connection(file):
    """Creates a database connection to the SQLite database specified by 'file'.
       Returns a Connection Object or None.
    """
    try:
        connection = sqlite3.connect(file)
        print("Success! Connection created at ", file)
    except Error as e:
        print(f'Error! Occured while creating a connection! --> {e}')
        connection = None
    return connection

def create_table(connection, table):
    """Creates a table described by the 'table' parameter.
       :param connection: a Connection Object
       :param table: a CREATE TABLE statement
    """
    try:
        c = connection.cursor()
        c.execute(table)
        print("Success! Table has been created.")
    except Error as e:
        print(f'This Error Occured while Creating a table! --> {e}')

def main():
    students_table = """CREATE TABLE IF NOT EXISTS Students (
                            adm_no integer PRIMARY KEY,
                            first_name text NOT NULL,
                            second_name text NOT NULL,
                            third_name text NOT NULL,
                            gender text NOT NULL,
                            telephone int NOT NULL,
                            location text NOT NULL
                            );"""
    connection = create_connection(r'school.db')
    if connection is not None:
        create_table(connection, students_table)
    else:
        print("Error! Failed to establish a connection to the database file.")

if __name__ == '__main__':
    main()