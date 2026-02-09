CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
INSERT OR REPLACE INTO students (id, name, age) VALUES 
    (1, 'Иван', 20),
    (2, 'Мария', 22),
    (3, 'Петр', 19);
SELECT * FROM students;
SELECT 'ID: ' | id | ' | Имя: ' | name | ' | Возраст: ' || age AS cтуденты 
FROM students;

CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL NOT NULL
);

INSERT OR REPLACE INTO employees (id, name, position, salary) VALUES 
    (1, 'Анна', 'Разработчик', 50000),
    (2, 'Олег', 'Менеджер', 60000),
    (3, 'Елена', 'Дизайнер', 45000);
SELECT 'Исходные данные:' AS Инфо;
SELECT * FROM employees;
UPDATE employees 
SET salary = 65000 
WHERE id = 2;
SELECT 'New data:' AS Инфо;
SELECT * FROM employees;
SELECT  'ID: ' || id ||  ' | Имя: ' || name ||  ' | Должность: ' |position |  ' | Зарплата: ' | salary | ' Р' AS Сотрудники
FROM employees;