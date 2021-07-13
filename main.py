from islander_stocks import Islander_stocks

data = Islander_stocks()
data.getting_the_data()
data.PriceOfStock()
data.top()
# bob = data.islander_stocks.queue.head
# while (data.islander_stocks.queue.head is not None):
#     print(data.islander_stocks.queue.head.data)
#     data.islander_stocks.queue.head = data.islander_stocks.queue.head.next
#     data.islander_stocks.queue.head = bob