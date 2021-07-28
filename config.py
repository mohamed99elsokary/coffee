from flask import Flask
from flask_mysqldb import MySQL
from flaskwebgui import FlaskUI


app = Flask(__name__)

ui = FlaskUI(app)

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345678"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "coffe"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
