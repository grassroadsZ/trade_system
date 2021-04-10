
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