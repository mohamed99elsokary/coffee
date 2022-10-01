from flask import Blueprint, render_template, request, flash, redirect, url_for, session

from werkzeug.security import generate_password_hash, check_password_hash

coffe = Blueprint("coffe", __name__)


@coffe.route("/coffe", methods=["GET", "POST"])
def main():
    loggedin = "loggedin" in session
    return render_template("coffe.html", loggedin=loggedin, active="coffee")
