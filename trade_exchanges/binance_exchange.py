import ccxt

from settings import API_KEY, API_SECRET

exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True,
    "verbose":True,
})
# print(exchange.options)

print(exchange.public_get_ticker_price(params={"symbol":"BTCUSDT"}))