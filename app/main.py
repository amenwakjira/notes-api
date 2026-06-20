from fastapi import FastAPI
from . import database

app = FastAPI()

# Route: Opening Message
@app.get("/")
def read_root():
    return "Welcome! Time to take some notes!!"

# Route: get all notes
@app.get("/notes")
def get_notes(): 
    return [
        {"id": 1, "title": "First Note Kinda Nervous"}, 
        {"id": 2, "title": "But really these don't count, just checking I know what's happening"}
    ] 

# Route: create a note
@app.post("/notes")
def create_note(note: dict): 
    return {
        "message": "note added successfully", 
        "note": note
    }

