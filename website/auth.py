from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Purchase
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)

SpecialSym = set("!£$%^&*()?@;:~`¬-=_+")


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    """If a POST method then from the form get the data from the email,
    first name, password1 & password2"""
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # Query database to see if user exists already
        user = User.query.filter_by(email=email).first()
        if user:
            flash("User already exists!", category="error")
            return render_template("sign-up.html", user=current_user)

        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(first_name) < 3:
            flash(
                "First Name must be greater than two characters.",
                category="error",
            )
        elif not first_name.isalpha():
            flash("First Name must contain only letters!", category="error")
        elif not last_name.isalpha():
            flash("Last Name must contain only letters!", category="error")
        elif len(last_name) < 3:
            flash(
                "Last Name must be greater than two characters.",
                category="error",
            )
        elif password1 != password2:
            flash("Passwords do not match!", category="error")
        elif len(password1) < 7:
            flash(
                "Password must be greater than 6 characters", category="error"
            )
        elif not any(char.isdigit() for char in password1):
            flash("Password must contain a Numerical value!", category="error")
        elif not any(char.isupper() for char in password1):
            flash("Password must contain a Capital letter!", category="error")
        elif not any(char in SpecialSym for char in password1):
            flash(
                "Password must contain a Special character!", category="error"
            )
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                # Hashes password
                password=generate_password_hash(password1, method="scrypt"),
            )
            db.session.add(new_user)  # Adds new user to database
            db.session.commit()  # Commits information to database
            flash("Account Created! Please login!", category="success")
            login_user(new_user, remember=True)
            return redirect(url_for("views.home"))

    return render_template("sign-up.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        """If users passwords matches then log them in"""
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully!", category="success")
                login_user(user, remember=True)  # Remembers user logged in
                return redirect(url_for("views.home"))
            else:
                flash(
                    "Incorrect password or username. Please try again!",
                    category="error",
                )
        else:
            flash("User doesn't exist", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/submit-purchase-form", methods=["GET", "POST"])
@login_required
def purchase():
    if request.method == "POST":
        car_model = request.form.get("cars")
        valid_car_models = ["Veyron", "Chiron"]

        # Checks if the selected car model is in the list of valid car models.
        if car_model not in valid_car_models:
            flash("Invalid car model selected!")

        country = request.form.get("country")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        company_name = request.form.get("company_name", "")
        address_line1 = request.form.get("address_line1")
        address_line2 = request.form.get("address_line2")
        city = request.form.get("city")
        zip_code = request.form.get("zip_code")
        email = request.form.get("email")
        phone = request.form.get("phone")
        card_number = request.form.get("ccn")
        expiry_month = request.form.get("exp_month")
        expiry_year = request.form.get("exp_year")
        security_code = request.form.get("security_code")

        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(first_name) < 3:
            flash(
                "First Name must be greater than two characters.",
                category="error",
            )
        elif not first_name.isalpha():
            flash("First Name must contain only letters!", category="error")
        elif not last_name.isalpha():
            flash("Last Name must contain only letters!", category="error")
        elif len(last_name) < 3:
            flash(
                "Last Name must be greater than two characters.",
                category="error",
            )
        elif len(country) < 29:
            flash(
                "Country can't be more than 29 characters!", category="error"
            )
        elif len(company_name) < 19:
            flash("Company name can't exceed 19 characters!", category="error")
        elif len(address_line1) < 29:
            flash("Address can't exceed 29 characters!", category="error")
        elif len(address_line2) < 29:
            flash("Address can't exceed 29 characters!", category="error")
        elif len(city) < 85:
            flash("City can't exceed 85 characters!", category="error")
        elif not city.isalpha():
            flash("City must contain only letters!", category="error")
        elif len(zip_code) < 15:
            flash(
                "Zip Code//Post Code must not be more than 15 digits!",
                category="error",
            )
        elif not phone.isdigit():
            flash("Telephone number must be only numerical!", category="error")
        elif len(phone) < 14:
            flash(
                "Phone number can't be more than 14 characters!",
                category="error",
            )
        elif not card_number.isdigit():
            flash(
                "Card number must contain numerical values only!",
                category="error",
            )
        elif len(card_number) < 16:
            flash(
                "Card number can't be more than 16 digits!", category="error"
            )
        elif len(expiry_month) < 3:
            flash("Expiry month can't exceed 2 digits!", category="error")
        elif not expiry_month.isdigit():
            flash("Expiry month must be a numerical value!", category="error")
        elif not expiry_year.isdigit():
            flash("Expiry year must be a numerical value!", category="error")
        elif len(expiry_year) < 3:
            flash("Expiry year can't exceed 2 digits!", category="error")
        elif len(security_code) < 4:
            flash("Security can't exceed 3 digits!", category="error")
        elif not security_code.isdigit():
            flash("Security code must be a numerical value!", category="error")
        else:
            new_purchase = Purchase(
                car_model=car_model,
                country=country,
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                address_line1=address_line1,
                address_line2=address_line2,
                city=city,
                zip_code=zip_code,
                email=email,
                phone=phone,
                card_number=card_number,
                expiry_month=expiry_month,
                expiry_year=expiry_year,
                security_code=security_code,
                user_id=current_user.id,
            )
            db.session.add(new_purchase)
            db.session.commit()
            flash(
                "Purchase successful! Your car will be dispatched to the address provided within 16 weeks!",
                category="success",
            )
            return redirect(url_for("views.home"))

    return render_template("purchase-form.html", user=current_user)
