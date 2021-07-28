from config import app, ui
from flask import Blueprint, render_template, request, flash, redirect, url_for, session

app.config["SECRET_KEY"] = "dk;vnjfvdfblkcvjn klasdanfivsndsj"

# ------------------------------users
from methods.users.sign_up import sign_up
from methods.users.login import login
from methods.users.logout import logout
from methods.users.reset_password import reset_password
from methods.users.edit_acc import edit_acc
from methods.users.delete import delete

# ------------------------------home
from methods.home.home import home
from methods.home.about import about
from methods.home.coffe import coffe

# ------------------------------products
from methods.products.all_products import all_products
from methods.products.product import product


# ------------------------------users
app.register_blueprint(delete)
app.register_blueprint(edit_acc)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(reset_password)
app.register_blueprint(sign_up)

# ------------------------------home
app.register_blueprint(home)
app.register_blueprint(about)
app.register_blueprint(coffe)
# ------------------------------products
app.register_blueprint(all_products)
app.register_blueprint(product)


"""if __name__ == "__main__":
    app.run(host="192.168.1.2", port=80, debug=True)"""
ui.run()
