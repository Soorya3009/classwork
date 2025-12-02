1
CREATE DATABASE GroceryShop;

2
USE GroceryShop;

3
CREATE TABLE products (product_id INT PRIMARY KEY,product_name VARCHAR(100),price DECIMAL(10,2));

4
ALTER TABLE products ADD category VARCHAR(50);

5
DELETE FROM products;

6
DROP DATABASE GroceryShop;