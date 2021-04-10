# 介绍
script_run.py 交易代码运行入口
set_coin_info.py 交易对的添加与停止(暂时先不支持单个币对的参数修改)

1. 设置自定义策略参数值
2. 根据自定义策略 + 币种

## 逻辑

- 设置自定义策略参数值
    
    获取 base_strategy 中的所有策略 [{"策略1":param_dict},{"策略2":param_dict}]
    
    用户根据选择策略,然后设置策略所需要的参数保存为唯一的自定义策略
    
    保存数据: 自定义策略名称,base(base_strategy中的name),设置的参数值
    
- 自定义策略 + 币种
    
    保存数据: 币种 + 自定义策略名 + 自定义策略名



1. 查询db中trade_config中is_use = True 的交易信息

    1.1 交易信息 coin_type  + user_strategy + base + coin_type_param
    
    - coin_type : 交易币对
    - user_strategy : 与 user_strategy 中的name 相等
    - base : 与 base_strategy 中的 name 相等
    





# MongoDB 初始化脚本

初始策略表
```mongojs
db.getCollection("base_strategy").insert( {
    "next_buy_price": NumberInt("0"),
    "grid_sell_price": NumberInt("0"),
    "step": NumberInt("0"),
    "profit_ratio": NumberInt("0"),
    "double_throw_ratio": NumberInt("0"),
    "quantity": NumberInt("0"),
    "max_no_sell_count": NumberInt("0"),
    "buy_with_no_sell_count_ratio": NumberInt("1"),
    "max_no_buy_count": NumberInt("0"),
    "max_no_buy_num": NumberInt("0"),
    "min_num": NumberInt("5"),
    "current_num": NumberInt("0"),
    "name": "un_limit_sport"
} );

```
用户策略表
```mongojs
db.getCollection("user_strategy").insert( {
    "next_buy_price": NumberInt("0"),
    "grid_sell_price": NumberInt("0"),
    "step": NumberInt("0"),
    "profit_ratio": NumberInt("0"),
    "double_throw_ratio": NumberInt("0"),
    "coin_type": "BTCUSDT",
    "quantity": NumberInt("0"),
    "max_no_sell_count": NumberInt("0"),
    "buy_with_no_sell_count_ratio": NumberInt("1"),
    "max_no_buy_count": NumberInt("0"),
    "max_no_buy_num": NumberInt("0"),
    "min_num": NumberInt("5"),
    "current_num": NumberInt("0"),
    "base": "un_limit_sport",
    "name": "自定义网格",
    "txt": "这是用于描述"
} );
```