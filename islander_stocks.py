import os
import queue
import threading
from price import Price,StockDoesNotExistError
from getting_the_data import GettingTheData
from islanderqueue import IslanderQueue
class Islander_stocks:
	'''the purpose of this class is to allow the user to see all of the current stocks
	that are less then or equal to there maximum amount entered'''

	def __init__(self):
		self.data = {}
		self.key = []
	def getting_the_data(self):
		choices = ["NASDAQ", "NYSE","AMEX"]
		print("hello user please choice one of the markets mentioned below")
		while True:
			user = input(f"please enter {choices[0]} to view that market\n"
				f"please enter {choices[1]} to view that market\n"
				f"please enter {choices[2]} to view that market\n")
			if (user.upper() in  choices):
				break
			else:
				print("please chose from the following")

		stock = GettingTheData(chosen_market = user.upper())
		self.data["stock"] = stock.download()
		self.key.append("stock")

	def PriceOfStock(self):

		self.data["price"] = []
		self.data["symbols"] = []
		self.data["percentage"] = []
		self.data["overall_percentage"] = []
		self.key.append("price")
		self.key.append("symbols")
		self.key.append("percentage")
		self.key.append("overall_percentage")
		next = False
		while (True):
			try:
				maximum = int(input("what is the maximum price you would like to spend"))
				break
			except ValueError:
				print("Please make a choice")
		thread = {}
		for i in range(0,len(self.data[self.key[0]])//os.cpu_count(), os.cpu_count()):
			for j in range(os.cpu_count()):

				index = self.data[self.key[0]][i+j]
				thread[str(j)] = threading.Thread(target=self.speedy, args=(index,maximum,))
			for w in range(os.cpu_count()):
				thread[str(w)].start()
			for l in range(os.cpu_count()):
				thread[str(l)].join()

	def speedy(self, index,maximum):

		try:

			data = Price(symbol=index,maximum = maximum)
			data.driver()

			if (data.current_price <= maximum and data.current_price > 0 and data.current_percentage > 0 or maximum ==0):
				self.data[self.key[1]].append(data.current_price)
				self.data[self.key[2]].append(index)
				self.data[self.key[3]].append(data.current_percentage)
				self.data[self.key[4]].append(data.total_percentage)
				print(f"${data.current_price},{100 * data.current_percentage}%,{index}")
		except StockDoesNotExistError:
			pass
	def top(self,key ="price"):
		self.queue = IslanderQueue(priority= True)
		for i in range(len(self.data["symbols"])):
			temp = {}
			for j in range(1,len(self.key)):
				temp[self.key[j]] = self.data[self.key[j]][i]
			self.queue.Push(data=temp,key=key)
			del temp
		self.queue.Heapify(key = key)

	def GetTop(self,topValue = None):
		self.data["sorted"] = IslanderQueue()
		self.key.append("sorted")

		while (True):
			try:
			# print(self.queue.root.data)
				self.data["sorted"].Push(data = self.queue.root.data)
				self.queue.RemoveMax(key = "price")
			except AttributeError:
				break
		temp = self.data["sorted"].head
		while (self.data["sorted"].head is not None):
			print(self.data["sorted"].head.data)
			if (topValue is not None):
				topValue-=1
				if (topValue==0):
					break
			self.data["sorted"].head = self.data["sorted"].head.next
		self.queue.head = temp