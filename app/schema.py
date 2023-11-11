from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DeviceInfo(BaseModel):
    token: str
    username: Optional[str]

    class Config:
        orm_mode = True


class Configuration(BaseModel):
    modelUrl: str
    frequency: int
    federated: bool

    class Config:
        orm_mode = True

class Item(BaseModel):
    created: datetime
    name: str
    content: bytes

    class Config:
        orm_mode = True