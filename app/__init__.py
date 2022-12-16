from flask import Flask

# routes
from app.controllers import stock


def create_app():

    app = Flask(__name__)

    stock.init(app)

    return app
