from pydantic import BaseModel
from typing import Optional

class Supplier(BaseModel):
    name: str
    phone: str
    
class SupplierCreate(Supplier):
    pass

class SupplierResponse(Supplier):
    id: int

    class Config:
        from_attributes = True