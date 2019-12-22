from department_app.models import Employee, Department


def test_new_employee():
    employee = Employee(
        id=1,
        name="John Smith",
        date_of_birth="1999-1-1",
        salary=40000.0,
        department_id = 1
    )
    assert employee.id == 1
    assert employee.name == "John Smith"
    assert employee.date_of_birth == "1999-1-1"
    assert employee.salary == 40000.0
    assert employee.department_id == 1


def test_new_department():
    department = Department(
        id=1,
        name="Python Web Development"
    )
    assert department.id == 1
    assert department.name == "Python Web Development"
