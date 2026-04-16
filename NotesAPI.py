from fastapi import FastAPI # Import the FastAPI class from the fastapi module to create a web application
from pydantic import BaseModel # Import the BaseModel class from the pydantic module to define data models for request validation
app = FastAPI() # Create an instance of the FastAPI class to define the application
class Note(BaseModel): # Define a data model for notes by creating a class that inherits from BaseModel, which allows for automatic validation and serialization of the data
    title: str
    content: str
notes = [] # Create an empty list to store the notes
@app.post("/notes") # Define a route for creating a note, which will be accessed via a POST request, and specify the path as "/notes". The function to be called when this endpoint is accessed will be defined below
def create_note(note: Note):
    notes.append(note) # Add the note to the list of notes
    return {"message": "Note created successfully"} # Return a JSON response containing a message indicating that the note was created successfully. To test this endpoint, you can use an API testing tool like Postman or curl to send a POST request to http://localhost:8000/notes with a JSON body containing the note's information, for example: {"title": "My First Note", "content": "This is the content of my first note."}. The response will be a JSON object containing the success message, for example: {"message": "Note created successfully"}
@app.get("/notes") # Define a route for retrieving all notes, which will be accessed via a GET request, and specify the path as "/notes". The function to be called when this endpoint is accessed will be defined below
def get_notes():
    return notes # Return the list of notes as a JSON response. To test this endpoint, you can use an API testing tool like Postman or curl to send a GET request to http://localhost:8000/notes. The response will be a JSON array containing all the notes that have been created, for example: [{"title": "My First Note", "content": "This is the content of my first note."}, {"title": "My Second Note", "content": "This is the content of my second note."}] 
@app.get("/notes/search") # Define a route for searching notes by title, which will be accessed via a GET request, and specify the path as "/notes/search". The function to be called when this endpoint is accessed will be defined below
def search_notes(title: str):
    matching_notes = [note for note in notes if title.lower() in note.title.lower()] # Use a list comprehension to filter the notes based on whether the search term (title) is present in the note's title, ignoring case sensitivity
    return matching_notes # Return the list of matching notes as a JSON response. To test this endpoint, you can use an API testing tool like Postman or curl to send a GET request to http://localhost:8000/notes/search?title=search_term, replacing "search_term" with the title you want to search for. The response will be a JSON array containing all the notes that match the search term, for example: [{"title": "My First Note", "content": "This is the content of my first note."}] if you search for "First".