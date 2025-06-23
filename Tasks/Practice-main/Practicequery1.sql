CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT,
    hire_date DATE
);

INSERT INTO employees (emp_id, emp_name, dept_id, salary, hire_date) VALUES
(1, 'Alice', 10, 60000, '2020-01-15'),
(2, 'Bob', 20, 75000, '2019-03-10'),
(3, 'Charlie', 10, 55000, '2021-06-20'),
(4, 'Dave', 20, 80000, '2018-09-05'),
(5, 'Eve', 30, 50000, '2022-02-10');

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO departments (dept_id, dept_name, location) VALUES
(10, 'HR', 'New York'),
(20, 'IT', 'Boston'),
(30, 'Finance', 'Chicago');

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    emp_id INT,
    project_name VARCHAR(50),
    start_date DATE,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

INSERT INTO projects (project_id, emp_id, project_name, start_date) VALUES
(101, 1, 'Project A', '2023-01-01'),
(102, 2, 'Project B', '2023-02-15'),
(103, 1, 'Project C', '2023-03-10'),
(104, 3, 'Project D', '2023-04-01');


SELECT e.emp_id, e.emp_name, e.salary, e.dept_id
FROM employees e
JOIN (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_id
) dept_avg ON e.dept_id = dept_avg.dept_id
WHERE e.salary > dept_avg.avg_salary;

SELECT e.emp_id, e.emp_name
FROM employees e
WHERE NOT EXISTS (
    SELECT p.project_id
    FROM employees e2
    JOIN projects p ON p.emp_id = e2.emp_id
    WHERE e2.dept_id = e.dept_id
    AND p.project_id NOT IN (
        SELECT p2.project_id FROM projects p2 WHERE p2.emp_id = e.emp_id
    )
);


SELECT emp_id, emp_name, dept_id, salary
FROM employees
WHERE hire_date > '2020-12-31'
AND (dept_id, salary) IN (
    SELECT dept_id, MAX(salary)
    FROM employees
    WHERE hire_date > '2020-12-31'
    GROUP BY dept_id
);


SELECT d.dept_id, d.dept_name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1 FROM employees e
    WHERE e.dept_id = d.dept_id AND e.salary <= 50000
);
