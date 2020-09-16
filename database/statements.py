def select(column, table):
	"""
	Creates an SQLite SELECT statement.

	Parameters:
	- column - Provide the name of the column in the 'table' from which to query.
	- table - Provide the name of the table in the 'database' from which to query.

	Return:
	- Returns a strind with the SELECT statement eg. SELECT * FROM cities
	"""
	
    command = f"""SELECT {column} FROM {table}"""
    return command
