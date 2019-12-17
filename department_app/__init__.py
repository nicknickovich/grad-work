from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

from department_app.main.views import main
from department_app.employees.views import emp
from department_app.departments.views import dep

app.register_blueprint(main)
app.register_blueprint(emp)
app.register_blueprint(dep)
