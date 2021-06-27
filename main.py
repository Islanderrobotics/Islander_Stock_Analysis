from islander_stocks import Islander_stocks

data = Islander_stocks()
data.getting_the_data()
data.PriceOfStock()
print(data.data[data.key[0]])