from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()

students = {}
next_student_id = 1

@app.get("/")
def home():
    return {"message": "Welcome to stuudent api"}

class Student(BaseModel):
    name:str
    age:int

@app.post("/student")
def create_student(student: Student):

    global next_student_id

    students[next_student_id] = {
        "id": next_student_id,
        "name": student.name,
        "age": student.age
    }

    next_student_id += 1

    return {
        "message": "Student created successfully",
        "student": students[next_student_id - 1]
    }

@app.get("/students")
def get_students():
    return students

@app.get("/student/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]

@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[student_id] = {
        "id": student_id,
        "name": student.name,
        "age": student.age
    }

    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }

@app.delete("/student/{student_id}")
def delete_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }