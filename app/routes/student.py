from fastapi import APIRouter, HTTPException
from app.models.student import Student
from app.services import student_service

router = APIRouter()

students = {}
next_student_id = 1


@router.get("/")
def home():
    return {"message": "Welcome to Student API"}


@router.post("/student")
def create_student(student: Student):

    created_student = student_service.create_student(student)

    return {
        "message": "Student created successfully",
        "student": created_student
    }


@router.get("/students")
def get_students():
    return student_service.get_students()


@router.get("/student/{student_id}")
def get_student(student_id: int):

    student = student_service.get_student(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.put("/student/{student_id}")
def update_student(student_id: int, student: Student):

    if student_service.get_student(student_id) is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    updated_student = student_service.update_student(student_id, student)

    return {
        "message": "Student updated successfully",
        "student": updated_student
    }


@router.delete("/student/{student_id}")
def delete_student(student_id: int):

    if student_service.get_student(student_id) is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_student = student_service.delete_student(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }