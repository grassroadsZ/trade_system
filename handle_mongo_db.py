# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 19:38
# @Author  : grassroadsZ
# @File    : handle_mongo_db.py

import time
import pymongo


class TradeMongoDBTools:
    """
    使用 find_one() 方法来查询集合中的一条数据
    find() 方法可以查询集合中的所有数据，类似 SQL 中的 SELECT * 操作
    https://www.runoob.com/python3/python-mongodb-query-document.html
    """

    def __init__(self, host, user, pwd):
        self.client = pymongo.MongoClient(host=host, username=user, password=pwd)
        self.db = self.client["trade"]

    def get_strategy_param(self, strategy_name):
        param_list = []
        for i in self.db["base_strategy"].find({"name": strategy_name}):
            i.pop("_id")
            i.pop("name")
            param_list.append(i)
        return param_list[0]

    def set_coin_info(self, coin_type: str, user_strategy: str, is_use: bool, param: dict):
        """
        设置交易对信息到 trade_config
        :param coin_type: XRPUSDT
        :param user_strategy: 自定义网格(user_strategy中的name字段)
        :param param:  策略的key 对应的value
        :return:
        """
        self.db["trade_config"].insert_one({'coin_type': coin_type, 'user_strategy': user_strategy, "is_use": is_use,
                                            "param": param})

    def get_user_strategy_param_to_strategy_param(self, user_strategy_name):
        """通过用户策略找到基础策略的参数，好像不需要？"""
        return self.get_strategy_param(self.db["user_strategy"].find_one({"name": user_strategy_name})["base"])

    def update_coin_trade_param(self, coin_type, user_strategy_name, param={}):
        """
        修改trade_config 中的币种的参数信息
        :param coin_type:
        :param user_strategy_name:
        :param param:
        :return:
        """

        arg = {"user_strategy": user_strategy_name, "coin_type": coin_type}
        _: dict = self.db["trade_config"].find_one(arg)["param"]
        # 只更新自定义策略的参数
        for key in _:
            _[key] = param[key]
        # print(_)
        self.db["trade_config"].find_one_and_update(arg, update={"$set": {"param": _}})

    def get_trade_info(self):
        """
        获取需要交易的交易信息
        :return: symbol,func_name,param
        """
        # 查询所有交易信息
        trade_info_list = []
        for i in self.db['trade_config'].find({"is_use": True}):
            param = i["param"]
            param["user_strategy"] = i["user_strategy"]

            one_info = [i["coin_type"], i["param"]["base"], param]
            trade_info_list.append(one_info)
        return trade_info_list

    def trade_record(self, kwargs={}):
        data = {"date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
        data.update(kwargs)
        self.db["trade_record"].insert_one(data)

    def set_uniq_index(self):
        self.db["trade_config"].ensure_index({"coin_type": 1, "user_strategy": 1}, {"unique": True})
        self.db["user_strategy"].ensure_index({"coin_type": 1, "name": 1}, {"unique": True})


if __name__ == '__main__':
    from settings import MONGO_DB

    d = {"next_buy_price": 20.996, "grid_sell_price": 21, "step": 0,
         "profit_ratio": 1,
         "double_throw_ratio": 1,
         "quantity": 5,
         "max_no_sell_count": 10,
         "buy_with_no_sell_count_ratio": 1,
         "max_no_buy_count": 10,
         "max_no_buy_num": 0,
         "min_num": 5,
         "current_num": 0,
         "base": "un_limit_sport",
         "txt": "",
         'is_use': True,
         }
    print(TradeMongoDBTools(**MONGO_DB).set_coin_info("ATOMUSDT", "自定义网格", True, d))
