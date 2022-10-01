from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from config import mysql
from argon2 import PasswordHasher

ph = PasswordHasher()
from werkzeug.security import generate_password_hash, check_password_hash

sign_up = Blueprint("sign_up", __name__)


@sign_up.route("/sign-up", methods=["GET", "POST"])
def home():
    cur = mysql.connection.cursor()
    if "loggedin" in session:
        return redirect(url_for("home.main"))
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        address = request.form.get("address")
        address2 = request.form.get("address2")
        city = request.form.get("city")
        state = request.form.get("state")
        zip = request.form.get("zip")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        cur.execute("SELECT * FROM users WHERE email = %s ", (email,))
        result = cur.fetchone()
        if result is None:
            if len(email) == 0:
                flash("You have to use an email address", category="error")
            elif len(email) < 4:
                flash("email must be greater than 3 characters", category="error")
            elif len(first_name) < 2:
                flash(
                    "first name must be greater than 1 characters",
                    category="error",
                )
            elif len(last_name) < 2:
                flash(
                    "last name must be greater than 1 characters",
                    category="error",
                )
            elif len(password) < 7:
                flash(
                    "password must be greater than 6 characters",
                    category="error",
                )
            else:
                password = ph.hash(password)
                cur.execute(
                    "INSERT INTO users SET first_name = %s, last_name=%s, address=%s, address2=%s , city = %s , state = %s , zip=%s , email = %s , user_name = %s , password = %s ",
                    (
                        first_name,
                        last_name,
                        address,
                        address2,
                        city,
                        state,
                        zip,
                        email,
                        username,
                        password,
                    ),
                )
                mysql.connection.commit()
                cur.execute("SELECT * FROM users WHERE email = %s ", (email,))
                result = cur.fetchone()
                session["loggedin"] = True
                session["id"] = result["id"]
                session["first_name"] = result["first_name"]
                flash("Account Created ", category="success")
                return redirect(url_for("home.main"))

        else:
            flash("email is aleady taken", category="error")
    return render_template("signup.html", active="settings")
