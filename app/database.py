# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://username:password@db:5432/nudges"

# 비동기 엔진을 생성합니다.
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 비동기 세션을 생성합니다.
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()