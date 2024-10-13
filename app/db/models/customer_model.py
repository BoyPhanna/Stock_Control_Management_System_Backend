from sqlalchemy import Column, Integer, String,DateTime
from app.db.database import Base
from datetime import datetime
from app.db.models.people_mixin import PeopleMixin
from app.db.models.time_stamp_mixin import TimestampMixin



class CustomerModel(Base,PeopleMixin,TimestampMixin):
    __tablename__="customers"
    
    
