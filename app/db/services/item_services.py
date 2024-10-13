from fastapi import  HTTPException, Depends

from app.db.database import  get_db

from app.db.schemas.item_schema import  ItemCreate
from app.db.models.item_model import ItemDB
from sqlalchemy.orm import Session




class ItemService:
    def __init__(self):
        pass
        
    def create_item(item: ItemCreate ,db:Session):
        db_item = ItemDB(**item.model_dump())
        
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item


    def read_items(db):
        return db.query(ItemDB).all()


    def read_item(item_id: int,db):
        db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item


    def update_item(item_id: int, item: ItemCreate,db):
        db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        for key, value in item.model_dump().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item


    def delete_item(item_id: int,db):
        db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        db.delete(db_item)
        db.commit()
        return {"message": "Item deleted"}