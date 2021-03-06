# -*- coding: utf-8 -*-
"""
    department_app.forms
    ~~~~~~~~~~~~~~~~~~~~

    Forms for:
    - adding and updating employees;
    - adding and updating departments;
    - search employees by date of birth.
"""

from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, DecimalField,
                     DateField, IntegerField)
from wtforms.validators import DataRequired, Length, ValidationError
from department_app.models import Department


class EmployeeForm(FlaskForm):
    """Form for adding and updating employees."""
    name = StringField(
        "Name", validators=[DataRequired(), Length(min=2, max=50)]
    )
    date_of_birth = DateField("Date of Birth", validators=[DataRequired()])
    salary = DecimalField("Salary", validators=[DataRequired()])
    department_id = IntegerField("Department", validators=[DataRequired()])

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


class SearchForm(FlaskForm):
    """Form for searching employees by date of birth."""
    from_date = DateField("From", validators=[DataRequired()])
    to_date = DateField("To", validators=[DataRequired()])

    def validate_to_date(self, to_date):
        """Check if from date is before to date in the form."""
        if self.to_date.data < self.from_date.data:
            raise ValidationError("To date must be after from date.")

    submit = SubmitField("Search")
