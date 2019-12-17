from flask import render_template, Blueprint


main = Blueprint("main", __name__)


@main.route("/")
def home():
    """Render home page"""
    return render_template("home.html", title="Home")
