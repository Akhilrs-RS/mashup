INSERT INTO products (id, name, category, price, in_stock) VALUES
(1, 'Wireless Mouse', 'Electronics', 450, 'Yes'),
(2, 'Bluetooth Headphones', 'Electronics', 1200, 'No'),
(3, 'Office Chair', 'Furniture', 3500, 'Yes'),
(4, 'Water Bottle', 'Accessories', 250, 'Yes'),
(5, 'Laptop Stand', 'Electronics', 800, 'No');
SELECT DISTINCT category
FROM products;
SELECT *
FROM products
WHERE in_stock = 'Yes' AND price < 500;
SELECT *
FROM products
WHERE in_stock = 'No' OR price > 1000;
SELECT name, price
FROM products
ORDER BY price DESC;
SELECT 
    name,
    price,
    price * 1.18 AS price_with_tax
FROM products;