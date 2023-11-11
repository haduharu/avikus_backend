from sqlalchemy.orm import Session
from . import schema, models

def create_item(db: Session, item: schema.Item):
    item_model = models.Item(**item.dict())
    db.add(item_model)
    db.commit()
    db.refresh(item_model)
    
    return item_model

def read_item(db: Session, id: int):
    return db.query(models.Item).filter(models.Item.id == id).first()

def update_item(db: Session, id: int, item: schema.Item):
    item_to_update = db.query(models.Item).filter(models.Item.id == id).first()

    if item_to_update:
        for key, value in item.dict().items():
            setattr(item_to_update, key, value)
        db.commit()
        db.refresh(item_to_update)

    return item_to_update

def delete_item(db: Session, id: int):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    db.delete(item)
    db.commit()

    return {"message": "Item deleted success"}

def error_message(message):
    return {"error": message}

# 확인용
def get_item(db: Session):
    return db.query(models.Item).all()