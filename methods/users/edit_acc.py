from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from config import mysql
from argon2 import PasswordHasher

ph = PasswordHasher()
from werkzeug.security import generate_password_hash, check_password_hash

edit_acc = Blueprint("edit_acc", __name__)


@edit_acc.route("/edit_acc", methods=["GET", "POST"])
def home():
    if "loggedin" in session:
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

                if password == True:
                    if first_name != "":
                        first_name = first_name
                    else:
                        first_name = result["first_name"]
                    if last_name != "":
                        last_name = last_name
                    else:
                        last_name = result["last_name"]
                    if address != "":
                        address = address
                    else:
                        address = result["address"]
                    if address2 != "":
                        address2 = address2
                    else:
                        address2 = result["address2"]
                    if city != "":
                        city = city
                    else:
                        city = result["city"]
                    if state != "":
                        state = state
                    else:
                        state = result["state"]
                    if zip != "":
                        zip = zip
                    else:
                        zip = result["zip"]
                    if email != "":
                        print(email)
                        email = email
                    else:
                        email = result["email"]
                    if user_name != "":
                        user_name = user_name
                    else:
                        user_name = result["user_name"]

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
    else:
        return redirect(url_for("home.main"))
