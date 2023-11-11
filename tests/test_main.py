# test_main.py

import json
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

import sys
import os

# 현재 스크립트 파일의 경로를 얻어옴
current_dir = os.path.dirname(os.path.abspath(__file__))
# 프로젝트 루트 디렉토리를 계산
project_root = os.path.abspath(os.path.join(current_dir, ".."))
# sys.path에 프로젝트 루트 디렉토리를 추가
sys.path.insert(0, project_root)

from app.main import app, init
from app.crud import create_item, read_item, update_item, delete_item, get_item
from app.schema import Item

@pytest.fixture(scope="module")
def test_db():
    db = AsyncSession()
    yield db
    db.close()

@pytest.fixture(autouse=True, scope="module")
async def initialize_test_db(test_db):
    await init()

def test_create_item_with_testclient(test_db):
    item_data = {
        "created": "2023-11-10T12:34:56",
        "name": "async test 1",
        "content": "MTIzNDU="
    }

    # TestClient를 사용하여 /create 엔드포인트에 POST 요청 보내기
    with TestClient(app) as client:
        response = client.post("/create", json=item_data)

    # 응답 상태코드가 200인지 확인
    assert response.status_code == 200

    # 응답 결과를 JSON으로 디코딩하여 생성된 아이템 확인
    created_item = response.json()
    assert created_item["created"] == item_data["created"]
    assert created_item["name"] == item_data["name"]
    assert created_item["content"] == item_data["content"]
