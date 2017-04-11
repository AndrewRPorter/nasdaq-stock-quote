from setuptools import setup

try:
    with open('LICENSE.txt', 'r') as f:
        _license = f.read()
except:
    _license = ''

setup(
  name='nasdaq_stock_quote',
  packages=['nasdaq_stock_quote'],
  version='1.2.0',
  description='NASDAQ Common Stock Quote & Summary Data Scraper',
  author='Andrew Porter',
  author_email='porter.r.andrew@gmail.com',
  license=_license,
  url='https://github.com/AndrewRPorter/nasdaq-stock-quote',
  download_url='https://github.com/AndrewRPorter/nasdaq-stock-quote/archive/1.1.0.tar.gz',
  install_requires=['setuptools', 'requests', 'lxml'],
 )
