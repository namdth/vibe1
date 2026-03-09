import random
from sqlalchemy.orm import Session
from database import SessionLocal
import models

names = [
"Nguyen Van An","Tran Minh Duc","Le Hoang Nam","Pham Tuan Anh",
"Nguyen Minh Quan","Hoang Gia Bao","Do Anh Tuan","Pham Quang Huy",
"Tran Duc Minh","Nguyen Hoang Long"
]

majors = [
"Computer Science",
"Data Science",
"Artificial Intelligence",
"Information Systems",
"Software Engineering"
]

classes = ["C01","C02","C03","C04"]

db: Session = SessionLocal()

for i in range(1,201):

    student = models.Student(
        student_id=f"SV{i:03}",
        name=random.choice(names),
        birth_year=random.randint(2002,2005),
        major=random.choice(majors),
        gpa=round(random.uniform(2.0,4.0),2),
        class_id=random.choice(classes)
    )

    db.add(student)

db.commit()

print("Inserted 200 students!")