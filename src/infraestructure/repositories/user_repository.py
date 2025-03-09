from sqlalchemy.orm import Session
from sqlalchemy.sql import text 
from src.domain.entity.user_db import UserDB 
import json

class UserRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_users(self):
        query = text("SELECT id, name, email, password FROM dbo.[User]")  # ✅ Usando text()
        result = self.db.execute(query).fetchall()
        return result
    5
    def get_user(self, user_id: int):
        query = text("SELECT id, name, email, password FROM dbo.[User] WHERE id=:id")  # ✅ Usando text()
        result = self.db.execute(query, {"id": user_id}).fetchone()
        return result

    def create_user(self, user_data: dict):
        query = text("INSERT INTO dbo.[User] (id, name, email, password) VALUES (:id, :name, :email, :password)")
        self.db.execute(query, user_data)
        self.db.commit()

    # def create_user(self, user_data: dict):
    #     # user_data_json = json.loads(json.dumps(user_data))
    #     query = text("INSERT INTO dbo.[User] (id, name, email, password) VALUES (:id, :name, :email, :password")  # ✅ Usando text()
    #     params = {
    #         "id": int(user_data["id"]),
    #         "name": str(user_data["name"]),
    #         "email": str(user_data["email"]),
    #         "password": str(user_data["password"])
    #     }
    #     self.db.execute(query, params )
    #     self.db.commit()
    
    def get_users_v2(self):
        return self.db.query(UserDB).all()

    def get_user_v2(self, user_id: int):
        return self.db.query(UserDB).filter(UserDB.id == user_id).first()

    def create_user_v2(self, user: UserDB):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
