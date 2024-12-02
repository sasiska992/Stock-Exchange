from typing import Union
from settings import finhub_client
from utils.stocks import get_stock_info, get_dollar_to_rub_course
from fastapi import Request, APIRouter
from settings import POLYGON_API_KEY
from main import templates
from models import BuyingStock, db

stocks = APIRouter()


@stocks.get('/')
@stocks.get('/app')
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
def buy_stock(symbol: str, count: int):
    data = get_stock_info(symbol)
    buying = BuyingStock(data["current_price"], symbol, count)
    buying.add(db)
    return f"вы успешно купили {count} акций {symbol} по {buying.buying_price}"


@stocks.get("/my_stocks")
def my_stocks():
    print(get_stock_info("SBER"))
    rub_to_dollar = get_dollar_to_rub_course()
    data = db.query(BuyingStock).all()
    current_prices = {}
    buying_stocks = {
        # "symbol" :
        #        "buying" : [
        #           1:{
        #               count, buying_price, current_price, delta, total_delta
        #             }
        #           2:{
        #               count, buying_price, current_price, delta, total_delta
        #             }
        #        ]
    }
    for stock in data:
        current_prices[stock.symbol] = get_stock_info(stock.symbol)[
            "current_price"]
        if stock.symbol not in buying_stocks.keys():
            buying_stocks[stock.symbol] = {
                "buying": [
                    {
                        1: {
                            "count": stock.count,
                            "buying_price": stock.buying_price,
                            "current_price": current_prices[stock.symbol] * rub_to_dollar,
                            "delta": stock.buying_price - current_prices[stock.symbol],
                            "total_delta": stock.buying_price * stock.count - current_prices[stock.symbol] * stock.count,
                        }
                    }
                ]
            }
        else:
            stock_index = list(
                buying_stocks[stock.symbol]["buying"][-1].keys())[0] + 1
            buying_stocks[stock.symbol]["buying"].append({
                stock_index: {
                    "count": stock.count,
                    "buying_price": stock.buying_price,
                    "current_price": current_prices[stock.symbol] * rub_to_dollar,
                    "delta": stock.buying_price * stock.count - current_prices[stock.symbol] * stock.count,
                    "total_delta": stock.buying_price * stock.count - current_prices[stock.symbol] * stock.count,
                }
            }
            )

    return buying_stocks
