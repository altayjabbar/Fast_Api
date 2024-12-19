from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session,relationship
from db.models import Base, User, Student
from db.database import engine, SessionLocal

app = FastAPI()

# Cədvəlləri yarat
Base.metadata.create_all(bind=engine)


# Sessiya generatoru
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
async def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()


@app.post("/student/")
async def create_student(
    name: str, age: int, description: str, subject: str, db: Session = Depends(get_db)
):
    student = Student(name=name, age=age, description=description, subject=subject)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
