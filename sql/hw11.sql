CREATE DATABASE SchoolLibrary;
USE SchoolLibrary;
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(200) NOT NULL,
    author VARCHAR(150),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
CREATE INDEX idx_book_name ON books(book_name);
INSERT INTO categories (category_name)
VALUES 
('Fiction'),
('Science'),
('History'),
('Technology');
INSERT INTO books (book_name, author, category_id)
VALUES
('The Time Machine', 'H. G. Wells', 1),
('A Brief History of Time', 'Stephen Hawking', 2),
('World War II Chronicles', 'John Keegan', 3),
('Introduction to Algorithms', 'Thomas H. Cormen', 4),
('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 1);
SHOW INDEXES FROM books;