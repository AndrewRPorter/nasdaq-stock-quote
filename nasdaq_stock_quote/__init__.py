from lxml import html
import requests
import sys
import re

'''
NASDAQ Common Stock Quote & Summary Data Scraper
@author Andrew Porter / Tony Lucas
'''
class Share(object):

    def __init__(self, name):
        self.name = str(name).upper().strip()
        try:
            self.page = requests.get("http://www.nasdaq.com/symbol/" + self.name)
            self.tree = html.fromstring(self.page.content)
            self.page_text = self.page.text
            arrow = self.page_text.find('id="qwidget-arrow"')
            self.arrow_direction = self.page_text[arrow+44:arrow+44+9]
        except Exception as e:
            print("ERROR:\n" + str(e.args) + "\n\nTerminating execution...")
            sys.exit()

    '''
    The below functions scrape NASDAQ by creating a tree of html elements
    and traverse the tree looking for specific elements and tags.

    The returned result is an array of Strings, if the String cannot be
    returned it should return a None type as that means that the requested
    information may not be available for that specific ticker.  There are two
    execptions to returning strings, the 52 Week High/Low and Today's High/Low.
    These two results are returned as a float list.
    '''

    def get_price(self):
        price = self.tree.xpath("//div[@id='qwidget_lastsale']//text()")
        try:
            price = price[0].replace(",","").replace("$","").strip()
            return price
        except IndexError:
            return None

    def get_price_change(self):
        price_change = self.tree.xpath("//div[@id='qwidget_netchange']"+
        "//text()")
        try:
            price_change = price_change[0].replace(",","").strip()
            if self.arrow_direction == 'arrow-red':
                price_change = '-' + price_change
            return price_change
        except IndexError:
            return None

    def get_percent_change(self):
        percent_change = self.tree.xpath("//div[@id='qwidget_percent']"+
        "//text()")
        try:
            percent_change = percent_change[0].replace(",","")
            percent_change = percent_change.replace("%","")
            percent_change = str(float(percent_change)/100).strip()
            if self.arrow_direction == 'arrow-red':
                percent_change = '-' + percent_change
            return percent_change
        except IndexError:
            return None

    def get_prev_close(self):
        previous = self.page_text.find('Previous')
        if previous == -1:
            return 'Not Found'
        try:
            prev_close = self.page_text[previous+606:previous+606+8].strip()
            return prev_close
        except:
            return None
        
    def get_hi_lo(self):
        todays_high_low = self.page_text.find('todays_high_low')
        try:
            hi_lo = self.page_text[todays_high_low+986:todays_high_low+986+40]
            hi_lo = hi_lo.replace(',', '')
            hi_lo = re.findall(r"[-+]?\d*\.\d+|\d+", hi_lo)
            return hi_lo
        except:
            return None

    def get_year_high_low(self):
        year_week_hi_lo = self.page_text.find('52_week_high_low')
        try:
            year_high_low = self.page_text[year_week_hi_lo+1032:year_week_hi_lo+1032+40]
            year_high_low = year_high_low.replace(',', '')
            year_high_low = re.findall(r"[-+]?\d*\.\d+|\d+", year_high_low)
            return year_high_low
        except:
            return None
            

    def get_volume(self):
        share_volume = self.page_text.find('share_volume')
        try:
            volume =  self.page_text[share_volume+816:share_volume+816+20].strip()
            return volume
        except:
            return None

    def get_ninety_avg_volume(self):
        ninety_day_avg = self.page_text.find('90_day_avg')
        if ninety_day_avg == -1:
            ninety_day_avg = self.page_text.find('50_day_avg')
        try:
            ninety_avg_volume = self.page_text[ninety_day_avg+862:ninety_day_avg+862+20].strip()
            return ninety_avg_volume
        except:
            return None

    def get_price_earnings_ratio(self):
        pe_ratio = self.page_text.find('pe_ratio')
        if pe_ratio == -1:
            return 'N/A'
        try:
            price_earnings = self.page_text[pe_ratio+861:pe_ratio+861+12].strip()
            return price_earnings
        except:
            return None

    def get_eps(self):
        eps_index = self.page_text.find('id="eps"')
        if eps_index == -1:
            return 'N/A'
        try:
            eps = self.page_text[eps_index+1218:eps_index+1218+8].strip()
            return eps
        except:
            return None

    def get_yield(self):
        current_yield = self.page_text.find('current_yield')
        try:
            div_yield = self.page_text[current_yield+912:current_yield+912+5].strip()
            return div_yield
        except:
            return None

    def get_market_cap(self):
        share_outstanding = self.page_text.find('share_outstanding')
        try:
            cap = self.page_text[share_outstanding+1212:share_outstanding+1212+25].strip()
            return cap
        except:
            return None
        
    def get_ex_dividend_date(self):
        ex_dividend_date = self.page_text.find('ex_dividend_date')
        try:
            ex_div = self.page_text[ex_dividend_date+832:ex_dividend_date+832+15].strip()
            return ex_div
        except:
            return None
        
    def get_forward_pe(self):
        forward_PE = self.page_text.find('forward_PE')
        if forward_PE == -1:
            return 'N/A'
        try:
            fpe = self.page_text[forward_PE+934:forward_PE+934+12].strip()
            return fpe
        except:
            return None
        
    def get_dividend(self):
        annual = self.page_text.find('annualized_dividend')
        if annual == -1:
            return 'N/A'
        try:
            div_str = self.page_text[annual+703:annual+703+15].strip()
            div_num = re.findall(r"[-+]?\d*\.\d+|\d+", div_str)
            if len(div_num) == 0:                                
                return 'N/A'                                     
            else:                                                
                self.div = str(div_num[0])
                return self.div
        except:
            return None
        
    def get_dividend_date(self):
        dividend_date = self.page_text.find('dividend_payment_date')
        if dividend_date == -1:
            return 'N/A'
        try:
            div_date = self.page_text[dividend_date+794:dividend_date+794+15].strip()
            return div_date
        except:
            return None    
        
    def get_beta(self):
        id_beta = self.page_text.find('id="beta"')
        if id_beta == -1:
            return 'N/A'
        try:
            beta = self.page_text[id_beta+934:id_beta+934+5].strip()
            if beta == '0':
                beta = 'N/A'
            return beta
        except:
            return None
