from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":  # retrieving data from login form
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(
            email=email  # checking if user exists
        ).first()  # .first() return first occurance of given email,
        if user:
            if user.password == password:
                login_user(user, remember=False)
                return redirect(url_for("views.jobs_list"))
            else:
                flash(
                    "Enter correct email address and password", category="login_error"
                )
        else:
            flash("User does not exists", category="login_error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required  # doesn't allow this function unless a user is logged in
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Gets data from sign up form, checks it - if any error - pop up will show up.
    If data is correct - account is created
    """
    if request.method == "POST":  # retrieving data from html signup form
        first_name = request.form.get("firstname")
        last_name = request.form.get("lastname")
        password = request.form.get("password")
        password_conf = request.form.get("password_conf")
        email = request.form.get("email")
        company = request.form.get("company")

        user = User.query.filter_by(
            email=email
        ).first()  # .first() return first occurance of given email
        if user:  # just some input checking stuff
            flash("User with this email already exists!", category="signup_error")
        else:
            if len(first_name) < 3:
                flash("Provide correct first name", category="signup_error")
            elif len(password) < 6:
                flash(
                    "Your password must be at least 6 characters long",
                    category="signup_error",
                )
            elif password != password_conf:
                flash("Confirm your password", category="signup_error")
            elif len(email) < 4 or "@" not in email:
                flash("Provide correct email", category="signup_error")
            else:
                # creating new user instance
                new_user = User(
                    firstname=first_name,
                    lastname=last_name,
                    password=password,
                    email=email,
                    company=company,
                )
                db.session.add(new_user)  # adding new user to database
                db.session.commit()  # committing db changes
                flash("Account successfully created!", category="signup_success")
                return redirect(url_for("auth.login"))

    return render_template("signup.html", user=current_user)


"""
        if user:
            if check_password_hash(
                user.password, password
            ):  # checking if password is the same (hashed)
                login_user(user, remember=True)
                return redirect(url_for("views.jobs_list"))




            else:
                # creating new user instance
                new_user = User(
                    firstname=first_name,
                    lastname=last_name,
                    password=generate_password_hash(
                        password, method="sha256"
                    ),  # hashing password for security purposes
                    email=email,
                    company=company,
"""
