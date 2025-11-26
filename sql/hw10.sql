CREATE DATABASE OnlineBookStore;
USE OnlineBookStore;
CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
INSERT INTO authors (author_id, name, email) VALUES
(1, 'Chetan Bhagat', 'chetan@example.com'),
(2, 'J.K. Rowling', 'jkrowling@example.com'),
(3, 'George R.R. Martin', 'george@example.com');
INSERT INTO books (book_id, title, author_id) VALUES
(101, '2 States', 1),
(102, 'Harry Potter and the Philosopher''s Stone', 2),
(103, 'A Game of Thrones', 3),
(104, 'Half Girlfriend', 1);