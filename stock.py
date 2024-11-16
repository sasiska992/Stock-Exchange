from typing import Union
from settings import finhub_client
from utils.stocks import get_stock_info
from fastapi import Request, APIRouter
from settings import POLYGON_API_KEY
from main import templates
from models import BuyingStock, db

stocks = APIRouter()


@stocks.get('/')
def index(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={
            "name": "Vlad"
        },
        request=request)


@stocks.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id,
            "q": q}


@stocks.get("/prices")
def get_prices(request: Request):
    # c: Текущая цена (current price).
    # h: Высшая цена за день (high price of the day).
    # l: Низшая цена за день (low price of the day).
    # o: Цена открытия (open price).
    # pc: Цена закрытия предыдущего дня (previous close price).
    # t: Время последнего обновления (timestamp).

    data = get_stock_info("AAPL")

    # return templates.TemplateResponse(
    #     name="prices.html",
    #     context={
    #         "data": data
    #     },
    #     request=request
    # )

    return data


@stocks.post("/buy_stock")
def buy_stock(symbol: str):
    data = get_stock_info(symbol)
    buying = BuyingStock(data["current_price"], symbol)
    db.add(buying)
    db.commit()
    return f"вы успешно купили акции {symbol} по {buying.buying_price}"


@stocks.get("/my_stocks")
def my_stocks():
    data = db.query(BuyingStock).all()
    current_prices = {}
    buying_stocks = {}
    for stock in data:
        current_prices[stock.symbol] = get_stock_info(stock.symbol)


    return buying_stocks 
