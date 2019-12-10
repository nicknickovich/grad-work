from flask import render_template, url_for, redirect, flash
from department_app.models import Employee, Department
from department_app import db, app
from department_app.forms import AddDepartmentForm


@app.route("/")
def home():
    return render_template("home.html", title="EMS Home")


@app.route("/employees")
def show_employees():
    employees = Employee.query.order_by(Employee.id).all()
    return render_template("employees.html", employees=employees,
                            title="All employees")


@app.route("/departments")
def show_departments():
    departments = Department.query.order_by(Department.id).all()
    return render_template("departments.html", departments=departments,
                            title="All departments")


@app.route("/add_department", methods=["GET", "POST"])
def add_department():
    form = AddDepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data)
        db.session.add(department)
        db.session.commit()
        flash("Post has been created!", "success")
        return redirect(url_for("show_departments"))

    return render_template(
        "add_department.html", title="Add new department",
        form=form, legend="New Department"
    )
