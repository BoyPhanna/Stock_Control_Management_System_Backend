from sqlalchemy import Column, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

class TimestampMixin:
    @declared_attr
    def create_at(cls):
        return Column(DateTime, default=datetime.now)
    
    @declared_attr
    def update_at(cls):
        return Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    @declared_attr
    def delete_at(cls):
        return Column(DateTime, nullable=True)
    
    def soft_delete(self):
        self.delete_at = datetime.now()
