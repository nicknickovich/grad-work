"""
    Tests for CRUD functionality of API.
"""

# ========= Department Tests ==========

def test_api_return_all_departments(test_client, init_database):
    response = test_client.get("/api/department")
    assert response.json == [
        {
            "id": 1,
            "name": "Python"
        },
        {
            "id": 2,
            "name": "Java"
        },
        {
            "id": 3,
            "name": "Ruby"
        }
    ]


def test_api_return_one_department(test_client, init_database):
    response = test_client.get("/api/department/1")
    assert response.json == {
        "id": 1,
        "name": "Python"
    }


def test_api_add_new_department(test_client, init_database):
    new_department = {
        "id": 4,
        "name": "JavaScript"
    }
    test_client.post("/api/department", json=new_department)
    response = test_client.get("api/department")
    assert new_department in response.json


def test_api_update_department(test_client, init_database):
    updated_department = {
        "id": 1,
        "name": "Python Development"
    }
    test_client.put("/api/department/1", json=updated_department)
    response = test_client.get("api/department/1")
    assert response.json == updated_department


def test_api_delete_department(test_client, init_database):
    department_to_delete = test_client.get("api/employee/3").json
    test_client.delete("api/department/3")
    response = test_client.get("/api/department")
    assert department_to_delete not in response.json


# ============== Employee Tests ==============

def test_api_return_all_employees(test_client, init_database):
    response = test_client.get("/api/employee")
    assert response.json == [
        {
            "id": 1,
            "name": "John Smith",
            "date_of_birth": "1999-01-01T00:00:00",
            "salary": 40000.0,
            "department_id": 1
        },
        {
            "id": 2,
            "name": "Jane Doe",
            "date_of_birth": "1985-12-31T00:00:00",
            "salary": 50000.0,
            "department_id": 2
        }
    ]


def test_api_return_one_employee(test_client, init_database):
    response = test_client.get("/api/employee/1")
    assert response.json == {
        "id": 1,
        "name": "John Smith",
        "date_of_birth": "1999-01-01T00:00:00",
        "salary": 40000.0,
        "department_id": 1
    }


def test_api_add_new_employee(test_client, init_database):
    new_employee = {
        "id": 3,
        "name": "Kate White",
        "date_of_birth": "1983-12-12T00:00:00",
        "salary": 60000.0,
        "department_id": 1
    }
    test_client.post("/api/employee", json=new_employee)
    response = test_client.get("api/employee/3")
    assert new_employee == response.json


def test_api_update_employee(test_client, init_database):
    updated_employee = {
        "id": 2,
        "name": "Jane Doe",
        "date_of_birth": "1985-12-31T00:00:00",
        "salary": 85000.0,
        "department_id": 1
    }
    test_client.put("/api/employee/2", json=updated_employee)
    response = test_client.get("api/employee/2")
    assert response.json == updated_employee


def test_api_delete_employee(test_client, init_database):
    employee_to_delete = test_client.get("api/employee/1").json
    test_client.delete("api/employee/1")
    response = test_client.get("/api/employee")
    assert employee_to_delete not in response.json
