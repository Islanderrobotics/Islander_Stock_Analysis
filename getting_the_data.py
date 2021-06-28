import requests
from bs4 import BeautifulSoup as bs


class GettingTheData:
    '''this class will allow the user the ability to download the data for specific
    markets then import the data. after the data has been turned into a var the file will be deleted'''

    def __init__(self, chosen_market):
        self.chosen_market = chosen_market
        self.data = {}
        self.data[
            "NASDAQ"] = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-FCxor8WIfRHo1ZonFWQ0Kg58PLPn05TPWDOMUaVAp9c27P3iho340L3OfHOaXtd31syD1OXkC1pK/pubhtml"
        self.data[
            "NYSE"] = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTMh-By7UV0GHbQLzYe89xToVarHzn89md26E7flQOTOCoErJgCJge2FdeW2vPGSSnHWpC8K9Q8glwu/pubhtml"
        self.data[
            "AMEX"] = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRh_zI4r9HaDPtzGEonoGas7vVtJipTBS4AjmOz33syFYlqR_EQHiKn5DonOXf0PpqrwClSowvOifMR/pubhtml"

    def download(self):
        '''this is where the download will happen'''
        network = requests.get(self.data[self.chosen_market])
        soup = bs(network.content, "html5lib")
        data = []
        table = soup.find('table', attrs={'class': 'waffle'})
        table_body = table.find('tbody')
        symbol = []
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])  # Get rid of empty values
        for i in range(1, len(data)):
            symbol.append(data[i][0])
        return symbol


