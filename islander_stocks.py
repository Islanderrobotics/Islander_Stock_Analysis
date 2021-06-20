
import pandas as pd

class Islander_stocks:
	'''the purpose of this class is to allow the user to see all of the current stocks
	that are less then or equal to there maximum amount entered'''

	def __init__(self):
		self.data = {}
		self.key = []
	def getting_the_data(self):
		stock = pd.read_csv("nasdaq.csv")
		self.data["stock"] = stock.iloc[:,0]
		self.key.append("stock")

