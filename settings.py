import os
from dotenv import load_dotenv

load_dotenv()

POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')
ALPHA_API_KEY = os.getenv("ALPHA_API_KEY")
