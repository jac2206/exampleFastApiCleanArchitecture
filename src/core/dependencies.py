from src.application.use_cases.user_service import UserService
from src.application.use_cases.user_service_db import UserServiceDB
from src.application.use_cases.auth_service import AuthService
from src.infraestructure.repositories.user_repository import UserRepository
from src.infraestructure.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

def auth_service():
    return AuthService()

def user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)

def user_service(auth_service: AuthService = Depends(auth_service)):  
    return UserService(auth_service)  # 👈 Se inyecta la dependencia

def user_service_db(user_repository: UserRepository = Depends(user_repository)):
    return UserServiceDB(user_repository)

