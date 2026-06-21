import sqlite3

# either creates or connects to database
connection = sqlite3.connect("notes.db")

# for running SQL commands
cursor = connection.cursor()

print("connected to database (SQLITE)")

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY, 
    title TEXT, 
    content TEXT
)
""")

connection.commit()
connection.close()

