from fastapi import  Depends,APIRouter
from typing import List
from sqlalchemy.orm import Session
from app.db.database import get_db

from app.db.schemas.user_schema import UserCreate , UserResponse
from app.db.services.user_services import UserService



router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate,db:Session = Depends(get_db)):
    return UserService.create_user(user=user,db=db)

@router.get("/", response_model=List[UserResponse])
async def read_users(db: Session = Depends(get_db)):
    return UserService.read_users(db=db)

@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.read_user(user_id=user_id,db=db)

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return UserService.update_user(user_id=user_id,user=user,db=db)

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.delete_user(user_id=user_id,db=db)