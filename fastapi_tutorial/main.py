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
async def create_user(
    name: str, surname: str, email: str, db: Session = Depends(get_db)
):
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
    name: str,
    age: int,
    description: str,
    subject: str,
    user_id: int,
    db: Session = Depends(get_db),
):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    student = Student(
        name=name,
        age=age,
        description=description,
        subject=subject,
        user=db_user,  # Burada birbaşa `User` obyektini istifadə edirik
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


@app.post("/address/")
async def create_address(city: str, student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(
            status_code=404, detail=f"Student with id {student_id} not found"
        )

    address = Address(
        city=city,
        student=db_student,  # Burada birbaşa `Student` obyektini istifadə edirik
    )
    db.add(address)
    db.commit()
    db.refresh(address)
    return address


@app.put("/student")
async def student_update(
    id: int,
    name: str,
    description: str,
    age: int,
    subject: str,
    user_id: int,
    db: Session = Depends(get_db),
):
    # Mövcud tələbəni tapırıq
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        return {"error": "Student not found"}

    # Eyni user_id başqa bir tələbəyə aid olub olmadığını yoxlayırıq
    existing_student_with_user_id = (
        db.query(Student).filter(Student.user_id == user_id, Student.id != id).first()
    )

    if existing_student_with_user_id:
        return {"error": f"user_id {user_id} is already assigned to another student"}

    # Tələbəni yeniləyirik
    student.name = name
    student.description = description
    student.age = age
    student.subject = subject
    student.user_id = user_id

    db.commit()
    db.refresh(student)
    return {"message": "Student updated successfully", "student": student}


@app.put("/users")
async def user_update(
    id: int, name: str, email: str, surname: str, db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == id).first()

    if not user:
        return {"error": "User not found"}

    user.id = id
    user.name = name
    user.email = email
    user.surname = surname
    db.commit()
    db.refresh(user)
    return user