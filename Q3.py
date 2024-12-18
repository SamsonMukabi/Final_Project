def buy_and_sell(stock_price):
    max_profit_val, current_max_val = 0, 0

    for price in reversed(stock_price):
        current_max_val = max(current_max_val, price)
        potential_profit = current_max_val - price
        max_profit_val = max(potential_profit, max_profit_val)

    return max_profit_val

f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
f.close()

stock_prices = [float(price) for price in listItems]

max_profit = buy_and_sell(stock_prices)

print("The largest possible profit is:", round(max_profit, 2))
