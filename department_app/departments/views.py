# -*- coding: utf-8 -*-
"""
    department_app.departments.views
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Routes for department functionality of the app.

    Routes:
    - show_departments: show all departments;
    - add_department: add new department;
    - show_department: show department with a given id;
    - update_department: update department with a given id;
    - delete_department delete department with a given id;
"""
import os
from flask import render_template, Blueprint, url_for, redirect, request, flash
from sqlalchemy.exc import IntegrityError
from department_app.models import Employee, Department
from department_app import db
from department_app.forms import DepartmentForm
import pymysql


dep = Blueprint("dep", __name__)


@dep.route("/departments")
def show_departments():
    """Render a list of all departments"""
    departments = Department.query.order_by(Department.id).all()

    # Connect with database using pymysql
    con = pymysql.connect(host=os.environ.get("MY_HOST"),
                          user=os.environ.get("MY_USER"),
                          password=os.environ.get("MY_PASSWORD"),
                          db="company",
                          cursorclass=pymysql.cursors.DictCursor)
    
    with con:
        cur = con.cursor()
        # Calculate average salary for departments
        cur.execute("""SELECT department.id AS dep_id, 
                              AVG(employee.salary) AS avg_sal
                       FROM employee
                       JOIN department
                       ON employee.department_id = department.id
                       GROUP BY department_id
                    """)

    rows = cur.fetchall()

    avg_salaries = {row["dep_id"]: row["avg_sal"] for row in rows}

    return render_template(
        "departments.html", departments=departments,
        avg_salaries=avg_salaries, title="All departments"
    )


@dep.route("/add_department", methods=["GET", "POST"])
def add_department():
    """Add a new department using a form."""
    form = DepartmentForm()

    if form.validate_on_submit():
        # Set department name to a value from the form.
        department = Department(name=form.name.data)
        db.session.add(department)
        db.session.commit()
        flash("Department has been added!", "success")
        return redirect(url_for("dep.show_departments"))

    return render_template(
        "add_department.html", title="Add new department",
        form=form, legend="New Department"
    )


@dep.route("/department/<int:department_id>")
def show_department(department_id):
    """Render page of a department with a given id"""
    department = Department.query.get_or_404(department_id)
    return render_template(
        "department.html", title=department.name, department=department
    )


@dep.route("/department/<int:department_id>/update", methods=["GET", "POST"])
def update_department(department_id):
    """Delete department with a given id"""
    department = Department.query.get_or_404(department_id)
    form = DepartmentForm()

    if form.validate_on_submit():
        # Set department name to a value from the form.
        department.name = form.name.data
        db.session.commit()
        flash("Department has been updated!", "success")
        return redirect(url_for("dep.show_departments"))
    if request.method == "GET":
        # Fill the form with current value.
        form.name.data = department.name

    return render_template(
        "add_department.html", title="Update department",
        form=form, legend=f"Update {department.name}"
    )


@dep.route("/department/<int:department_id>/delete", methods=["POST"])
def delete_department(department_id):
    """Delete department with a given id"""
    department = Department.query.get_or_404(department_id)
    try:
        db.session.delete(department)
        db.session.commit()
    except IntegrityError:
        # If department has employees handle an exception.
        flash("Department that has employees cannot be deleted!", "danger")
        return redirect(url_for("dep.show_departments"))
    else:
        # Redirect to departments page with success message.
        flash("Department has been deleted!", "success")
        return redirect(url_for("dep.show_departments"))
