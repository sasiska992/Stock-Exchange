from datetime import datetime, timedelta
from polygon import RESTClient
from settings import POLYGON_API_KEY

client = RESTClient(api_key=POLYGON_API_KEY)

# Получаем сегодняшнюю дату
today = datetime.now()

# Получаем дату вчера
yesterday = today - timedelta(days=1)

# Форматируем даты в строковом формате
from_date = yesterday.strftime("%Y-%m-%d")
to_date = today.strftime("%Y-%m-%d")

# Теперь используем эти даты в вашем коде
ticker = "AAPL"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker,
                          multiplier=1,
                          timespan="minute",
                          from_=from_date,
                          to=to_date,
                          limit=50000):
    aggs.append(a)

print(aggs)

# Get Last Trade
trade = client.get_last_trade(ticker=ticker)
print(trade)
