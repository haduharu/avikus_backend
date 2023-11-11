from .database import Base
from sqlalchemy import Column, String, Boolean, Integer, DateTime, LargeBinary
from datetime import datetime

class Item(Base):
    __tablename__ = "Item"
    id = Column(Integer, primary_key = True, autoincrement = True)
    created = Column(DateTime, default=datetime.utcnow)
    name = Column(String)
    content = Column(LargeBinary)