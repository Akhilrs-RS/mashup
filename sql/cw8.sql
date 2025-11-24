CREATE DATABASE GroceryShop;
USE GroceryShop;
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);
INSERT INTO products (product_id, product_name, price, category)
VALUES 
(1, 'Rice', 45.00, 'Grains'),
(2, 'Sugar', 42.50, 'Essentials'),
(3, 'Milk', 28.00, 'Dairy'),
(4, 'Tea Powder', 120.00, 'Beverages'),
(5, 'Bread', 35.00, 'Bakery');
ALTER TABLE products
ADD COLUMN category VARCHAR(50);
TRUNCATE TABLE products;
DROP DATABASE GroceryShop;