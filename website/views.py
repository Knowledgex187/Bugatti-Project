from flask import Blueprint, render_template

views = Blueprint("views", __name__)


# About Page
@views.route("/")
def home():
    return render_template("about.html")


# Bugatti Chiron Page
@views.route("/bugatti-chiron")
def bugatti_chiron():
    return render_template("bugatti-chiron.html")


# Bugatti Veyron Page
@views.route("/bugatti-veyron")
def bugatti_veyron():
    return render_template("bugatti-veyron.html")


# Conversions Page
@views.route("/conversions")
def conversions():
    return render_template("conversions.html")


# FAQ Page
@views.route("/faq")
def faq():
    return render_template("faq.html")


# History Page
@views.route("/history")
def history():
    return render_template("history.html")
