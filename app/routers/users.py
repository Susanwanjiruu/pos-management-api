from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.services.users import UserService
from app.schemas.users import UserCreate, UserResponse, UserLogin
from typing import List

router = APIRouter(prefix="/users", tags=["User Accounts"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_new_staff_account(user_in: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.register_new_user(user_in)

@router.get("/{user_id}", response_model=UserResponse)
def get_single_user_details(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.fetch_user_by_id(user_id)

@router.get("/", response_model=List[UserResponse])
def list_all_staff_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.fetch_all_users(skip=skip, limit=limit)

@router.post("/login", response_model=UserResponse)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.authenticate(credentials)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_staff_account(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    service.remove_user(user_id)