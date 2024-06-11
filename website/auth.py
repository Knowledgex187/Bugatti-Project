from flask import Blueprint, render_template, request, flash

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
            flash("Account created successfully!", category="success")

    return render_template("sign-up.html")


@auth.route("/logout")
def logout():
    pass


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/submit-purchase-form")
def purchase_form():
    return render_template("purchase-form.html")
