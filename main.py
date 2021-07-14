from islander_stocks import Islander_stocks

data = Islander_stocks()
data.getting_the_data()
data.PriceOfStock()
data.top()
bob = data.queue.head
while (data.queue.head is not None):
    print(data.queue.head.data)
    data.queue.head = data.queue.head.next
