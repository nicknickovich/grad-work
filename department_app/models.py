from department_app import db


class Employee(db.Model):
    """Model for an employee"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"), nullable=False)
    department = db.relationship("Department", backref="department", lazy=True)


    def __init__(self, name, date_of_birth, salary, department_id):
        self.name = name
        self.date_of_birth = date_of_birth
        self.salary = salary
        self.department_id = department_id


    def __repr__(self):
        return f"""
Employee('{self.id}', 
         '{self.name}', 
         '{self.salary}',
         '{self.date_of_birth}',
         '{self.department}')"""


class Department(db.Model):
    """Model for a department"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f"Department('{self.name}')"
