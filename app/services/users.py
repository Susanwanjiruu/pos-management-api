import bcrypt

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.users import UserRepository
from app.schemas.users import UserCreate, UserLogin


def hash_password(raw_password: str) -> str:
    return bcrypt.hashpw(raw_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(raw_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(raw_password.encode("utf-8"), hashed_password.encode("utf-8"))


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_new_user(self, user_data: UserCreate):
        if self.repository.get_by_username(user_data.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This username is already taken."
            )

        hashed_password = hash_password(user_data.password)
        return self.repository.create_user(
            username=user_data.username,
            hashed_password=hashed_password,
            full_name=user_data.full_name,
            role=user_data.role,
        )

    def fetch_user_by_id(self, user_id: int):
        user = self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with ID {user_id} was not found."
            )
        return user

    def fetch_all_users(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all_users(skip=skip, limit=limit)

    def authenticate(self, credentials: UserLogin):
        user = self.repository.get_by_username(credentials.username)
        if not user or not verify_password(credentials.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password."
            )
        return user

    def remove_user(self, user_id: int):
        self.fetch_user_by_id(user_id)
        return self.repository.delete_user(user_id)