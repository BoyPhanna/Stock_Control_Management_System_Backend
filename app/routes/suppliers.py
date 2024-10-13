from fastapi import  Depends,APIRouter
from typing import List
from sqlalchemy.orm import Session
from app.db.database import get_db

from app.db.schemas.supplier_schema import SupplierCreate , SupplierResponse
from app.db.services.supplier_services import SupplierService



router = APIRouter()

# Create: สร้างสินค้าใหม่
@router.post("/", response_model=SupplierResponse)
async def create_supplier(supplier: SupplierCreate,db:Session = Depends(get_db)):
    return SupplierService.create_supplier(supplier=supplier,db=db)

# Read: อ่านสินค้าทั้งหมด
@router.get("/", response_model=List[SupplierResponse])
async def read_suppliers(db: Session = Depends(get_db)):
    return SupplierService.read_suppliers(db=db)

# Read: อ่านสินค้าตาม ID
@router.get("/{supplier_id}", response_model=SupplierResponse)
async def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    return SupplierService.read_supplier(supplier_id=supplier_id,db=db)

# Update: อัปเดตสินค้าตาม ID
@router.put("/{supplier_id}", response_model=SupplierResponse)
async def update_supplier(supplier_id: int, supplier: SupplierCreate, db: Session = Depends(get_db)):
    return SupplierService.update_supplier(supplier_id=supplier_id,supplier=supplier,db=db)

# Delete: ลบสินค้าตาม ID
@router.delete("/{supplier_id}")
async def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    return SupplierService.delete_supplier(supplier_id=supplier_id,db=db)