from sqlalchemy.orm import Session
from . import schema, models


def save_device_info(db: Session, info: schema.DeviceInfo):
    device_info_model = models.DeviceInfo(**info.dict())
    db.add(device_info_model)
    db.commit()
    db.refresh(device_info_model)
    return device_info_model

def get_device_info(db: Session, token: str = None):
    if token is None:
        return db.query(models.DeviceInfo).all()
    else:
        return db.query(models.DeviceInfo).filter(models.DeviceInfo.token == token).first()

def save_nudges_configuration(db: Session, config: schema.Configuration):
    config_model = models.Configuration(**config.dict())
    db.add(config_model)
    db.commit()
    db.refresh(config_model)
    return config_model

def get_nudges_configuration(db: Session):
    return db.query(models.Configuration).first()

def delete_nudges_configuration(db: Session):
    db.query(models.Configuration).delete()

def error_message(message):
    return {
        'error': message
    }

def save_nudges_item(db: Session, item: schema.Item):
    item_model = models.Item(**item.dict())
    db.add(item_model)
    db.commit()
    db.refresh(item_model)
    return item_model

#     device_info_model = models.DeviceInfo(**info.dict())
#     db.add(device_info_model)
#     db.commit()
#     db.refresh(device_info_model)

def delete_nudges_item(db: Session):
    db.query(models.Item).delete()

def get_item(db: Session):
    return db.query(models.Item).all()

def read_item(db: Session, id: int):
    return db.query(models.Item).filter(models.Item.id == id).first()

def update_item(db: Session, id: int, item: schema.Item):
    # 해당 id에 해당하는 Item 찾기
    item_to_update = db.query(models.Item).filter(models.Item.id == id).first()

    if item_to_update:
        # 새로운 데이터로 업데이트
        for key, value in item.dict().items():
            setattr(item_to_update, key, value)

        # 변경사항을 데이터베이스에 반영
        db.commit()
        db.refresh(item_to_update)

    return item_to_update

def delete_item(db: Session, id: int):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}