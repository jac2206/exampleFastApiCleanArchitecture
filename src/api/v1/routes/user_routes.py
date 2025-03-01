from fastapi import APIRouter, Depends
from src.core.dependencies import user_service
from src.application.use_cases.user_service import UserService

router = APIRouter()

@router.get("/user/")
def get_users(user_service: UserService = Depends(user_service)):  
    return user_service.get_users()

@router.get("/user/{user_id}")
def get_user(user_id: int, user_service: UserService = Depends(user_service)):  
    return user_service.get_user_by_id(user_id)

@router.get("/user/{user_id}/roles")
def get_user_roles(user_id: int, user_service: UserService = Depends(user_service)):  
    return user_service.get_user_roles(user_id)