from environs import Env

import finnhub

env = Env()
env.read_env(path=".env")

POLYGON_API_KEY = env.str('POLYGON_API_KEY')
ALPHA_API_KEY = env.str("ALPHA_API_KEY")
FINHUB_API_KEY = env.str("FINHUB_API_KEY")
finhub_client = finnhub.Client(FINHUB_API_KEY)
EXCHANGERATE_API_KEY = env.str("EXCHANGERATE_API_KEY")
TINKOFF_API_KEY = env.str("TINKOFF_API_KEY")
DB_HOST = env.str("DB_HOST")
DB_NAME = env.str("DB_NAME")
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")

env.read_env(path='.flaskenv')  # или env.read_env(path='.env')
# Получаем переменные окружения
FLASK_DEBUG = env.bool("FLASK_DEBUG")
print(FLASK_DEBUG)
