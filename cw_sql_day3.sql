-- You are helping an online store manager view product details from a products table. The table contains the following columns:
-- id (number)
-- name (text)
-- category (text)
-- price (number)
-- in_stock (text, either 'Yes' or 'No')
-- Your task is to:
-- Show all the unique product categories available in the table.
-- Select all products that are in stock and have a price less than 500.
-- Select all products that are not in stock or have a price greater than 1000.
-- Show the names and prices of all products, and sort the results by price from highest to lowest.
-- Display the name and an expression showing the price with 18% tax added (label it as price_with_tax).


INSERT INTO hw_products (id,name,category,price,in_stock)VALUES("1","Bluetooth Speaker","Electronics","750","Yes"),
("2","T-shirt","Clothing","450","Yes"),
("3","Laptop","Electronics","55000","No"),
("4","Coffee Mug","Kitchen Ware","250","Yes"),
("5","Chair","Furniture","3200","No"),
("6","Notebook","Stationary","120","Yes"),
("7","Smart watch","Electronics","4800","Yes"),
("8","Dinning table","Furniture","12500","No"),
("9","Waterbottle","Kitchen Ware","300","Yes"),
("10","Headphone","Electronics","950","Yes");

1)
SELECT DISTINCT category from hw_products;

2)
SELECT * FROM hw_products WHERE in_stock="Yes" AND price <500;

3)
SELECT * FROM hw_products WHERE in_stock="No" OR price>1000;

4)
SELECT name,price from hw_products ORDER BY price DESC;

5)
SELECT name, price * 1.18 AS price_with_tax FROM hw_products;
