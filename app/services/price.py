from pandas_datareader import data as web
from datetime import date


def get_stock_prices_by_code(stock_code):

    today = str(date.today())

    try:
        cotacao = web.DataReader(
            f"{stock_code}.SA", data_source="yahoo", start=today)

        stock_price = cotacao["Adj Close"][today]

        return stock_price

    except Exception as e:
        return None
