from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# Create a FastAPI instance
app = FastAPI()

# Sample student records
studentsRecord = {
    1: {"name": "Nifemi", "age": 16, "year": "part 3"},
    2: {"name": "SoluTion", "age": 29, "year": "part 5"},
    3: {"name": "Samuel", "age": 21, "year": "part 3"},
    4: {"name": "Taiwo", "age": 67, "year": "part 2"},
    5: {"name": "Timmy", "age": 34, "year": "part 4"},
}

# Define a Pydantic model for student
class Student(BaseModel):
    name: str
    age: int
    year: str

# Define a Pydantic model for updating student information
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

# Root endpoint
@app.get("/")
def index():
    return {"name": "Welcome to root endpoint."}

# Endpoint to get a student record by ID
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description='Student record id', gt=0, lt=len(studentsRecord))):
    if student_id not in studentsRecord:
        return {"Error": f"No student with id {student_id} found!"}
    return studentsRecord[student_id]

# Endpoint to get all student records
@app.get("/get-all-students")
def get_all_students():
    return studentsRecord

# Endpoint to get a student record by name
@app.get("/get-student-by-name/{student_id}")
def get_student_by_name(*, name: Optional[str] = None, student_id: int):
    for student_id in studentsRecord:
        if studentsRecord[student_id].name == name:
            return studentsRecord[student_id]
    return {"Error": "No student record found!"}

# Endpoint to create a new student record
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in studentsRecord:
        return {"Error": "Student already exists"}
    
    studentsRecord[student_id] = student
    return studentsRecord[student_id]

# Endpoint to update a student record
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in studentsRecord:
        return {"Error": f"Student with id {student_id} does not exist"}
    
    if student.name is not None:
        studentsRecord[student_id].name = student.name

    if student.age is not None:
        studentsRecord[student_id].age = student.age

    if student.year is not None:
        studentsRecord[student_id].year = student.year

    return studentsRecord[student_id]

# Endpoint to delete a student record
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in studentsRecord:
        return {"Error": f"Student with id {student_id} does not exist!"}
    
    del studentsRecord[student_id]
    return {"Message": f"Student with id {student_id} has been deleted!"}