"""Index blueprint. Simply returns some text to welcome the user if visiting on browser."""

from flask import Blueprint


index_blueprint = Blueprint("index", __name__)


@index_blueprint.route("/", methods=["GET"])
def index():
    return "Welcome! Enjoy the API \U0001F603"
