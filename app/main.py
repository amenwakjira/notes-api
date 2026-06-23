from fastapi import FastAPI
from . import database
from app.routes import notes


app = FastAPI()

app.include_router(notes.router)

@app.get("/")
def read_root():
    return "Welcome! Time to take some notes!!"
