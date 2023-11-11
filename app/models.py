from .database import Base
from sqlalchemy import Column, String, Boolean, Integer, DateTime, LargeBinary
from datetime import datetime


class DeviceInfo(Base):
    __tablename__ = 'DeviceInfo'
    token = Column(String, primary_key = True)
    username = Column(String, default = 'user')


class Configuration(Base):
    __tablename__ = 'Configuration'
    id = Column(Integer, primary_key = True, autoincrement = True)
    modelUrl = Column(String)
    frequency = Column(Integer)
    federated = Column(Boolean)

class Item(Base):
    __tablename__ = "Item"
    id = Column(Integer, primary_key = True, autoincrement = True)
    created = Column(DateTime, default=datetime.utcnow)
    name = Column(String)
    content = Column(LargeBinary)