from flask import Flask


def create_app():
    """Function to run flask"""
    app = Flask(__name__)
    # Initialize flask app. Represents the name of the file ran.

    # Config variable, encrypt or secure cookie data related to our website
    app.config["SECRET_KEY"] = "imelaezemoh7"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
