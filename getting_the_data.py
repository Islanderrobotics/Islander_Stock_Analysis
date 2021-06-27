import pandas as pd
from selenium import webdriver
from pathlib import Path
import requests
import os

class GettingTheData:
    '''this class will allow the user the ability to download the data for specific
    markets then import the data. after the data has been turned into a var the file will be deleted'''
    def __init__(self, chosen_market):
        self.chosen_market = chosen_market
        self.data = {}
        self.data["NYSE"] = []
        self.data["NASDAQ"] = []
        self.data["AMEX"] = []
        self.data["NASDAQ"].append("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-FCxor8WIfRHo1ZonFWQ0Kg58PLPn05TPWDOMUaVAp9c27P3iho340L3OfHOaXtd31syD1OXkC1pK/pub?output=csv")
        self.data["NYSE"].append("https://docs.google.com/spreadsheets/d/e/2PACX-1vTTKk2nCD7HySXPHXH7mH1X_ZVeAMbQWRyrHz-3BgXxG7hvRpqJY7pfTYMi5rSZ2NpClbt2DieD7pEt/pub?output=csv")
        self.data["AMEX"].append("https://docs.google.com/spreadsheets/d/e/2PACX-1vRh_zI4r9HaDPtzGEonoGas7vVtJipTBS4AjmOz33syFYlqR_EQHiKn5DonOXf0PpqrwClSowvOifMR/pub?output=csv")
        self.data["NASDAQ"].append("/Users/williammckeon/Downloads/NASADQ - Sheet1.csv")
        self.data["NYSE"].append("/Users/williammckeon/Downloads/NYSE - sheet1.csv")
        self.data["AMEX"].append("/Users/williammckeon/Downloads/AMEX - sheet1.csv")
        self.driver_path = "/Users/williammckeon/Sync/chromedriver"
    
    def download(self):
        '''this is where the download will happen'''
        count = 0
        while True:
            try:
                requests.get(self.data[self.chosen_market][0])
                break
            except requests.ConnectionError:
                if (count == 0):
                    print("please connect to the WIFI")
                    count+=1
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.data[self.chosen_market][0])
        while (True):
            if Path(self.data[self.chosen_market][1]).is_file():
                break

    def delete(self):
        '''this function will delete the data once the file is done with the data'''
        os.remove(path = self.data[self.chosen_market][1])

    def symbols(self):
        stock = pd.read_csv(self.data[self.chosen_market][1])
        return(stock.iloc[:,0])
