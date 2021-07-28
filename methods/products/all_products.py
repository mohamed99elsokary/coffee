from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from config import mysql

from werkzeug.security import generate_password_hash, check_password_hash

all_products = Blueprint("all_products", __name__)


@all_products.route("/all-products", methods=["GET", "POST"])
def main():
    if "loggedin" in session:
        loggedin = True
    else:
        loggedin = False
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM items ORDER BY id DESC")
    items = cur.fetchall()

    return render_template(
        "all products.html", items=items, loggedin=loggedin, active="products"
    )
