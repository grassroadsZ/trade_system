# import asyncio
from pprint import pprint

# import ccxt.async_support as ccxt  # noqa: E402
import random

import ccxt

exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
    'enableRateLimit': True
})


# async def run():
#     price = await exchange.public_get_ticker_price(params={"symbol":"BTCUSDT"})
#     await exchange.close()
#     return price





def create_limit_buy_orde(symbol):
    # res=object
    # res = None
    res = random.choice(
        [{"symbol": symbol, "orderId": 1926131052, "orderListId": -1, "clientOrderId": "fozBl3EwAfhVHSZoi7uMWu",
          "transactTime": 1616510784635, "price": 0.56971, "origQty": 25, "executedQty": 25,
          "cummulativeQuoteQty": 14.2435,
          "status": "FILLED", "timeInForce": "FOK", "type": "LIMIT", "side": "SELL", "fills": [
                {"price": "0.56974000", "qty": "25.00000000", "commission": "0.01424350", "commissionAsset": "USDT",
                 "tradeId": 165902158}], "mTradeId": "mTradId-8a7cb660-8be6-11eb-ad8a-65a36cd0112c",
          "stockId": "stockId-41332500-8be3-11eb-ad8a-65a36cd0112c",
          "sellStock": {"price": 0.56508, "qty": 25, "commission": 0.025, "commissionAsset": "XRP",
                        "tradeId": 165890548,
                        "stockId": "stockId-41332500-8be3-11eb-ad8a-65a36cd0112c", "createTime": 1616509373264,
                        "symbol": "XRPUSDT", "_id": "Fpx5pVmpMAjXvILC"}, "_id": "u2w8k31Dq4W2bASP"},
         {"symbol": symbol, "orderId": 1925468964, "orderListId": -1, "clientOrderId": "s4X2JiGwR88D66QoJZHnBw",
          "transactTime": 1616502582858, "price": 0.57653, "origQty": 25, "executedQty": 25,
          "cummulativeQuoteQty": 14.41225,
          "status": "FILLED", "timeInForce": "FOK", "type": "LIMIT", "side": "BUY", "fills": [
             {"price": 0.57649, "qty": 25, "commission": 0.025, "commissionAsset": "XRP", "tradeId": 165840946,
              "stockId": "stockId-71d6b970-8bd3-11eb-91ac-63b3ccfb56aa", "createTime": 1616502582919,
              "symbol": "XRPUSDT"}],
          "mTradeId": "mTradId-71d6e080-8bd3-11eb-91ac-63b3ccfb56aa",
          "stockId": "stockId-71d6b970-8bd3-11eb-91ac-63b3ccfb56aa", "_id": "wH0SqW58XG29Im36"}])
    # res.resp = resp
    res["status_code"] = 200
    return res


def create_limit_sell_orde(symbol):
    res = random.choice(
        [{"symbol": "XRPUSDT", "orderId": 1926131052, "orderListId": -1, "clientOrderId": "fozBl3EwAfhVHSZoi7uMWu",
          "transactTime": 1616510784635, "price": 0.56971, "origQty": 25, "executedQty": 25,
          "cummulativeQuoteQty": 14.2435,
          "status": "FILLED", "timeInForce": "FOK", "type": "LIMIT", "side": "SELL", "fills": [
                {"price": "0.56974000", "qty": "25.00000000", "commission": "0.01424350", "commissionAsset": "USDT",
                 "tradeId": 165902158}], "mTradeId": "mTradId-8a7cb660-8be6-11eb-ad8a-65a36cd0112c",
          "stockId": "stockId-41332500-8be3-11eb-ad8a-65a36cd0112c",
          "sellStock": {"price": 0.56508, "qty": 25, "commission": 0.025, "commissionAsset": "XRP",
                        "tradeId": 165890548,
                        "stockId": "stockId-41332500-8be3-11eb-ad8a-65a36cd0112c", "createTime": 1616509373264,
                        "symbol": "XRPUSDT", "_id": "Fpx5pVmpMAjXvILC"}, "_id": "u2w8k31Dq4W2bASP"},
         {"symbol": "XRPUSDT", "orderId": 1925468964, "orderListId": -1, "clientOrderId": "s4X2JiGwR88D66QoJZHnBw",
          "transactTime": 1616502582858, "price": 0.57653, "origQty": 25, "executedQty": 25,
          "cummulativeQuoteQty": 14.41225,
          "status": "FILLED", "timeInForce": "FOK", "type": "LIMIT", "side": "BUY", "fills": [
             {"price": 0.57649, "qty": 25, "commission": 0.025, "commissionAsset": "XRP", "tradeId": 165840946,
              "stockId": "stockId-71d6b970-8bd3-11eb-91ac-63b3ccfb56aa", "createTime": 1616502582919,
              "symbol": "XRPUSDT"}],
          "mTradeId": "mTradId-71d6e080-8bd3-11eb-91ac-63b3ccfb56aa",
          "stockId": "stockId-71d6b970-8bd3-11eb-91ac-63b3ccfb56aa", "_id": "wH0SqW58XG29Im36"}])
    # res.resp = resp
    res["status_code"] = 200
    return res


import types

# exchange.public_get_ticker_price = types.MethodType(public_get_ticker_price, exchange)
exchange.create_limit_buy_order = types.MethodType(create_limit_buy_orde, exchange)
exchange.create_limit_sell_order = types.MethodType(create_limit_sell_orde, exchange)

print(exchange.public_get_ticker_price(params={"symbol":"ATOMUSDT"}))
# print(exchange.create_limit_buy_order())
# print(exchange.create_limit_sell_order())
if __name__ == '__main__':
    pass
    # print(asyncio.run(run()))
    # print(asyncio.get_event_loop().run_until_complete(run()))
# print(price)
