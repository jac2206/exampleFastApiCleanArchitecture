# from typing import List, Optional
# from fastapi import HTTPException
# from src.domain.entity.user import User
# from src.application.use_cases.auth_service import AuthService

# class UserService:
#     def __init__(self, auth_service: AuthService):
#         self.users: List[User] = [
#             User(id=1, name="Julian", email="julian@example.com", password="secure123"),
#             User(id=2, name="Ana", email="ana@example.com", password="pass456"),
#             User(id=3, name="Carlos", email="carlos@example.com", password="mypassword")
#         ]
#         self.auth_service = auth_service

#     def get_users(self) -> List[User]:
#         try:
#             return self.users
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Error al obtener usuarios: {str(e)}")

#     def get_user_by_id(self, user_id: int) -> Optional[User]:
#         try:
#             user = next((u for u in self.users if u.id == user_id), None)
#             if not user:
#                 raise HTTPException(status_code=404, detail="Usuario no encontrado")
#             return user
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Error al buscar usuario: {str(e)}")

#     def create_user(self, user: User) -> User:
#         try:
#             self.users.append(user)
#             return user
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Error al crear usuario: {str(e)}")

# class UserService:
#     def __init__(self, auth_service: AuthService):
#         """Inicializa la lista con tres usuarios quemados"""
#         self.users: List[User] = [
#             User(id=1, name="Julian", email="julian@example.com", password="secure123"),
#             User(id=2, name="Ana", email="ana@example.com", password="pass456"),
#             User(id=3, name="Carlos", email="carlos@example.com", password="mypassword")
#         ]
#         self.auth_service = auth_service

#     def get_users(self) -> List[User]:
#         """Devuelve todos los usuarios"""
#         return self.users

#     def get_user_by_id(self, user_id: int) -> Optional[User]:
#         """Busca un usuario por ID"""
#         for user in self.users:
#             if user.id == user_id:
#                 return user
#         return None

#     def create_user(self, user: User) -> User:
#         """Crea un usuario y lo guarda en la lista"""
#         self.users.append(user)
#         return user

#     async def get_user_roles(self, user_id: int):
#         return self.auth_service.get_roles(user_id)  # 👈 Llamando a 