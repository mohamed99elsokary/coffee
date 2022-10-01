from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from config import mysql
from argon2 import PasswordHasher

ph = PasswordHasher()
from werkzeug.security import generate_password_hash, check_password_hash

login = Blueprint("login", __name__)


@login.route("/login", methods=["GET", "POST"])
def home():
    if "loggedin" in session:
        return redirect(url_for("home.main"))

    if request.method == "POST":
        email = request.form.get("email")
        password2 = request.form.get("password")
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s ", (email,))
        result = cur.fetchone()
        if result is None:
            return "invalid user"

        id = result["id"]
        email = result["email"]
        password1 = result["password"]
        first_name = result["first_name"]
        try:
            password = ph.verify(
                password1,
                password2,
            )
            password = True
        except:
            password = False

        if password:
            flash("logged in successfuly", category="success")
            session["loggedin"] = True
            session["id"] = result["id"]
            session["first_name"] = result["first_name"]
            return redirect(url_for("home.main"))
        else:
            flash("Incorrect Password", category="error")
            return render_template("login.html", active="settings")
    return render_template("login.html", active="settings")
