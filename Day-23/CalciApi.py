from fastapi import FastAPI
app = FastAPI()
@app.get("/add")
def add(x: int, y: int):
    return {"result": x + y}
@app.get("/subtract")
def subtract(x: int, y: int):
    return {"result": x - y}
@app.get("/multiply")
def multiply(x: int, y: int):
    return {"result": x * y}
@app.get("/divide")
def divide(x: int, y: int):
    if y == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": x / y}
@app.get("/power")
def power(x: int, y: int):
    return {"result": x ** y}
@app.get("/modulus")
def modulus(x: int, y: int):
    if y == 0:
        return {"error": "Modulus by zero is not allowed"}
    return {"result": x % y}