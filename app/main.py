from fastapi import FastAPI, Depends, HTTPException
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from .schema import Item
from . import crud, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# "Create": 새로운 엔트리를 추가하는 함수 (POST 메서드)
@app.post('/create')
def post_create_item(item: Item, db=Depends(db)):
    return crud.create_item(db, item)

# "Read": 주어진 키에 해당하는 엔트리를 반환하는 함수 (GET 메서드)
@app.get('/read/{id}')
def get_read_item(id: int, db=Depends(db)):
    read_item = crud.read_item(db, id)
    if read_item:
        return read_item
    else:
        raise HTTPException(404, crud.error_message('No item : id {}'.format(id)))

# "Update": 주어진 키에 해당하는 엔트리를 업데이트하는 함수 (PUT 메서드)
@app.put('/update/{id}')
def put_update_item(item: Item, id: int, db=Depends(db)):
    update_item = crud.update_item(db, id, item)
    if update_item:
        return update_item
    else:
        raise HTTPException(404, crud.error_message('No item : id {}'.format(id)))

# "Delete": 주어진 키에 해당하는 엔트리를 삭제하는 함수 (DELETE 메서드)
@app.delete("/delete/{id}")
def delete_item(id: int, db=Depends(db)):
    read_item = crud.read_item(db, id)
    if read_item is None:
        raise HTTPException(404, crud.error_message('No item : id {}'.format(id)))
    else:
        return crud.delete_item(db, id)

# 지워야하는 부분 - test 확인용
@app.get('/item/all')
def get_all_item(db=Depends(db)):
    return crud.get_item(db)
    
# 조건 다시 보면서 추가할거살펴보기
# 비동기 기능 추가