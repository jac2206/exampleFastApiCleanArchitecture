from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.core.config import Config

DATABASE_URL = Config.get_database_url()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db  # Proporciona la sesión para ser usada en dependencias
    finally:
        db.close()  # Asegura que la sesión se cierre correctamente
