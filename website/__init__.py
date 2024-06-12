from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()  # creates an instance of SQLAlchemy.
DB_NAME = "database.db"


def create_app():
    """Function to run flask"""
    app = Flask(__name__)
    # Initialize flask app. Represents the name of the file ran.

    # Config variable, encrypt or secure cookie data related to our website
    app.config["SECRET_KEY"] = "imelaezemoh7"

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"sqlite:///{DB_NAME}"  # Defines database URI
    )

    """In summary, db.init_app(app) is a crucial step in setting up
    SQLAlchemy with a Flask application, allowing you to use the
    database within the context of the Flask app."""

    # Used to bind the SQLAlchemy instance to your Flask application.
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .views import views
    from .auth import auth

    # Register the base prefix to access auth and views routes
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Purchase

    User = User
    Purchase = Purchase

    """This line creates an instance of the LoginManager class from the
    Flask-Login extension. The LoginManager object will handle user session
    management, such as remembering logged-in users and handling
    user login/logout."""
    login_manager = LoginManager()

    # This line sets the view function that should handle login requests.
    login_manager.login_view = "auth.login"

    """This line initializes the LoginManager object with your Flask
    application instance (app). By calling init_app(app), you are associating
    the login_manager with the Flask application, allowing it to handle user
    session management for the app."""
    login_manager.init_app(app)

    """The @login_manager.user_loader decorator and the load_user function
    are used in Flask-Login to specify how to load a user from the user
    ID stored in the session. """

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    # Check if path already exists
    if not path.exists("website/" + DB_NAME):
        db.create_all(app)
        print("Created Database!")
