import sqlite3

# either creates or connects to database
connection = sqlite3.connect("notes.db")

# for running SQL commands
cursor = connection.cursor()

print("connected to database (SQLITE)")

