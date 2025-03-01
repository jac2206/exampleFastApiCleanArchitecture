from src.application.use_cases.auth_service import AuthService
from typing import List, Optional
from src.domain.entity.user import User
from src.core.base_service import BaseService

class UserService(BaseService):  # ✅ Hereda de BaseService
    def __init__(self, auth_service: AuthService):
        """Inicializa la lista con tres usuarios quemados"""
        self.users: List[User] = [
            User(id=1, name="Julian", email="julian@example.com", password="secure123"),
            User(id=2, name="Ana", email="ana@example.com", password="pass456"),
            User(id=3, name="Carlos", email="carlos@example.com", password="mypassword")
        ]
        self.auth_service = auth_service

    def get_users(self) -> List[User]:
        """Devuelve todos los usuarios, ahora usando BaseService"""
        return self.execute(lambda: self.users)  # ✅ Manejo de errores con `execute`

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Busca un usuario por ID"""
        return self.execute(lambda: next((user for user in self.users if user.id == user_id), None))

    def create_user(self, user: User) -> User:
        """Crea un usuario y lo guarda en la lista"""
        return self.execute(lambda: self._add_user(user))

    def _add_user(self, user: User) -> User:
        """Método privado para agregar un usuario a la lista"""
        if any(u.email == user.email for u in self.users):
            raise ValueError("El email ya está registrado")  # `BaseService` lo atrapará
        self.users.append(user)
        return user

    async def get_user_roles(self, user_id: int):
        """Obtiene roles del usuario usando AuthService"""
        return self.execute(lambda: self.auth_service.get_roles(user_id))  # ✅ Protección contra fallos en AuthService
