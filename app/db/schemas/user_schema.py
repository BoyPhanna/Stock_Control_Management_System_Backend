from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import Field

class User(BaseModel):
    username: str
    password: str
    role:str
    
class UserCreate(User):
    pass

class UserResponse(User):
    id: int
    date: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True