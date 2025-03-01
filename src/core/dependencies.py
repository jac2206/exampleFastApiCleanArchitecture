from src.application.use_cases.user_service import UserService
from src.application.use_cases.auth_service import AuthService
from fastapi import Depends

def auth_service():
    return AuthService()

def user_service(auth_service: AuthService = Depends(auth_service)):  
    return UserService(auth_service)  # 👈 Se inyecta la dependencia