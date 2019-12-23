# -*- coding: utf-8 -*-
"""
    department_app.api_v2.views
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Version 2 of REST API.
    Created with Flask-RESTful.


    - GET /api_v2/employee: retrieve all employees;
    - GET /api_v2/employee/<id>: retrieve employee with a given id;
    - POST /api_v2/employee: add new employee;
    - PUT /api_v2/employee/<id>: update employee with a given id;
    - DELETE /api_v2/employee/<id>: delete employee with a given id;

    - GET /api_v2/department: retrieve all departments;
    - GET /api_v2/department/<id>: retrieve department with a given id;
    - POST /api_v2/department: add new department;
    - PUT /api_v2/department/<id>: update department with a given id;
    - DELETE /api_v2/department/<id>: delete department with a given id;
"""

from flask import Blueprint, request
from flask_restful import Resource
from department_app.models import Employee, Department
from department_app import db, api_restful
from department_app.api.schema import (employee_schema, employees_schema,
                                       department_schema, departments_schema)


api_v2 = Blueprint("api_v2", __name__)


class EmployeeApi(Resource):
    def get(self, employee_id=None):
        if employee_id is None:
            all_employees = Employee.query.all()
            return employees_schema.dump(all_employees)
        else:
            employee = Employee.query.get_or_404(employee_id)
            return employee_schema.dump(employee)

    def post(self, employee_id=None):
        name = request.json["name"]
        date_of_birth = request.json["date_of_birth"]
        salary = request.json["salary"]
        department_id = request.json["department_id"]

        new_employee = Employee(
            name=name, 
            date_of_birth=date_of_birth, 
            salary=salary, 
            department_id=department_id
        )
        db.session.add(new_employee)
        db.session.commit()

        return employee_schema.dump(new_employee), 201

    def put(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)
        # Get attributes for an employee from json.
        name = request.json["name"]
        date_of_birth = request.json["date_of_birth"]
        salary = request.json["salary"]
        department_id = request.json["department_id"]
        # Set new values for attributes.
        employee.name = name
        employee.date_of_birth = date_of_birth
        employee.salary = salary
        employee.department_id = department_id

        db.session.commit()

        return employee_schema.dump(employee)

    def delete(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()

        return employee_schema.dump(employee)


api_restful.add_resource(EmployeeApi,
                         "/api_v2/employee",
                         "/api_v2/employee/<employee_id>")


class DepartmentApi(Resource):
    def get(self, department_id=None):
        if department_id is None:
            all_departments = Department.query.all()
            return departments_schema.dump(all_departments)
        else:
            department = Department.query.get_or_404(department_id)
            return department_schema.dump(department)

    def post(self, department_id=None):
        name = request.json["name"]

        new_department = Department(name=name)
        db.session.add(new_department)
        db.session.commit()

        return department_schema.dump(new_department), 201

    def put(self, department_id):
        department = Department.query.get_or_404(department_id)
        # Get attributes for a department from json.
        name = request.json["name"]
        # Set new values for attributes.
        department.name = name
        db.session.commit()

        return department_schema.dump(department)

    def delete(self, department_id):
        department = Department.query.get_or_404(department_id)
        db.session.delete(department)
        db.session.commit()

        return department_schema.dump(department)


api_restful.add_resource(DepartmentApi,
                         "/api_v2/department",
                         "/api_v2/department/<department_id>")
