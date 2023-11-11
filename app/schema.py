from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Item(BaseModel):
    created: datetime
    name: str
    content: bytes

    class Config:
        orm_mode = True