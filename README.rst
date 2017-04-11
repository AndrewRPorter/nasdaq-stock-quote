==================
nasdaq-stock-quote
==================

Installation
------------
From PyPI with pip:

.. code:: bash

    $ pip install nasdaq-stock-quote
    
Usage
-----

.. code:: python

    >>> from nasdaq_stock_quote import Share
    >>> share = Share('aapl')
    >>> print(share.get_price())
    143.17
    >>> print(share.get_market_cap())
    751147131800
    
Methods

- ``get_name()``
- ``get_price()``
- ``get_price_change()``
- ``get_percent_change()``
- ``get_prev_close()``
- ``get_day_high()``
- ``get_day_low()``
- ``get_year_high()``
- ``get_year_low()``
- ``get_volume()``
- ``get_fifty_avg_volume()``
- ``get_price_earnings_ratio()``
- ``get_eps()``
- ``get_yield()``
- ``get_market_cap()``
  
Motivation
----------

This project was created purely to mimic the behavior of the yahoo-finance module but scrape data from NASDAQ.

License
-------

MIT License

Copyright (c) 2017 Andrew Porter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
