from flask import Blueprint, request, jsonify
from datetime import date

from app.services.price import get_stock_prices_by_code

stock_price_bp = Blueprint("stock_price", __name__)


@stock_price_bp.route("/", methods=["GET"])
def get_stock_price_by_code():

    stock_code = request.args.get("stock_code")
    stock_price = get_stock_prices_by_code(stock_code)

    if stock_price:

        return jsonify({
            "Code": stock_code.upper(),
            "Date": date.today(),
            "Price": stock_price
        })

    return jsonify({
        "Message": "Stock not found! Keep in mind that this API only gets the IBOVESPA stocks"
    })


def init(app):
    app.register_blueprint(stock_price_bp)
