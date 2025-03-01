# from sqlalchemy.orm import Session
# from src.domain.entity.user import User
# from src.domain.interfaces.user_repository import IUserRepository
# # from src.infrastructure.database import Base, engine

# class UserRepository(IUserRepository):
#     def __init__(self, db: Session):
#         self.db = db

#     def get_by_id(self, user_id: int) -> User:
#         return self.db.query(User).filter(User.id == user_id).first()

#     def create(self, user: User) -> User:
#         self.db.add(user)
#         self.db.commit()
#         self.db.refresh(user)
#         return user
