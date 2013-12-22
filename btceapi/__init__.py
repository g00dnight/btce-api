# Copyright (c) 2013 Alan McIntyre
__version__ = "0.3.0"
from public import getDepth, getTicker, getTradeFee, getTradeHistory
from trade import TradeAPI
from scraping import scrapeMainPage
from keyhandler import KeyHandler
from common import all_currencies, all_pairs, min_orders,\
                   max_digits_rate, max_digits_amount,\
                   formatCurrencyRate, formatCurrencyAmount, formatCurrencyDigits, \
                   truncateAmount, truncateAmountDigits, \
                   validatePair, validateOrder, \
                   BTCEConnection
