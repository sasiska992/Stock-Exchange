from typing import Union

import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from settings import POLYGON_API_KEY

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={
            "name": "Vlad"
        },
        request=request)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id,
            "q": q}


@app.get("/prices")
def get_prices():
    url = (
        f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey={POLYGON_API_KEY}"
    )
    r = requests.get(url)
    data = r.json()
    return data
