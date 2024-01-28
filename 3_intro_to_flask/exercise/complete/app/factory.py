from flask import Flask
from .views.index import index_blueprint
from .views.user import user_blueprint
from .views.post import post_blueprint


def create_app():
    """
    Flask Factory.

    Create and return a singleton Flask instance to be used
    throughout the project.
    :return: Flask App
    """

    app = Flask(__name__)

    # Add any relevant config: Database URI, Token Configuration etc.

    # Register your blueprints (User and Post)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(post_blueprint)

    return app
