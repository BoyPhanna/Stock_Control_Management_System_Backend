from fastapi import  HTTPException
from app.db.schemas.user_schema import  UserCreate
from app.db.models.user_model import UserModel
from sqlalchemy.orm import Session




class UserService:
    def __init__(self):
        pass
        
    def create_user(user: UserCreate ,db:Session):
        db_user = UserModel(**user.model_dump())
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


    def read_users(db):
        return db.query(UserModel).all()


    def read_user(user_id: int,db):
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="user not found")
        return db_user


    def update_user(user_id: int, user: UserCreate,db):
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="user not found")
        for key, value in user.model_dump().users():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user


    def delete_user(user_id: int,db):
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="user not found")
        db.delete(db_user)
        db.commit()
        return {"message": "user deleted"}