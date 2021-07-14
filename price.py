

import requests
from bs4 import BeautifulSoup as bs

class StockDoesNotExistError(Exception):
    pass

class NetworkError(Exception):
    pass

class Price:
    '''this class is going to web scrap yahoo finance to get the price
    as well as the current percentage'''
    def __init__(self,symbol,maximum):
        try:
            headers={'User-Agent':'Mozilla/5.0'}

            network = requests.get(f"https://finance.yahoo.com/quote/{symbol}/history",headers=headers)
        except:
            raise NetworkError()
        if network.status_code == 302 or network.status_code == 404:
            raise StockDoesNotExistError(symbol)

        self.soup = bs(network.content, "html.parser")
        if self.soup.find("span",attrs={"data-reactid":"32"}) is not None:
            if self.soup.find("span",attrs={"data-reactid":"32"}).text == f"No results for '{symbol.lower()}'":
                raise StockDoesNotExistError(symbol)
        if self.soup.find("span", attrs={"data-reactid": "6"}) is not None:
            if self.soup.find("span", attrs={"data-reactid": "6"}).text == f"Symbols similar to '{symbol.lower()}'":
                raise StockDoesNotExistError(symbol)
        self.symbol = symbol
        # print(symbol)
        self.maximum = maximum
        self.general = self.soup.find('div', attrs={"data-reactid": "48"})
    def Price(self):
        '''the purpose of this method is to get the current price'''
        try:
            price = self.general.find('span', attrs={"data-reactid":"49"}).text
            self.current_price = float(price.split(" ")[0].replace(",","").replace("(","")
                                       .replace(")","")
                                       .replace("%",""))
            return
        except AttributeError as error:
            raise StockDoesNotExistError(self.symbol) from error
        try:
            price = self.general.find('span', attrs={"data-reactid":"46"}).text
            self.current_price = float(price.split(" ")[0]
                                       .replace(",","")
                                       .replace("(","")
                                       .replace(")","")
                                       .replace("%",""))
            return
        except AttributeError as error:
            raise StockDoesNotExistError(self.symbol) from error
        try:
            price = self.general.find('span', attrs={"data-reactid":"46.69"}).text
            self.current_price = float(price.split(" ")[0]
                                       .replace(",","")
                                       .replace("(","")
                                       .replace(")","")
                                       .replace("%",""))
            return
        except AttributeError as error:
            raise StockDoesNotExistError(self.symbol) from error
    def percentage(self):
        '''this method will allow the user to view the current stock percentage'''
        try:
            percentage = self.general.find('span', attrs={"data-reactid": "50"}).text
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
            return
        except AttributeError as error:
            raise StockDoesNotExistError(self.symbol) from error
        try:
            percentage = self.general.find('span', attrs={"data-reactid": "47"}).text
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
            return
        except AttributeError as error:
            raise StockDoesNotExistError(self.symbol) from error
    def driver(self):
        '''this will make it so the class can be automated'''
        self.Price()
        self.percentage()
if __name__ == "__main__":
    data = Price(symbol = "AACG", maximum = 10)
    data.driver()
    print(data.current_price)
