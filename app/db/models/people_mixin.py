from sqlalchemy import Column, DateTime,String,Text,INTEGER,VARCHAR,DATE
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

class PeopleMixin:

    @declared_attr
    def id(cls):
        return Column(INTEGER,primary_key=True)
    @declared_attr
    def name(cls):
        return Column(String,nullable=False,index=True)
    
    @declared_attr
    def sex(cls):
        return Column(VARCHAR, default="M",index=True)
    
    @declared_attr
    def dob(cls):
        return Column(DATE,nullable=False)
    @declared_attr
    def address(cls):
        return Column(Text,nullable=False)
    @declared_attr
    def phone(cls):
        return Column(String)
    
    
