import pyodbc
import pandas as pd

# Replace these values with your database connection details
server = '172.18.5.180'
database = 'sunbeam_mssqldb_eTimeTrackLite_stud'
username = 'dbda'
password = 'manager'

# Establish a connection to the database
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_string)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Example query
query = "SELECT * FROM Dev"
cursor.execute(query)
# df = pd.read_sql(query, cursor)
# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close cursor and connection
cursor.close()
connection.close()
df = pd.read_sql(query, con=connection)