from typing import List
from fastapi import APIRouter, Depends
from src.application.dto.user_dto import UserDTO
from src.core.dependencies import user_service_db
from src.application.use_cases.user_service_db import UserServiceDB
from src.application.dto.user_dto import UserDTO

router = APIRouter()

@router.get("/", response_model = List[UserDTO])
def get_users(user_service_db: UserServiceDB = Depends(user_service_db)):  
    users = user_service_db.get_users()
    return [UserDTO(id=user.id, name=user.name, email=user.email, password=user.password) for user in users]

@router.get("/{user_id}")
def get_user(user_id: int, user_service_db: UserServiceDB = Depends(user_service_db)):  
    user = user_service_db.get_user_id(user_id)
    return UserDTO(id=user.id, name=user.name, email=user.email, password=user.password)

@router.get("/orm", response_model = List[UserDTO])
def get_users_orm(user_service_db: UserServiceDB = Depends(user_service_db)):
    users = user_service_db.get_users_orm()
    return [UserDTO(id=user.id, name=user.name, email=user.email, password=user.password) for user in users]
