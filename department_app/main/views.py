# -*- coding: utf-8 -*-
"""
    department_app.main.views
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Routes for app functionality other than employees and departments.
"""

from flask import render_template, Blueprint


main = Blueprint("main", __name__)


@main.route("/")
def home():
    """Render home page"""
    return render_template("home.html", title="Home")
