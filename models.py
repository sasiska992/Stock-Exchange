from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DB_NAME, DB_HOST, DB_PASS, DB_USER
# Создаем экземпляр FastAPI
app = FastAPI()

# Настройки базы данных
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# Создаем движок базы данных
engine = create_engine(DATABASE_URL)

# Создаем базовый класс для моделей
Base = declarative_base()

# Определяем модель таблицы


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer)


# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
