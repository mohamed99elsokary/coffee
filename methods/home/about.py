from flask import Blueprint, render_template, request, flash, redirect, url_for, session

from werkzeug.security import generate_password_hash, check_password_hash

about = Blueprint("about", __name__)


@about.route("/about", methods=["GET", "POST"])
def main():
    loggedin = "loggedin" in session
    return render_template("about.html", loggedin=loggedin, active="about")
