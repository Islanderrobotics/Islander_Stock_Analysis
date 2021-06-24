
import pandas as pd
from getting_the_data import GettingTheData
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
		stock.download()
		self.data["stock"] = stock.symbols()
		self.key.append("stock")
		stock.delete()


