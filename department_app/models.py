from app import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"), nullable=False)
    department_name = db.relationship("Department", backref="department", lazy=True)


    def __repr__(self):
        return f"""
Employee('{self.id}', 
         '{self.name}', 
         '{self.salary}',
         '{self.date_of_birth}',
         '{self.department_name})"""


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    
    def __repr__(self):
        return f"Department('{self.name}', '{self.head}')"

