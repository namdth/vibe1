
from sqlalchemy.orm import Session
import models

def get_students(db: Session):
    return db.query(models.Student).all()

def create_student(db: Session, student):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def delete_student(db: Session, student_id: str):
    student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if student:
        db.delete(student)
        db.commit()

def search_student(db: Session, name: str):
    return db.query(models.Student).filter(models.Student.name.contains(name)).all()

def statistics(db: Session):
    students = db.query(models.Student).all()
    total = len(students)

    avg_gpa = sum([s.gpa for s in students]) / total if total else 0

    major_stats = {}
    for s in students:
        major_stats[s.major] = major_stats.get(s.major, 0) + 1

    return total, round(avg_gpa,2), major_stats
