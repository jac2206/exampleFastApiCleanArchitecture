from sqlalchemy.orm import Session
from sqlalchemy.sql import text 
from src.domain.entity.user_db import UserDB 

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self):
        query = text("SELECT id, name, email, password FROM dbo.[User]")  # ✅ Usando text()
        result = self.db.execute(query).fetchall()
        return result
    
    def get_user(self, user_id: int):
        query = text(f"SELECT id, name, email, password FROM dbo.[User] WHERE id={user_id}")  # ✅ Usando text()
        result = self.db.execute(query).fetchone()
        return result

    def create_user(self, name, email, password):
        self.db.execute(
            "INSERT INTO users (name, email, password) VALUES (:name, :email, :password)",
            {"name": name, "email": email, "password": password}
        )
        self.db.commit()
    
    def get_users_v2(self):
        return self.db.query(UserDB).all()

    def create_user_v2(self, user: UserDB):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
