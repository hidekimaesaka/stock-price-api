from app.services.price import get_stock_prices_by_code


def test_if_get_stock_prices_by_code_function_is_returning_value():

    stock = "NVDC34"
    stock_price = get_stock_prices_by_code(stock)

    assert stock_price != ""
