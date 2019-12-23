"""
    Tests for CRUD functionality of API_v2.
"""

# ========= Department Tests ==========

def test_api_return_all_departments(test_client, init_database):
    response = test_client.get("/api_v2/department")
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
    response = test_client.get("/api_v2/department/1")
    assert response.json == {
        "id": 1,
        "name": "Python"
    }


def test_api_add_new_department(test_client, init_database):
    new_department = {
        "id": 4,
        "name": "JavaScript"
    }
    test_client.post("/api_v2/department", json=new_department)
    response = test_client.get("api_v2/department")
    assert new_department in response.json


def test_api_update_department(test_client, init_database):
    updated_department = {
        "id": 1,
        "name": "Python Development"
    }
    test_client.put("/api_v2/department/1", json=updated_department)
    response = test_client.get("api_v2/department/1")
    assert response.json == updated_department


def test_api_delete_department(test_client, init_database):
    department_to_delete = test_client.get("api_v2/employee/3").json
    test_client.delete("api_v2/department/3")
    response = test_client.get("/api_v2/department")
    assert department_to_delete not in response.json


# ============== Employee Tests ==============

def test_api_return_all_employees(test_client, init_database):
    response = test_client.get("/api_v2/employee")
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
    response = test_client.get("/api_v2/employee/1")
    assert response.json == {
        "id": 1,
        "name": "John Smith",
        "date_of_birth": "1999-01-01T00:00:00",
        "salary": 40000.0,
        "department_id": 1
    }


def test_api_delete_employee(test_client, init_database):
    employee_to_delete = test_client.get("api_v2/employee/1").json
    test_client.delete("api_v2/employee/1")
    response = test_client.get("/api_v2/employee")
    assert employee_to_delete not in response.json
