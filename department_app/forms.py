from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, IntegerField, 
                     DecimalField, DateField, SelectField)
from wtforms.validators import DataRequired, Length
from department_app.models import Employee, Department


class AddEmployeeForm(FlaskForm):
    name = StringField(
        "Name", validators=[DataRequired(), Length(min=2, max=50)]
    )
    date_of_birth = DateField("Date of Birth", validators=[DataRequired()])
    salary = DecimalField("Salary", validators=[DataRequired()])
    department_id = SelectField("Department", coerce=int, choices=[
        (1, "Python Flask"), (2, "Python Django"), (3, "Front End"), 
        (4, "Human Resources")])
    
    submit = SubmitField("Add Employee")


class AddDepartmentForm(FlaskForm):
    name = StringField(
        "Name", validators=[DataRequired(), Length(min=2, max=100)]
    )
    
    submit = SubmitField("Add Department")
