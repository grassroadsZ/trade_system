# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 20:02
# @Author  : grassroadsZ
# @File    : strategy_function.py

# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 11:12
# @Author  : grassroadsZ
# @File    : strategy_function.py

from loguru import logger

from handle_mongo_db import TradeMongoDBTools
from settings import MONGO_DB
from trade_exchanges.binance_exchange import exchange

logger.add("file_{time}_log.txt", format="{time} {level} {message}", enqueue=True, level="DEBUG")

mongo_obj = TradeMongoDBTools(**MONGO_DB)


@logger.catch
def un_limit_sport(symbol, kwargs):
    buy_price = kwargs.get("next_buy_price")  # 当前网格买入价格
    sell_price = kwargs.get("grid_sell_price")  # 当前网格卖出价格
    current_num = kwargs.get("current_num")  # 当前连续买入次数
    max_count = kwargs.get("max_no_sell_count")  # 连续买入而不卖出的最大次数
    buy_with_no_sell_count_ratio = kwargs.get("buy_with_no_sell_count_ratio")  # 连续买入/最大买入而不卖出的比例

    step = kwargs.get("step")  # 当前步数

    def get_quantity(kwargs: dict):
        quantity = kwargs.get("quantity") * 2  # 买入数量
        # 如果当前次数/最大次数大于设置的比例时，取最小的交易量,当前买入次数为0 时也买最少
        if float(current_num / max_count) > (buy_with_no_sell_count_ratio / 10):
            logger.info("当前交易对:" + symbol + "连续买入次数已达" + str(current_num) + "次,调整为最低购买量" + str(
                quantity))
            quantity = round(quantity / 2, kwargs.get("min_num"))
        if step < 2:
            quantity = round(quantity / 2, kwargs.get("min_num"))

        return quantity

    def update_data(kwargs, deal_price, step, current_num):
        kwargs["next_buy_price"] = round(deal_price * (1 - kwargs["double_throw_ratio"] / 100),
                                         kwargs["min_num"])
        kwargs["grid_sell_price"] = round(deal_price * (1 + kwargs["profit_ratio"] / 100),
                                          kwargs["min_num"])
        kwargs["step"] += step
        kwargs["current_num"] += current_num
        kwargs["current_num"] = max([0, kwargs["current_num"]])
        logger.info(f'更新买入价格为：{kwargs["next_buy_price"]},卖出价格为:{kwargs["grid_sell_price"]},当前买入次数:{kwargs["step"]}')
        return kwargs

    try:

        cur_market_price = float(
            exchange.public_get_ticker_price(params={"symbol": symbol.replace("/", "")})["price"])  # 当前交易对市价

        logger.info(
            f"{symbol}当前现价:{cur_market_price} ,期望买入价格{buy_price},期望卖出价格{sell_price}, 当前买入次数{kwargs.get('step')},当前连续买入而不卖出次数{kwargs.get('current_num')}")
        quantity = get_quantity(kwargs)
        # 设置的买入价 > 当前现货价格
        if buy_price >= cur_market_price:
            if current_num == max_count:
                logger.info(f"当前连续买入次数以达 设定值{max_count},当前币种取消买入")
                return

            logger.info(f"创建 价格为 {buy_price} 的限价买单")

            res = exchange.create_limit_buy_order(symbol, quantity, buy_price)

            if res["info"]["orderId"]:  # 挂单成功
                mongo_obj.trade_record(
                    {"response": res['info'], "user_strategy": kwargs.get("user_strategy"), "coin_type": symbol})
                # 修改买入卖出价格、当前步数
                data = update_data(kwargs, buy_price, 1, 1)
                mongo_obj.update_coin_trade_param(coin_type=symbol, user_strategy_name=kwargs.get("user_strategy"),
                                                  param=data)

        elif sell_price < cur_market_price:  # 是否满足卖出价
            if step == 0:  # setp=0 防止踏空，跟随价格上涨
                data = update_data(kwargs, sell_price, step, 0)
                mongo_obj.update_coin_trade_param(coin_type=symbol, user_strategy_name=kwargs.get("user_strategy"),
                                                  param=data)

            else:
                logger.info(f"创建价格为 {sell_price} 的限价卖单")
                res = exchange.create_limit_sell_order(symbol, quantity, sell_price)
                # res = exchange.create_limit_sell_order()
                if res["info"]["orderId"]:
                    mongo_obj.trade_record(
                        {"response": res['info'], "user_strategy": kwargs.get("user_strategy"), "coin_type": symbol})
                # 修改买入卖出价格、当前步数
                data = update_data(kwargs, sell_price, -1, -1)
                mongo_obj.update_coin_trade_param(coin_type=symbol, user_strategy_name=kwargs.get("user_strategy"),
                                                  param=data)

    except Exception as e:
        logger.info(f"{symbol}币种运行失败,原因是：{e}")
