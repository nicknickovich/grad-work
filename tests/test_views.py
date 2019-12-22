"""
    General tests for view functions.
"""


def test_home_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200


def test_departments_page(test_client, init_database):
    response = test_client.get("/departments")
    assert response.status_code == 200
    assert b"Python" in response.data
    assert b"Java" in response.data


def test_employees_page(test_client, init_database):
    response = test_client.get("/employees")
    assert response.status_code == 200
    assert b"John Smith" in response.data
    assert b"Jane Doe" in response.data


def test_one_department_page(test_client, init_database):
    response = test_client.get("/department/1")
    assert response.status_code == 200
    assert b"Python" in response.data


def test_one_employee_page(test_client, init_database):
    response = test_client.get("/employee/1")
    assert response.status_code == 200
    assert b"John Smith" in response.data


def test_add_department_page(test_client, init_database):
    response = test_client.get("/add_department")
    assert response.status_code == 200


def test_add_employee_page(test_client, init_database):
    response = test_client.get("/add_employee")
    assert response.status_code == 200


def test_delete_department_whithout_employees(test_client, init_database):
    test_client.post("/department/3/delete")
    response = test_client.get("/departments")
    assert b"Ruby" not in response.data
    assert b"Java" in response.data


def test_delete_employee(test_client, init_database):
    test_client.post("/employee/1/delete")
    response = test_client.get("/employees")
    assert b"John Smith" not in response.data
    assert b"Jane Doe" in response.data