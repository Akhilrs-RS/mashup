CREATE DATABASE CompanyDB;
USE CompanyDB;
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
CREATE TABLE departments (
    emp_id INT,
    department_name VARCHAR(100)
);
INSERT INTO employees (id, name) VALUES
(1, 'Anjali'),
(2, 'Rohan'),
(3, 'Meena');

INSERT INTO departments (emp_id, department_name) VALUES
(1, 'HR'),
(2, 'IT'),
(4, 'Finance');
SELECT e.id, e.name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.id = d.emp_id;
SELECT e.id, e.name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.id = d.emp_id;
SELECT e.id, e.name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.id = d.emp_id;