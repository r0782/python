from fastapi import FastAPI, HTTPException
app = FastAPI()
students = {
    1: {"name": "John", "age": 20, "grade": "A"},
    2: {"name": "Jane", "age": 22, "grade": "B"},
    3: {"name": "Doe", "age": 21, "grade": "C"}
}
@app.get("/students/{student_id}")
def read_student(student_id: int):
    if student_id in students:
        return students[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student not found")