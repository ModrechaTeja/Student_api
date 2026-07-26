from fastapi import APIRouter, HTTPException
from app.models.student import Student

router = APIRouter()

students = {}
next_student_id = 1


@router.get("/")
def home():
    return {"message": "Welcome to Student API"}


@router.post("/student")
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


@router.get("/students")
def get_students():
    return students


@router.get("/student/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


@router.put("/student/{student_id}")
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


@router.delete("/student/{student_id}")
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