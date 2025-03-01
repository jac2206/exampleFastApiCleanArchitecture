from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "name":"Julian",
        "age": 31
    }

