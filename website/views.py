from flask import Blueprint, render_template
from flask_login import current_user

views = Blueprint("views", __name__)


# About Page
@views.route("/")
def home():
    return render_template("about.html", user=current_user)


# Bugatti Chiron Page
@views.route("/bugatti-chiron")
def bugatti_chiron():
    return render_template("bugatti-chiron.html", user=current_user)


# Bugatti Veyron Page
@views.route("/bugatti-veyron")
def bugatti_veyron():
    return render_template("bugatti-veyron.html", user=current_user)


# Conversions Page
@views.route("/conversions")
def conversions():
    return render_template("conversions.html", user=current_user)


# FAQ Page
@views.route("/faq")
def faq():
    return render_template("faq.html", user=current_user)


# History Page
@views.route("/history")
def history():
    return render_template("history.html", user=current_user)
