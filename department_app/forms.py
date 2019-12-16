from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, IntegerField, 
                     DecimalField, DateField, SelectField)
from wtforms.validators import DataRequired, Length, ValidationError
from department_app.models import Department
from department_app import db


class EmployeeForm(FlaskForm):
    """Form for adding and updating employees."""
    name = StringField(
        "Name", validators=[DataRequired(), Length(min=2, max=50)]
    )
    date_of_birth = DateField("Date of Birth", validators=[DataRequired()])
    salary = DecimalField("Salary", validators=[DataRequired()])
    department_id = SelectField("Department", coerce=int, choices=[
        (department.id, department.name) for department in
        Department.query.order_by(Department.id).all()])
    
    submit = SubmitField("Submit")


class DepartmentForm(FlaskForm):
    """Form for adding and updating departments."""
    name = StringField(
        "Name", validators=[DataRequired(), Length(min=2, max=100)]
    )
    
    def validate_name(self, name):
        """Check if department with provided name exists."""
        department = Department.query.filter_by(name=name.data).first()
        if department:
            raise ValidationError("Department with this name already exists.")

    submit = SubmitField("Submit")
