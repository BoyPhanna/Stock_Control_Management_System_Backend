from fastapi import  Depends,APIRouter
from typing import List
from sqlalchemy.orm import Session
from app.db.database import get_db

from app.db.schemas.item_schema import ItemResponse , ItemCreate
from app.db.services.item_services import ItemService



router = APIRouter()

# Create: สร้างสินค้าใหม่
@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate,db:Session = Depends(get_db)):
    return ItemService.create_item(item=item,db=db)

# Read: อ่านสินค้าทั้งหมด
@router.get("/", response_model=List[ItemResponse])
async def read_items(db: Session = Depends(get_db)):
    return ItemService.read_items(db=db)

# Read: อ่านสินค้าตาม ID
@router.get("/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    return ItemService.read_item(item_id=item_id,db=db)

# Update: อัปเดตสินค้าตาม ID
@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    return ItemService.update_item(item_id=item_id,item=item,db=db)

# Delete: ลบสินค้าตาม ID
@router.delete("/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    return ItemService.delete_item(item_id=item_id,db=db)