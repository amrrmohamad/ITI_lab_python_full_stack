CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO students (name, email) VALUES
('Amr Mohamad', 'amr@example.com'), 
('Ali Karam', 'ali@example.com'), 
('Mohamad Ahmed', 'mohamad@example.com'), 
('sayed Abdo', 'sayed@example.com'),
('Mostafa Khaled', 'mostafa@example.com');

SELECT * FROM students;

SELECT name, email FROM students;

SELECT * FROM students WHERE name LIKE 'A%';

SELECT * FROM students ORDER BY email ASC;
