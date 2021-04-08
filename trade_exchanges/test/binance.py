
import asyncio
from pprint import pprint

import ccxt.async_support as ccxt  # noqa: E402

exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
    'enableRateLimit': True
})
async def run():
    price = await exchange.public_get_ticker_price(params={"symbol":"BTCUSDT"})
    await exchange.close()
    return price
if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(run())
# print(price)