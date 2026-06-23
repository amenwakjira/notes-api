from fastapi import APIRouter
from app import database
from app.schemas import Note

router = APIRouter()

@router.post("/notes")
def create_notes(note: Note): 
    #SQL query
    query = "INSERT INTO notes (title, content) VALUES (?, ?)"

    # Exectue query with values from request
    database.cursor.execute(query, (note.title, note.content))

    # Save changes
    database.connection.commit()

    return {"message": "Note created successfully..0"}

# @router.post("/notes")
# def get_notes(): 
#     database.cursor.execute("SELECT * FROM notes")
#     all_entries = database.cursor.fetchall()
#     # Print out your data rows
#     for row in all_entries:
#         print(row)

#     # Save changes
#     database.connection.commit()

#     return {"message": "Notes outputted successfully..0"}