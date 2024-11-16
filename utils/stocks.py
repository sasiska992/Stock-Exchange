from settings import finhub_client


def get_stock_info(symbol: str) -> dict:
    data = finhub_client.quote(symbol)
    return {
        "current_price": data["c"],
        "high_price": data['h'],
        "low_price": data['l'],
        "open_price": data['o'],
        "previous_close": data['pc']
    }
