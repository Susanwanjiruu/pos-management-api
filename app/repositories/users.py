from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, hashed_password: str, full_name: str, role: str):
        db_user = User(
            username=username,
            password=hashed_password,
            full_name=full_name,
            role=role,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.user_id == user_id).first()

    def get_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def get_all_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()

    def update_user(self, user_id: int, updated_fields: dict):
        db_user = self.get_by_id(user_id)
        if not db_user:
            return None

        for key, value in updated_fields.items():
            if hasattr(db_user, key):
                setattr(db_user, key, value)

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.get_by_id(user_id)
        if not db_user:
            return False

        self.db.delete(db_user)
        self.db.commit()
        return True