from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()  # Creates an instance of SQLAlchemy.
migrate = Migrate()
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

    # Used to bind the SQLAlchemy instance to your Flask application.
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models here to avoid circular imports
    from .models import User, Purchase

    User = User
    Purchase = Purchase

    # Create the database if it doesn't exist
    with app.app_context():
        if not path.exists("website/" + DB_NAME):
            db.create_all()
            print("Created Database!")

    # Register blueprints
    from .views import views
    from .auth import auth

    # Register the base prefix to access auth and views routes
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Setup Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
