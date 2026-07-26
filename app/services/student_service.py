from app import database

from app import database

def create_student(student):

    database.students[database.next_student_id] = {
        "id": database.next_student_id,
        "name": student.name,
        "age": student.age
    }

    database.next_student_id += 1

    return database.students[database.next_student_id - 1]


def get_students():
    return database.students


def get_student(student_id):
    return database.students.get(student_id)


def update_student(student_id, student):

    database.students[student_id] = {
        "id": student_id,
        "name": student.name,
        "age": student.age
    }

    return database.students[student_id]


def delete_student(student_id):
    return database.students.pop(student_id)