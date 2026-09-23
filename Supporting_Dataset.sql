CREATE DATABASE IF NOT EXISTS empolyee;

USE empolyee;

CREATE TABLE IF NOT EXISTS employee_db (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(45),
    department VARCHAR(45),
    salary FLOAT
);

INSERT INTO employee_db
(emp_id, emp_name, department, salary)
VALUES
(101, 'Rahul', 'IT', 45000),
(102, 'Priya', 'HR', 38000),
(103, 'Amit', 'IT', 52000),
(104, 'Sneha', 'Sales', 42000),
(105, 'Rohit', 'Sales', 48000),
(106, 'Neha', 'HR', 40000);