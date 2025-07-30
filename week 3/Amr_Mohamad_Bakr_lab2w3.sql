-- =================================== Task 1: Advanced Queries with JOINs ===================================

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

CREATE TABLE registrations (
    student_id INT REFERENCES students(id),
    course_id INT REFERENCES courses(id),
    registration_date DATE NOT NULL,
    PRIMARY KEY (student_id, course_id)
);

SELECT students.name AS student_name, courses.course_name
FROM students
JOIN registrations ON students.id = registrations.student_id
JOIN courses ON courses.id = registrations.course_id;


-- ==================================== Task 2: Data Normalization ====================================

CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_name VARCHAR(100) NOT NULL,
    publisher_name VARCHAR(100) NOT NULL
);

CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE publishers (
    publisher_id SERIAL PRIMARY KEY,
    publisher_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT REFERENCES authors(author_id),
    publisher_id INT REFERENCES publishers(publisher_id)
);

INSERT INTO authors (author_name) VALUES ('Author A'), ('Author B');

INSERT INTO publishers (publisher_name) VALUES ('Publisher X'), ('Publisher Y');

INSERT INTO books (title, author_id, publisher_id) 
VALUES ('Book 1', 1, 1), ('Book 2', 2, 2);


-- =========================== Task 3: Design a Simple Database ================================

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address TEXT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2),
    stock INT
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE
);

CREATE TABLE order_details (
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    price DECIMAL(10, 2),
    PRIMARY KEY (order_id, product_id)
);
