# -*- coding: utf-8 -*-
"""
    department_app
    ~~~~~~~~~~~~~~

    Module for initializing the app, database, serializer
    and blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
def create_app(config_file):
    app = Flask(__name__, instance_relative_config=True)
    with app.app_context():
        app.config.from_object("config")
        app.config.from_pyfile(config_file)

        db.init_app(app)

        from department_app.main.views import main
        from department_app.employees.views import emp
        from department_app.departments.views import dep
        from department_app.api.views import api

        app.register_blueprint(main)
        app.register_blueprint(emp)
        app.register_blueprint(dep)
        app.register_blueprint(api)

    return app
