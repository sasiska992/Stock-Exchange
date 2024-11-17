import requests
from settings import TINKOFF_API_KEY
from datetime import timedelta

from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now


def main():
    with Client(TINKOFF_API_KEY) as client:
        orderbook = client.market.orderbook_get(figi='BBG004730N88')
        print(orderbook)

    return 0


if __name__ == "__main__":
    main()
