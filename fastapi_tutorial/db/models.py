from sqlalchemy import Column, Integer, String,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    student = relationship("Student", back_populates="user", uselist=False)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer,primary_key = True)
    name = Column(String)
    age = Column(Integer)
    description = Column(String)
    subject = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    user = relationship("User", back_populates="student")