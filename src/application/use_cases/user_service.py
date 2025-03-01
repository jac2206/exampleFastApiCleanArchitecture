from src.application.use_cases.auth_service import AuthService
from typing import List, Optional
from src.domain.entity.user import User

class UserService:
    def __init__(self, auth_service: AuthService):
        """Inicializa la lista con tres usuarios quemados"""
        self.users: List[User] = [
            User(id=1, name="Julian", email="julian@example.com", password="secure123"),
            User(id=2, name="Ana", email="ana@example.com", password="pass456"),
            User(id=3, name="Carlos", email="carlos@example.com", password="mypassword")
        ]
        self.auth_service = auth_service

    def get_users(self) -> List[User]:
        """Devuelve todos los usuarios"""
        return self.users

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Busca un usuario por ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def create_user(self, user: User) -> User:
        """Crea un usuario y lo guarda en la lista"""
        self.users.append(user)
        return user

    def get_user_roles(self, user_id: int):
        return self.auth_service.get_roles(user_id)  # 👈 Llamando a otro servicio

# from src.domain.entity.user import User
# from typing import List, Optional

# class UserService:
#     def __init__(self):
#         self.users: List[User] = []  # Simulación de base de datos en memoria

#     def get_users(self):
#         """Devuelve todos los usuarios (simulados)"""
#         return self.users if self.users else [{"name": "Julian", "age": 31}]

#     def get_user_by_id(self, user_id: int) -> Optional[User]:
#         """Busca un usuario por ID"""
#         for user in self.users:
#             if user.id == user_id:
#                 return user
#         return None

#     def create_user(self, user: User):
#         """Crea un usuario y lo guarda en la lista"""
#         self.users.append(user)
#         return user
