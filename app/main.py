from fastapi import FastAPI, Depends, HTTPException
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from .schema import DeviceInfo, Configuration, Item
from . import crud, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post('/device/info')
def save_device_info(info: DeviceInfo, db=Depends(db)):
    object_in_db = crud.get_device_info(db, info.token)
    if object_in_db:
        raise HTTPException(400, detail= crud.error_message('This device info already exists'))
    return crud.save_device_info(db,info)

@app.get('/device/info/{token}')
def get_device_info(token: str, db=Depends(db)):
    info = crud.get_device_info(db,token)
    if info:
        return info
    else:
        raise HTTPException(404, crud.error_message('No device found for token {}'.format(token)))

@app.get('/device/info')
def get_all_device_info(db=Depends(db)):
    return crud.get_device_info(db)

@app.post('/configuration')
def save_configuration(config: Configuration, db=Depends(db)):
    # always maintain one config
    crud.delete_nudges_configuration(db)
    return crud.save_nudges_configuration(db, config)

@app.get('/configuration')
def get_configuration(db=Depends(db)):
    config = crud.get_nudges_configuration(db)
    if config:
        return config
    else:
        raise HTTPException(404, crud.error_message('No configuration set'))

@app.post('/create')
def create_item(item: Item, db=Depends(db)):
    # always maintain one config
    # crud.delete_nudges_item(db)
    return crud.save_nudges_item(db, item)

# def save_device_info(info: DeviceInfo, db=Depends(db)):
#     object_in_db = crud.get_device_info(db, info.token)
#     if object_in_db:
#         raise HTTPException(400, detail= crud.error_message('This device info already exists'))
#     return crud.save_device_info(db,info)

@app.get('/item/all')
def get_all_item(db=Depends(db)):
    return crud.get_item(db)

@app.get('/read/{id}')
def get_read_item(id: int, db=Depends(db)):
    info = crud.read_item(db, id)
    if info:
        return info
    else:
        raise HTTPException(404, crud.error_message('No item found for id {}'.format(id)))

@app.put('/update/{id}')
def put_update_item(item: Item, id: int, db=Depends(db)):
    info = crud.update_item(db, id, item)
    if info:
        return info
    else:
        raise HTTPException(404, crud.error_message('No item found for id {}'.format(id)))

@app.delete("/delete/{id}")
def delete_item(id: int, db=Depends(db)):
    item = crud.read_item(db, id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    crud.delete_item(db, id)
    return {"message": "Item deleted successfully"}

# 조건 다시 보면서 추가할거살펴보기
# 비동기 기능 추가