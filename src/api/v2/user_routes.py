# from fastapi import APIRouter, Depends
# from src.application.use_cases.user_service import UserService
# from src.infrastructure.repositories.user_repository import UserRepository
# from src.infrastructure.database import get_db

# router = APIRouter()

# @router.get("/users/{user_id}", response_model=UserDTO)
# def get_user(user_id: int, db=Depends(get_db)):
#     user_service = UserService(UserRepository(db))
#     return user_service.get_user(user_id)

# @router.post("/users/", response_model=UserDTO)
# def create_user(name: str, email: str, password: str, db=Depends(get_db)):
#     user_service = UserService(UserRepository(db))
#     return user_service.create_user(name, email, password)
