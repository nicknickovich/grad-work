## Department App

A simple app that allows you to manage departments and employees.

# Homepage
At the homepage a welcome message is presented with links to departments and employees pages.

# Departments
At the departments page a table with all current departments is presented. In the table you can see names of departments and average salary of department's employees.
* You can add a new department by clicking "New department" button which takes you to a form for creating a new department.
* You can update a department by clicking "Update" button to the right of the department record.
* Clicking on a department's name takes you to this department's page. Here you can see information about the department and you also have options to update and delete it. Keep in mind that department which have employees cannot be deleted.

# Employees
At the employees page a table with all current employees is presented. In the table you can see employees' names, dates of birth, salaries and department they belong to.
* You can add a new employee by clicking "New employee" button and filling out the form for a new employee.
* You can update an employee's information by clicking "Update" button to the right of the employee record.
* You can search employees by date of birth. Click "Search employees" button and fill "from" and "to" date in the form. Search results will be presented in a new table.
* Clicking on an employee's name takes you to this employee's page. Here you can see information about the employee and you also have options to update and delete this record.

# API
CRUD operations are available for departments and employees.

Departments:
- GET /department - gets a list of all departments;
- GET /department/\<department_id\> - gets a department with a given id;
- POST /department - creates a department from provided json data;
- PUT /department/\<department_id> - update a department with provided id using json data;
- DELETE /department/\<department_id> - delete a department with provided id;

Employees:
- GET /employee - gets a list of all employees;
- GET /employee/\<employee_id\> - gets an employee with a given id;
- POST /employee - creates a employee from provided json data;
- PUT /employee/\<employee_id> - update an employee with provided id using json data;
- DELETE /employee/\<employee_id> - delete an employee with provided id; 