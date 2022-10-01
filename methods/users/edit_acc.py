from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from config import mysql
from argon2 import PasswordHasher

ph = PasswordHasher()
from werkzeug.security import generate_password_hash, check_password_hash

edit_acc = Blueprint("edit_acc", __name__)


@edit_acc.route("/edit_acc", methods=["GET", "POST"])
def home():
    if "loggedin" not in session:
        return redirect(url_for("home.main"))
    id = session["id"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s ", (id,))
    result = cur.fetchone()
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        address = request.form.get("address")
        address2 = request.form.get("address2")
        city = request.form.get("city")
        state = request.form.get("state")
        zip = request.form.get("zip")
        email = request.form.get("email")
        user_name = request.form.get("user_name")
        old_password = request.form.get("password")

        if result != None:
            try:
                password = ph.verify(
                    result["password"],
                    old_password,
                )
                password = True
            except:
                password = False

            if password:
                first_name = first_name if first_name != "" else result["first_name"]
                last_name = last_name if last_name != "" else result["last_name"]
                address = address if address != "" else result["address"]
                address2 = address2 if address2 != "" else result["address2"]
                city = city if city != "" else result["city"]
                state = state if state != "" else result["state"]
                zip = zip if zip != "" else result["zip"]
                if email != "":
                    print(email)
                    email = email
                else:
                    email = result["email"]
                user_name = user_name if user_name != "" else result["user_name"]
                cur.execute(
                    "UPDATE users SET first_name =%s  , last_name = %s , address = %s, address2=%s, city = %s , state = %s , zip = %s , email = %s , user_name = %s WHERE id = %s",
                    (
                        first_name,
                        last_name,
                        address,
                        address2,
                        city,
                        state,
                        zip,
                        email,
                        user_name,
                        id,
                    ),
                )
                mysql.connection.commit()
                session.pop("first_name", None)
                session["first_name"] = first_name
                flash("edit saved successfully", category="success")
                return redirect(url_for("home.main"))
            else:
                flash("Wrong Password", category="error")
    return render_template(
        "profile.html",
        title="edit acc",
        profile=result,
        loggedin=True,
        active="settings",
    )
