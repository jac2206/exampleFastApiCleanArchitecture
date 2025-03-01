# from src.domain.interfaces.user_repository import IUserRepository
# from src.application.dto.user_dto import UserDTO
# from src.domain.entity.user import User

# class UserService:
#     def __init__(self, user_repository: IUserRepository):
#         self.user_repository = user_repository

#     def get_user(self, user_id: int) -> UserDTO:
#         user = self.user_repository.get_by_id(user_id)
#         if user:
#             return UserDTO(id=user.id, name=user.name, email=user.email)
#         return None

#     def create_user(self, name: str, email: str, password: str) -> UserDTO:
#         new_user = User(id=None, name=name, email=email, password=password)
#         saved_user = self.user_repository.create(new_user)
#         return UserDTO(id=saved_user.id, name=saved_user.name, email=saved_user.email)

# import hashlib
# from src.domain.entity.user import User

# class UserService:
#     def create_user(self, id: int, name: str, email: str, password: str) -> User:
#         """Crea un usuario con la contraseña encriptada"""
#         encrypted_password = self.encrypt_password(password)
#         return User(id, name, email, encrypted_password)

#     def encrypt_password(self, password: str) -> str:
#         """Encripta la contraseña usando SHA256"""
#         return hashlib.sha256(password.encode()).hexdigest()

# from src.domain.entity.user import User
# from src.domain.entity.product import Product
# from src.domain.entity.order import Order
# from src.application.use_cases.user_service import UserService
# from typing import List, Optional

# class OrderService:
#     def __init__(self):
#         self.orders: List[Order] = []  # Simulación de base de datos en memoria
#         self.user_service = UserService()  # Llamando otro servicio dentro de este

#     def create_order(self, user_id: int, product: Product) -> Optional[Order]:
#         """Crea un pedido si el usuario existe"""
#         user = self.user_service.get_user_by_id(user_id)  # Llamando al UserService

#         if not user:
#             return None  # Si el usuario no existe, retorna None

#         new_order = Order(id=len(self.orders) + 1, user=user, product=product)
#         self.orders.append(new_order)
#         return new_order

#     def get_orders(self) -> List[Order]:
#         """Retorna la lista de pedidos"""
#         return self.orders
