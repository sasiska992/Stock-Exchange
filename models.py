from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Double
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
class Func(Base):
    __abstract__ = True  # Указываем, что этот класс является абстрактным

    def add(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()


class Test(Func):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer)


class BuyingStock(Func):
    __tablename__ = 'buying stock'

    id = Column(Integer, primary_key=True, index=True)
    buying_price = Column(Double)
    symbol = Column(String)
    count = Column(Integer)

    def __init__(self, buying_price: int, symbol: str, count: int):
        self.symbol = symbol
        self.buying_price = buying_price
        self.count = count


# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()
