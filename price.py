import requests
from bs4 import BeautifulSoup as bs

class StockDoesNotExistError(Exception):
    pass

class NetworkError(Exception):
    pass

class Price:
    '''this class is going to web scrap yahoo finance to get the price
    as well as the current percentage'''
    def __init__(self,symbol):
        try:
            network = requests.get(f"https://finance.yahoo.com/quote/{symbol}/history")
        except:
            raise NetworkError()
        if network.status_code == 302:
            raise StockDoesNotExistError(symbol)
        self.soup = bs(network.content, 'html5lib')
        self.symbol = symbol
    def Price(self):
        '''the purpose of this method is to get the current price'''
        try:
            price = self.soup.find('span', attrs={"data-reactid":"50"}).text
            self.current_price = float(price.split(" ")[0]
                                       .replace(",","")
                                       .replace("(","")
                                       .replace(")","")
                                       .replace("%",""))
        except AttributeError as error:
            raise StockDoesNotExistError(self.symbol) from error
    def percentage(self):
        '''this method will allow the user to view the current stock percentage'''
        try:
            percentage = self.soup.find('span', attrs={"data-reactid":"51"}).text
            self.current_percentage = float(percentage.split(" ")[0]
                                            .replace(",", "")
                                            .replace("(", "")
                                            .replace(")", "")
                                            .replace("%", "")
                                            )
            self.total_percentage = float(percentage.split(" ")[1]
                                          .replace(",", "")
                                          .replace("(", "")
                                          .replace(")", "")
                                          .replace("%", "")
                                          )
        except AttributeError as error:
            raise StockDoesNotExistError(self.symbol) from error
    def driver(self):
        '''this will make it so the class can be automated'''
        self.Price()
        self.percentage()
