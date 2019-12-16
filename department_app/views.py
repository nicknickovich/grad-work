from flask import render_template, url_for, redirect, request, flash
from sqlalchemy.exc import IntegrityError
from department_app.models import Employee, Department
from department_app import db, app
from department_app.forms import DepartmentForm, EmployeeForm, SearchForm



@app.route("/")
def home():
    """Render home page"""
    return render_template("home.html", title="Home")


@app.route("/employees")
def show_employees():
    """Render a list of all employees"""
    employees = Employee.query.order_by(Employee.id).all()
    return render_template("employees.html", employees=employees,
                           title="All employees")


@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():
    """Add a new employee using a form."""
    form = EmployeeForm()

    if form.validate_on_submit():
        # Create new Employee with values from the form.
        employee = Employee(
            name=form.name.data,
            date_of_birth=form.date_of_birth.data,
            salary=form.salary.data,
            department_id=form.department_id.data,
        )
        db.session.add(employee)
        db.session.commit()
        flash("Employee has been added!", "success")
        return redirect(url_for("show_employees"))

    return render_template(
        "add_employee.html", title="Add new employee",
        form=form, legend="New Employee"
    )


@app.route("/employee/<int:employee_id>")
def show_employee(employee_id):
    """Render page of an employee with a given id"""
    employee = Employee.query.get_or_404(employee_id)
    return render_template(
        "employee.html", title=employee.name, employee=employee
    )


@app.route("/employee/<int:employee_id>/update", methods=["GET", "POST"])
def update_employee(employee_id):
    """Render page on which you can update information about an
    employee with a given id.
    """
    employee = Employee.query.get_or_404(employee_id)
    form = EmployeeForm()

    if form.validate_on_submit():
        # Set employee attributes to values from the form.
        employee.name = form.name.data
        employee.date_of_birth = form.date_of_birth.data
        employee.salary = form.salary.data
        employee.department_id = form.department_id.data
        db.session.commit()
        flash("Employee has been updated!", "success")
        return redirect(url_for("show_employees"))
    if request.method == "GET":
        # Fill the form with current values.
        form.name.data = employee.name
        form.date_of_birth.data = employee.date_of_birth
        form.salary.data = employee.salary
        form.department_id.data = employee.department_id

    return render_template(
        "add_employee.html", title="Update employee",
        form=form, legend=f"Update {employee.name}"
    )


@app.route("/employee/<int:employee_id>/delete", methods=["POST"])
def delete_employee(employee_id):
    """Delete employee with a given id"""
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    flash("Employee has been deleted!", "success")
    return redirect(url_for("show_employees"))


@app.route("/search_employees", methods=["GET", "POST"])
def search_employees():
    """Search employees by date of birth."""
    form = SearchForm()
    if form.validate_on_submit():
        employees = Employee.query\
            .filter(form.from_date.data <= Employee.date_of_birth,
                    Employee.date_of_birth <= form.to_date.data).all()
        return render_template("employees.html", employees=employees,
                               title="Search results")
    return render_template(
        "search_employees.html", title="Search employees", form=form,
        legend="Search employees by date of birth"
    )


@app.route("/departments")
def show_departments():
    """Render a list of all departments"""
    departments = Department.query.order_by(Department.id).all()
    employees = Employee.query.all()

    # Get information about all employees' salaries
    # and departments they belong to.
    salaries_info = {}
    for employee in employees:
        if employee.department_id in salaries_info:
            salaries_info[employee.department_id]["total"] += employee.salary
            salaries_info[employee.department_id]["count"] += 1
        else:
            salaries_info.update(
                {
                    employee.department_id: {
                        "total": employee.salary,
                        "count": 1,
                    }
                }
            )

    # Calculate average salaries for all departments
    # and store them in a dictionary.
    avg_salaries = {}
    for department in departments:
        if department.id in salaries_info:
            # If department has employees.
            avg_salaries[department.id] = (
                round(salaries_info[department.id]["total"]
                      / salaries_info[department.id]["count"], 2)
            )
        else:
            # Department has no employees.
            avg_salaries[department.id] = 0

    return render_template(
        "departments.html", departments=departments,
        avg_salaries=avg_salaries, title="All departments"
    )


@app.route("/add_department", methods=["GET", "POST"])
def add_department():
    """Add a new department using a form."""
    form = DepartmentForm()

    if form.validate_on_submit():
        # Set department name to a value from the form.
        department = Department(name=form.name.data)
        db.session.add(department)
        db.session.commit()
        flash("Department has been added!", "success")
        return redirect(url_for("show_departments"))

    return render_template(
        "add_department.html", title="Add new department",
        form=form, legend="New Department"
    )


@app.route("/department/<int:department_id>")
def show_department(department_id):
    """Render page of a department with a given id"""
    department = Department.query.get_or_404(department_id)
    return render_template(
        "department.html", title=department.name, department=department
    )


@app.route("/department/<int:department_id>/update", methods=["GET", "POST"])
def update_department(department_id):
    """Delete department with a given id"""
    department = Department.query.get_or_404(department_id)
    form = DepartmentForm()

    if form.validate_on_submit():
        # Set department name to a value from the form.
        department.name = form.name.data
        db.session.commit()
        flash("Department has been updated!", "success")
        return redirect(url_for("show_departments"))
    if request.method == "GET":
        # Fill the form with current value.
        form.name.data = department.name

    return render_template(
        "add_department.html", title="Update department",
        form=form, legend=f"Update {department.name}"
    )


@app.route("/department/<int:department_id>/delete", methods=["POST"])
def delete_department(department_id):
    """Delete department with a given id"""
    department = Department.query.get_or_404(department_id)
    try:
        db.session.delete(department)
        db.session.commit()
    except IntegrityError:
        # If department has employees handle an exception.
        flash("Department that has employees cannot be deleted!", "danger")
        return redirect(url_for("show_departments"))
    else:
        # Redirect to departments page with success message.
        flash("Department has been deleted!", "success")
        return redirect(url_for("show_departments"))
