from models import db

# Создаем таблицы в базе данных, если они еще не существуют
def init_db():
    if not database_exists(engine.url):
        Base.metadata.create_all(bind=engine)

