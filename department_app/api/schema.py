from department_app import ma


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ("name", "date_of_birth", "salary", "department_id")

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


class DepartmentSchema(ma.Schema):
    class Meta:
        fields = ("name",)

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)
