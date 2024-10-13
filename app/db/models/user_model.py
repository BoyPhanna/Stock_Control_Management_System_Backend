from sqlalchemy import Column, Integer, String,DateTime
from app.db.database import Base
from app.db.models.time_stamp_mixin import TimestampMixin



class UserModel(Base,TimestampMixin):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    username=Column(String,nullable=False)
    password=Column(String,nullable=False)
    role=Column(String,nullable=False)
    