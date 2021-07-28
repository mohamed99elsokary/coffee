from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from config import mysql

from werkzeug.security import generate_password_hash, check_password_hash

home = Blueprint("home", __name__)


@home.route("/", methods=["GET", "POST"])
def main():
    loggedin = False
    if "loggedin" in session:
        loggedin = True
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM items ORDER BY id DESC LIMIT 8")
    items = cur.fetchall()

    return render_template("index.html", loggedin=loggedin, items=items, active="home")
