from sqlalchemy import Column, Integer, String
from src.infraestructure.database import Base

class UserDB(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
