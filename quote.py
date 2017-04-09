from lxml import html
import requests

'''
NASDAQ Common Stock Quote & Summary Data Scraper
@author Andrew Porter
'''
class Ticker(object):
    #Constructs a ticker object, scraping the information from nasdaq.com
    def __init__(self, name):
        self.name = name.upper().strip()
        self.page = requests.get("http://www.nasdaq.com/symbol/" + self.name)
        self.tree = html.fromstring(self.page.content)

    #Returns the price of the ticker as a String without commas and dollars
    def get_price(self):
        self.price = self.tree.xpath("//div[@id='qwidget_lastsale']//text()")
        try:
            return self.price[0].replace("","").replace("$","").strip()
        except IndexError:
            return None

    #Returns the price change from last open as a String without commas
    def get_price_change(self):
        self.price_change = self.tree.xpath("//div[@id='qwidget_netchange']//text()")
        try:
            return self.price_change[0].replace(",","").strip()
        except IndexError:
            return None

    #Returns the percent change from last open as a String without a percent
    def get_percent_change(self):
        self.percent_change = self.tree.xpath("//div[@id='qwidget_percent']//text()")
        try:
            return str(float(self.percent_change[0].replace("%",""))/100).strip()
        except IndexError:
            return None

    #Returns the volume of the ticker as a String without commmas
    def get_volume(self):
        self.volume = self.tree.xpath("//label[@id='" + self.name + "_Volume'" + "]//text()")
        try:
            return self.volume[0].replace(",","").strip()
        except IndexError:
            return None

    def get_price_earnings_ratio(self):
        self.price_earnings = self.tree.xpath("//*[@id='pe_ratio']/../../td[@align='right']//text()")
        try:
            return self.price_earnings[0].replace(",","").strip()
        except IndexError:
            return None

    def get_eps(self):
        self.eps = self.tree.xpath("//*[@id='eps']/../../td[@align='right']//text()")
        try:
            return self.eps[0].replace("","").replace("$","").strip()
        except IndexError:
            return None
