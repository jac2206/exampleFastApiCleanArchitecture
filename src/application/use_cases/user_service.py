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
