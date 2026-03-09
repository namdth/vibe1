
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Class(Base):
    __tablename__ = "classes"

    class_id = Column(String, primary_key=True, index=True)
    class_name = Column(String)
    advisor = Column(String)

    students = relationship("Student", back_populates="student_class")

class Student(Base):
    __tablename__ = "students"

    student_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    birth_year = Column(Integer)
    major = Column(String)
    gpa = Column(Float)

    class_id = Column(String, ForeignKey("classes.class_id"))

    student_class = relationship("Class", back_populates="students")
