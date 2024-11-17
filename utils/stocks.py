import requests

from settings import finhub_client, EXCHANGERATE_API_KEY


def get_stock_info(symbol: str) -> dict:
    data = finhub_client.quote(symbol)
    return {
        "current_price": data["c"],
        "high_price": data['h'],
        "low_price": data['l'],
        "open_price": data['o'],
        "previous_close": data['pc']
    }


def get_dollar_to_rub_course() -> float:
    url = f' https://v6.exchangerate-api.com/v6/{EXCHANGERATE_API_KEY}/latest/USD'  # Пример для получения курса USD к другим валютам

    response = requests.get(url)
    data = response.json()
    # Получаем курс рубля
    rub_rate = data['conversion_rates']['RUB']

    return rub_rate
