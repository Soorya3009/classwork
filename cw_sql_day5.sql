-- You are managing a database for a mobile store. The table is called mobiles and contains the following columns:
-- id (number)
-- brand (text)
-- model (text)
-- price (number)
-- stock (number)
-- Perform the following tasks:
-- Insert the following mobile records into the table:
-- (1, 'Samsung', 'Galaxy M14', 12000, 30)
-- (2, 'Redmi', 'Note 12', 15000, 25)
-- (3, 'Realme', 'Narzo 50', 13000, 20)
-- (4, 'Samsung', 'Galaxy A23', 18000, 10)
-- Display all mobiles that cost more than 13000 or have stock less than 15.
-- Increase the stock by 5 and update the price to 12500 for the mobile with model = 'Narzo 50'.
-- Delete the mobile whose id is 2.
-- Find the lowest and highest price in the table.
-- Find the total stock of all mobiles in the table.
-- Show the top 2 most expensive mobiles.



1) INSERT INTO mobiles(ID,BRAND,MODEL,PRICE,STOCK)
    VALUES('1','Samsung','Galaxy M14','12000','30'),
	      ('2','Redmi','Note 12','15000','25'),
	      ('3','Realme','Narzo 50','13000','20'),
	      ('4','Samsung','Galaxy A23','18000','10');

2) SELECT * FROM mobiles WHERE PRICE > 13000 OR STOCK < 15;

3) UPDATE mobiles SET STOCK = STOCK + 5 , PRICE = '12500' WHERE MODEL = 'Narzo 50';

4) DELETE FROM mobiles WHERE ID = '2';

5) SELECT MIN(PRICE) AS LowestPrice, MAX(PRICE) AS HighestPrice FROM mobiles;

6) SELECT SUM(STOCK) AS TotalStock FROM mobiles;

7) SELECT * FROM mobiles ORDER BY PRICE DESC LIMIT 2;