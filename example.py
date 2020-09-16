from database.queries import create_connection, read_table
from database.statements import select

# Examples of how to use these new modules explained

# Connect to the database you want to use.
# It it important in the case where you have different databases you want to use in this single project.
connection = create_connection('database/school.db')

# Generate SQLite queries with which to query the database instead having to write the command yourself
# It is important because it can be used to generate commands to query different tables or different columns in the same table.
command = select('', 'students')

# This gives you a list of the names of students in the database
student_names = read_table(connection, command)
