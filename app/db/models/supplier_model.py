from sqlalchemy import Column, Integer, String,DateTime
from app.db.database import Base
from datetime import datetime
from app.db.models.time_stamp_mixin import TimestampMixin
from app.db.models.people_mixin import PeopleMixin


class SupplierModel(Base,TimestampMixin,PeopleMixin):
    __tablename__="suppliers"
    
    
