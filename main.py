
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal
import crud
from fastapi.templating import Jinja2Templates
import pandas as pd
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_students(request: Request, db: Session = Depends(get_db)):
    students = crud.get_students(db)
    total, avg_gpa, major_stats = crud.statistics(db)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "students": students,
        "total": total,
        "avg_gpa": avg_gpa,
        "major_stats": major_stats
    })

@app.get("/add", response_class=HTMLResponse)
def add_student_page(request: Request):
    return templates.TemplateResponse("add_student.html", {"request": request})

@app.post("/add")
def add_student(
    student_id: str = Form(...),
    name: str = Form(...),
    birth_year: int = Form(...),
    major: str = Form(...),
    gpa: float = Form(...),
    class_id: str = Form(...),
    db: Session = Depends(get_db)
):
    student = models.Student(
        student_id=student_id,
        name=name,
        birth_year=birth_year,
        major=major,
        gpa=gpa,
        class_id=class_id
    )

    crud.create_student(db, student)
    return RedirectResponse("/", status_code=303)

@app.get("/delete/{student_id}")
def delete(student_id: str, db: Session = Depends(get_db)):
    crud.delete_student(db, student_id)
    return RedirectResponse("/", status_code=303)

@app.get("/search", response_class=HTMLResponse)
def search(request: Request, name: str, db: Session = Depends(get_db)):
    students = crud.search_student(db, name)
    total, avg_gpa, major_stats = crud.statistics(db)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "students": students,
        "total": total,
        "avg_gpa": avg_gpa,
        "major_stats": major_stats
    })

@app.get("/export")
def export_csv(db: Session = Depends(get_db)):
    students = crud.get_students(db)

    data = []
    for s in students:
        data.append({
            "student_id": s.student_id,
            "name": s.name,
            "birth_year": s.birth_year,
            "major": s.major,
            "gpa": s.gpa,
            "class_id": s.class_id
        })

    df = pd.DataFrame(data)
    path = "students_export.csv"
    df.to_csv(path, index=False)

    return FileResponse(path, filename="students_export.csv")
