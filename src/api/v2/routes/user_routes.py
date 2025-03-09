from typing import List
from fastapi import APIRouter, Depends
from src.application.dto.user_dto import UserDTO
from src.core.dependencies import user_service_db
from src.application.use_cases.user_service_db import UserServiceDB
from src.application.dto.user_dto import UserDTO
from src.core.security import verify_token, verify_api_key

router = APIRouter()

@router.get("/", response_model = List[UserDTO])
def get_users(user_service_db: UserServiceDB = Depends(user_service_db),
    token: dict = Depends(verify_token)  
):  
    users = user_service_db.get_users()
    return [UserDTO(id=user.id, name=user.name, email=user.email, password=user.password) for user in users]

@router.post("/", response_model=UserDTO)
def create_user(user_data: UserDTO, user_service_db: UserServiceDB = Depends(user_service_db),
    token: dict = Depends(verify_token)
):
    user_create = user_service_db.create_user(user_data)
    return UserDTO(id=user_create.id, name=user_create.name, email=user_create.email, password=user_create.password)

@router.get("/orm", response_model = List[UserDTO])
def get_users_orm(user_service_db: UserServiceDB = Depends(user_service_db),
    api_key: str = Depends(verify_api_key)
):
    users = user_service_db.get_users_orm()
    return [UserDTO(id=user.id, name=user.name, email=user.email, password=user.password) for user in users]

@router.get("/{user_id}")
def get_user(user_id: int, user_service_db: UserServiceDB = Depends(user_service_db),
    token: dict = Depends(verify_token)
):  
    user = user_service_db.get_user_id(user_id)
    return UserDTO(id=user.id, name=user.name, email=user.email, password=user.password)

@router.get("/orm/{user_id}")
def get_user(user_id: int, user_service_db: UserServiceDB = Depends(user_service_db),
    api_key: str = Depends(verify_api_key)
):  
    user = user_service_db.get_user_id_orm(user_id)
    return UserDTO(id=user.id, name=user.name, email=user.email, password=user.password)