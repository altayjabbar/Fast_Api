from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Verilənlər bazası URL (SQLite, PostgreSQL və s.)
DATABASE_URL = "sqlite:///./test.db"

# SQLite üçün engine yarat
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Sessiya yaradıcısı
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Baza modeli üçün əsas sinif
Base = declarative_base()
