from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from config import mysql

from werkzeug.security import generate_password_hash, check_password_hash

product = Blueprint("product", __name__)


@product.route("/product/<int:page_id>", methods=["GET", "POST"])
def main(page_id):
    if "loggedin" in session:
        loggedin = True
    else:
        loggedin = False
    id = page_id
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM items Where id = %s", (id,))
    item = cur.fetchone()
    return render_template(
        "show details.html", item=item, loggedin=loggedin, active="products"
    )
