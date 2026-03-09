
# Student Management System (Vibe Coding Assignment)

## Student Information
Name: Nguyen Van Nam

## Tech Stack
- FastAPI
- SQLite
- HTML (Jinja2)
- Pandas

## Features
- Add student
- View student list
- Delete student
- Search student by name
- Statistics (total students, average GPA, students by major)
- Export data to CSV

## Project Structure
student-management
│
├── main.py
├── database.py
├── models.py
├── crud.py
├── requirements.txt
├── README.md
│
├── templates
│   ├── index.html
│   └── add_student.html
│
└── data
    └── students.db

## Run Project

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn main:app --reload

Open browser:

http://127.0.0.1:8000
