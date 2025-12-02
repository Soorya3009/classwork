1
INSERT INTO studentsonline (id, name, course, score, email, phone, city, bonus_points) VALUES
(1, 'Asha', 'Python', 85, 'asha@mail.com', '9876543210', 'Chennai', 5),
(2, 'Ravi', 'Python', 90, 'ravi@mail.com', '9876543211', 'Chennai', NULL),
(3, 'Sneha', 'Java', 78, 'sneha@mail.com', '9876543212', 'Mumbai', NULL),
(4, 'Karan', 'Java', 88, 'karan@mail.com', '9876543213', 'Delhi', 2),
(5, 'Divya', 'Python', 95, 'divya@mail.com', '9876543214', 'Mumbai', 4),
(6, 'Manoj', 'JavaScript', 72, 'manoj@mail.com', '9876543215', 'Delhi', NULL);

2
SELECT course, COUNT(id) AS total_students FROM studentsonline GROUP BY course;

3
SELECT course, AVG(score) AS average_score FROM studentsonline GROUP BY course HAVING AVG(score) > 80;

4
SELECT name, score FROM studentsonline WHERE city IN ('Chennai', 'Mumbai');

5
SELECT * FROM studentsonline WHERE bonus_points IS NULL;

6
SELECT name FROM studentsonline WHERE city = 'Chennai' UNION SELECT name FROM studentsonline WHERE city = 'Mumbai';