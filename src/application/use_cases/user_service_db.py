from typing import List, Optional
from src.domain.entity.user import User
from src.core.base_service import BaseService
from src.infraestructure.repositories.user_repository import UserRepository

class UserServiceDB(BaseService,):  # ✅ Hereda de BaseService
    def __init__(self, user_repository: UserRepository):
        # self
        self.user_repository = user_repository

    def get_users(self) -> List[User]:
        """Devuelve todos los usuarios, ahora usando BaseService"""
        return self.execute(lambda: self.user_repository.get_users())
    
    def get_user_id(self, user_id: int) -> User:
        return self.execute(lambda: self.user_repository.get_user(user_id))
    
    # def create_user(self, user):
    #     return self.user_repository.create_user(user)

    def get_users_orm(self) -> List[User]:
        return self.execute(lambda: self.user_repository.get_users_v2()) 

    # def get_users(self):
    #     """Devuelve todos los usuarios, ahora usando BaseService"""
    #     return self.execute(lambda: self.user_repository.get_users())

    # def get_users(self) -> List[User]:
    #     """Devuelve todos los usuarios, ahora usando BaseService"""
    #     return self.execute(lambda: [
    #         User(id=1, name="Julian", email="julian@example.com", password="123"),
    #         User(id=2, name="Ana", email="ana@example.com", password="456"),
    #         User(id=3, name="Carlos", email="carlos@example.com", password="789"),
    #     ])
