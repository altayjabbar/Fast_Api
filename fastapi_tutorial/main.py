from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal  # Absolute import
from db.models import Base, User, Student, Address  # Absolute import

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Session generator
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
async def create_user(name: str, surname: str, email: str, db: Session = Depends(get_db)):
    user = User(name=name, surname=surname, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

@app.post("/student/")
async def create_student(
    name: str, age: int, description: str, subject: str, user_id: int, db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    
    student = Student(
        name=name,
        age=age,
        description=description,
        subject=subject,
        user=db_user  # Burada birbaşa `User` obyektini istifadə edirik
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.post("/address/")
async def create_address(
    city: str, student_id: int, db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail=f"Student with id {student_id} not found")
    
    address = Address(
        city=city,
        student=db_student  # Burada birbaşa `Student` obyektini istifadə edirik
    )
    db.add(address)
    db.commit()
    db.refresh(address)
    return address