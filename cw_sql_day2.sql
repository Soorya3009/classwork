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