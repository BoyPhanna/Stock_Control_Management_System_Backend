from fastapi import  HTTPException
from app.db.schemas.supplier_schema import  SupplierCreate
from app.db.models.supplier_model import SupplierModel
from sqlalchemy.orm import Session




class SupplierService:
    def __init__(self):
        pass
        
    def create_supplier(supplier: SupplierCreate ,db:Session):
        db_supplier = SupplierModel(**supplier.model_dump())
        
        db.add(db_supplier)
        db.commit()
        db.refresh(db_supplier)
        return db_supplier


    def read_suppliers(db):
        return db.query(SupplierModel).all()


    def read_supplier(supplier_id: int,db):
        db_supplier = db.query(SupplierModel).filter(SupplierModel.id == supplier_id).first()
        if db_supplier is None:
            raise HTTPException(status_code=404, detail="supplier not found")
        return db_supplier


    def update_supplier(supplier_id: int, supplier: SupplierCreate,db):
        db_supplier = db.query(SupplierModel).filter(SupplierModel.id == supplier_id).first()
        if db_supplier is None:
            raise HTTPException(status_code=404, detail="supplier not found")
        for key, value in supplier.model_dump().suppliers():
            setattr(db_supplier, key, value)
        db.commit()
        db.refresh(db_supplier)
        return db_supplier


    def delete_supplier(supplier_id: int,db):
        db_supplier = db.query(SupplierModel).filter(SupplierModel.id == supplier_id).first()
        if db_supplier is None:
            raise HTTPException(status_code=404, detail="Supplier not found")
        db.delete(db_supplier)
        db.commit()
        return {"message": "Supplier deleted"}