from setuptools import setup

try:
    with open('LICENSE.txt', 'r') as f:
        _license = f.read()
except:
    readme = ''
    _license = ''

setup(
  name='nasdaq-stock-quote',
  version='1.0',
  description='NASDAQ Common Stock Quote & Summary Data Scraper',
  author='Andrew Porter',
  author_email='porter.r.andrew@gmail.com',
  license=_license,
  url='',
  download_url='https://github.com/AndrewRPorter/nasdaq-stock-quote',
  install_requires=['setuptools', 'requests', 'lxml'],
 )
