from pandas_datareader import data as web
import yfinance as yf
import pandas as pd
from datetime import date


def get_stock_prices_by_code(stock_code):

    yf.pdr_override()

    today = str(date.today())

    try:
        cotacao = web.DataReader(
            f"{stock_code}.SA", data_source="yahoo", start=today)
        # print(cotacao)
        stock_price = cotacao["Adj Close"][0]

        return stock_price

    except Exception as e:
        print(e)
        return None
