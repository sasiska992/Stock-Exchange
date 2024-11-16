from models import engine, Base
from sqlalchemy_utils import database_exists
import uvicorn

# Создаем таблицы в базе данных, если они еще не существуют


def init_db():
    if not database_exists(engine.url):
        Base.metadata.create_all(bind=engine)


def main():
    init_db()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
