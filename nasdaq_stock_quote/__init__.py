from lxml import html
import requests

'''
NASDAQ Common Stock Quote & Summary Data Scraper
@author Andrew Porter
'''
class Share(object):

    def __init__(self, name):
        self.name = name.upper().strip()
        self.page = requests.get("http://www.nasdaq.com/symbol/" + self.name)
        self.tree = html.fromstring(self.page.content)

    '''
    The below functions scrape NASDAQ by creating a tree of html elements
    and traverse the tree looking for specific elements and tags.

    The returned result is an array of Strings, if the String cannot be
    returned it should return a None type as that means that the requested
    information may not be available for that specific ticker.
    '''
    def get_name(self):
        return self.name

    def get_price(self):
        self.price = self.tree.xpath("//div[@id='qwidget_lastsale']//text()")
        try:
            self.price = self.price[0].replace(",","").replace("$","").strip()
            return self.price
        except IndexError:
            return None

    def get_price_change(self):
        self.price_change = self.tree.xpath("//div[@id='qwidget_netchange']"+
        "//text()")
        try:
            self.price_change = self.price_change[0].replace(",","").strip()
            return self.price_change
        except IndexError:
            return None

    def get_percent_change(self):
        self.percent_change = self.tree.xpath("//div[@id='qwidget_percent']"+
        "//text()")
        try:
            self.percent_change = self.percent_change[0].replace(",","")
            self.percent_change = self.percent_change.replace("%","")
            self.percent_change = str(float(self.percent_change)/100).strip()
            return self.percent_change
        except IndexError:
            return None

    def get_prev_close(self):
        self.prev_close = self.tree.xpath("//*[@id='previous_close']/../../"+
        "td[@align='right']//text()")
        try:
            self.prev_close = self.prev_close[0].replace("$","")
            self.prev_close = self.prev_close.replace(",","").strip()
            return self.prev_close
        except IndexError:
            return None

    def get_day_high(self):
        self.day_high = self.tree.xpath("//*[@id='todays_high_low']/../../"+
        "td/label[@id='Label3']//text()")
        try:
            self.day_high = self.day_high[0].replace("$","").replace(",","")
            self.day_high = self.day_high.strip()
            return self.day_high
        except IndexError:
            return None

    def get_day_low(self):
        self.day_low = self.tree.xpath("//*[@id='todays_high_low']/../../td/"+
        "label[@id='Label1']//text()")
        try:
            self.day_low = self.day_low[0].replace("$","").replace(",","")
            self.day_low = self.day_low.strip()
            return self.day_low
        except IndexError:
            return None

    def get_year_high(self):
        self.year_high = self.tree.xpath("//*[@id='52_week_high_low']/../../"+
        "td[@align='right']//text()")
        try:
            self.year_high = self.year_high[0].replace("$","").replace(",","")
            self.year_high = self.year_high.strip()
            self.year_high = self.year_high[:self.year_high.find("/")].strip()
            return self.year_high
        except IndexError:
            return None

    def get_year_low(self):
        self.year_low = self.tree.xpath("//*[@id='52_week_high_low']/../../"+
        "td[@align='right']//text()")
        try:
            self.year_low = self.year_low[0].replace("$","").replace(",","")
            self.year_low = self.year_low.strip()
            self.year_low = self.year_low[self.year_low.find("/")+1:].strip()
            return self.year_low
        except IndexError:
            return None

    def get_volume(self):
        self.volume = self.tree.xpath("//label[@id='"+self.name+"_Volume'"+
        "]//text()")
        try:
            self.volume =  self.volume[0].replace(",","").strip()
            return self.volume
        except IndexError:
            return None

    def get_fifty_avg_volume(self):
        self.fifty_avg_volume = self.tree.xpath("//*[@id='50_day_avg']/../"+
        "../td[@align='right']//text()")
        try:
            self.fifty_avg_volume = self.fifty_avg_volume[0].replace(",","")
            self.fifty_avg_volume = self.fifty_avg_volume.strip()
            return self.fifty_avg_volume
        except IndexError:
            return None

    def get_price_earnings_ratio(self):
        self.price_earnings = self.tree.xpath("//*[@id='pe_ratio']/../../"+
        "td[@align='right']//text()")
        try:
            self.price_earnings = self.price_earnings[0].replace(",","")
            self.price_earnings = self.price_earnings.strip()
            if( self.price_earnings == "NE" ):
                return None
            return self.price_earnings
        except IndexError:
            return None

    def get_eps(self):
        self.eps = self.tree.xpath("//*[@id='eps']/../../td[@align='right']"+
        "//text()")
        try:
            self.eps = self.eps[0].replace(",","").replace("$","").strip()
            return self.eps
        except IndexError:
            return None

    def get_yield(self):
        self.div_yield = self.tree.xpath("//*[@id='current_yield']/../../"+
        "td[@align='right']//text()")
        try:
            self.div_yield = self.div_yield[0].replace(",","").replace("%","")
            self.div_yield = str(float(self.div_yield)/100).strip()
            return self.div_yield
        except IndexError:
            return None

    def get_market_cap(self):
        self.cap = self.tree.xpath("//*[@id='share_outstanding']/../../"+
        "td[@align='right']//text()")
        try:
            self.cap = self.cap[0].replace("$","").replace(",","")
            self.cap = self.cap.strip()
            return self.cap
        except IndexError:
            return None
