from fastapi import FastAPI # Import the FastAPI class from the fastapi module to create a web application
from pydantic import BaseModel # Import the BaseModel class from the pydantic module to define data models for request validation
app = FastAPI()# Create an instance of the FastAPI class to define the application
class user(BaseModel):# Define a data model for user information by creating a class that inherits from BaseModel, which allows for automatic validation and serialization of the data
    name: str
    email: str
    age: int
@app.post("/create_user")# Define a route for creating a user, which will be accessed via a POST request, and specify the path as "/create_user". The function to be called when this endpoint is accessed will be defined below
def create_user(user: user):
    return {"message": f"User {user.name} created successfully with email {user.email} and age {user.age}"} # Return a JSON response containing a message that includes the user's name, email, and age, indicating that the user was created successfully. To test this endpoint, you can use an API testing tool like Postman or curl to send a POST request to http://localhost:8000/create_user with a JSON body containing the user's information, for example: {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
