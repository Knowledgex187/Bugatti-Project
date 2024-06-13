from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # Establish relationship with Purchase
    purchases = db.relationship("Purchase", back_populates="user")


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_model = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100))
    address_line1 = db.Column(db.String(200), nullable=False)
    address_line2 = db.Column(db.String(200))
    city = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    expiry_month = db.Column(db.String(2), nullable=False)
    expiry_year = db.Column(db.String(2), nullable=False)
    security_code = db.Column(db.String(3), nullable=False)

    # Foreign key to link Purchase to User
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # Establish relationship with User
    user = db.relationship("User", back_populates="purchases")
