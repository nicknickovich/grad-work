from flask import render_template, url_for, redirect, flash

from department_app import db, app


@app.route("/")
def home():
    return render_template("home.html", title="EMS Home")


