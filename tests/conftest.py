"""
    Fixtures that create separate instance of an app and database.
"""

import datetime
import pytest
from department_app import create_app, db
from department_app.models import Employee, Department


@pytest.fixture(scope="module")
def test_client():
    """Create an instance of an app.  Add it to context.
    Run tests and then delete app from context.
    """
    # Create app with test configuration.
    app = create_app("testconfig.py")

    # Test client provided by Flask
    testing_client = app.test_client()

    # Establish an app context.
    ctx = app.app_context()
    ctx.push()

    yield testing_client

    # Remove app context.
    ctx.pop()


@pytest.fixture(scope="module")
def init_database():
    """Create an instance of a database and populate it with test data.
    Run tests and then delete test data.
    """
    db.create_all()

    # Add departments to db.
    department1 = Department(name="Python")
    department2 = Department(name="Java")
    department3 = Department(name="Ruby")
    db.session.add(department1)
    db.session.add(department2)
    db.session.add(department3)
    db.session.commit()

    # Add employees to db.
    employee1 = Employee(
        id=1,
        name="John Smith",
        date_of_birth=datetime.datetime(1999, 1, 1),
        salary=40000.0,
        department_id = 1
    )

    employee2 = Employee(
        id=2,
        name="Jane Doe",
        date_of_birth=datetime.datetime(1985, 12, 31),
        salary=50000.0,
        department_id = 2
    )

    db.session.add(employee1)
    db.session.add(employee2)
    db.session.commit()

    yield db

    # Delete everything from db.
    db.drop_all()