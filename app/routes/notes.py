from fastapi import APIRouter
from app import database
from app.schemas import Note

router = APIRouter()

@router.post("/notes")
def create_note(note: Note): 
    #SQL query
    query = "INSERT INTO notes (title, content) VALUES (?, ?)"

    # Exectue query with values from request
    database.cursor.exectue(query, (note.title, note.content))

    # Save changes
    database.connection.commit()

    return {"message": "Note created successfully..0"}