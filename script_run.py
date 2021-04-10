# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 20:04
# @Author  : grassroadsZ
# @File    : run.py
import time

import strategy_function

import concurrent.futures

executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)


def run():
    all_obj_list = []
    for info in strategy_function.mongo_obj.get_trade_info():
        one_obj = {"func": getattr(strategy_function, info[1]), "symbol": info[0], "kwargs": info[2]}
        all_obj_list.append(one_obj)

    worker = 1 if len(all_obj_list) < 3 else 2
    with concurrent.futures.ThreadPoolExecutor(max_workers=worker) as executor:

        # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Start the load operations and mark each future with its URL
        future_to_task = {executor.submit(one_obj["func"], symbol=one_obj["symbol"], kwargs=one_obj["kwargs"]): one_obj for one_obj in all_obj_list}
        for future in concurrent.futures.as_completed(future_to_task):
            task = future_to_task[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception' % (task["symbol"]))
        # else:
        #     print('%s is ok' % (task["symbol"]))


while True:
    run()
    time.sleep(3)
