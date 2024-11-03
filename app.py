from typing import Union

import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from settings import POLYGON_API_KEY

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


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
def get_prices(request: Request):
    time = 15
    url = (
        f"https://www.alphavantage.co/query?"
        f"function=TIME_SERIES_INTRADAY&"
        f"symbol=AAPL&"
        f"interval={time}min&"
        f"month=2024-11&"
        f"outputsize=compact&"
        f"apikey={POLYGON_API_KEY}"
    )
    r = requests.get(url)
    data = r.json()
    print(data)
    return templates.TemplateResponse(
        name="prices.html",
        context={
            "data": data
        },
        request=request
    )

    # return data


@app.get("/test")
def test(request: Request):
    return templates.TemplateResponse(
        name="test_template/index.html",
        request=request,
    )
