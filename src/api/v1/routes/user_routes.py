from typing import List
from fastapi import APIRouter, Depends
from src.application.dto.user_dto import UserDTO
from src.core.dependencies import user_service
from src.application.use_cases.user_service import UserService
from src.application.dto.user_dto import UserDTO

router = APIRouter()

@router.get("/", response_model = List[UserDTO])
def get_users(user_service: UserService = Depends(user_service)):  
    users = user_service.get_users()
    return [UserDTO(id=user.id, name=user.name, email=user.email, password=user.password) for user in users] 

@router.post("/", response_model=UserDTO)
def create_user(user_data: UserDTO, user_service: UserService = Depends(user_service)):
    user_create = user_service.create_user(user_data)
    return UserDTO(id=user_create.id, name=user_create.name, email=user_create.email, password=user_create.password)

@router.get("/{user_id}")
def get_user(user_id: int, user_service: UserService = Depends(user_service)):  
    return user_service.get_user_by_id(user_id)

@router.get("/{user_id}/roles")
async def get_user_roles(user_id: int, user_service: UserService = Depends(user_service)):  
    return await user_service.get_user_roles(user_id)

