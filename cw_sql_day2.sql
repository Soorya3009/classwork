-- You are helping manage a student information table in a college database. The table is named students and contains the following columns:
-- id (number)
-- name (text)
-- age (number)
-- department (text)
-- grade (number)
-- Your task is to:
-- Insert 4 student records into the students table using realistic data.
-- Write a query to display all students whose age is greater than 20.
-- Write a query to display all students in the 'Computer Science' or 'Physics' departments.
-- Write a query to show the student who has the grade exactly equal to 90.
-- Write a query to find students whose grades are between 70 and 90.


1)
INSERT INTO students VALUES('01','Soorya','23','Computer science','74'); 

2)
INSERT INTO students (id,name,age,department,grade)
VALUES ('02','Adithya','19','physics','88'), 
       ('03','Ashwin','18','Maths','90'),
       ('04','Arya','23','Computer science','75');

3)
SELECT * FROM students WHERE age > 20;

4)
SELECT * FROM students WHERE department='Computer science' OR department='Physics';

5)
SELECT * FROM students WHERE grade=90;

6)
SELECT * FROM students WHERE grade BETWEEN 70 AND 90;