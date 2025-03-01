from pydantic import BaseModel, EmailStr

class UserDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
