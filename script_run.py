# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 20:04
# @Author  : grassroadsZ
# @File    : run.py
import strategy_function

for info in strategy_function.mongo_obj.get_trade_info():
    getattr(strategy_function, info[1])(symbol=info[0], kwargs=info[2])
