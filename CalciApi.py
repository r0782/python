from fastapi import FastAPI # Import the FastAPI class from the fastapi module
app = FastAPI() # Create an instance of the FastAPI class to define the application
@app.get("/add") # Define the endpoint for addition, which will be accessed via a GET request, and specify the path as "/add", and the function to be called when this endpoint is accessed will be defined below
def add(x: int, y: int): # Define the function to perform addition, which takes two parameters x and y, both of type int, and returns a JSON response containing the result of the addition
    return {"result": x + y} # Return the result as a JSON response,To run this add function you can use the following URL in your browser or API testing tool: http://localhost:8000/add?x=5&y=3, where you can replace 5 and 3 with any integers you want to add together. The response will be a JSON object containing the result of the addition, for example: {"result": 8}
@app.get("/subtract") # Define the endpoint for subtraction
def subtract(x: int, y: int): # Define the function to perform subtraction
    return {"result": x - y} # Return the result as a JSON response
@app.get("/multiply") # Define the endpoint for multiplication
def multiply(x: int, y: int): # Define the function to perform multiplication
    return {"result": x * y} # Return the result as a JSON response
@app.get("/divide") # Define the endpoint for division
def divide(x: int, y: int): # Define the function to perform division
    if y == 0:
        return {"error": "Division by zero is not allowed"}# Check for division by zero and return an error message if y is zero
    return {"result": x / y}# Return the result as a JSON response if division is valid
@app.get("/power") # Define the endpoint for exponentiation
def power(x: int, y: int):# Define the function to perform exponentiation
    return {"result": x ** y} # Return the result as a JSON response
@app.get("/modulus") # Define the endpoint for modulus
def modulus(x: int, y: int): # Define the function to perform modulus
    if y == 0:
        return {"error": "Modulus by zero is not allowed"} # Check for modulus by zero and return an error message if y is zero
    return {"result": x % y} # Return the result as a JSON response