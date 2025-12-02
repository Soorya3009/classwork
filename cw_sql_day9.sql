CREATE DATABASE LibraryDB;

USE LibraryDB;

CREATE TABLE book (book_id INT,title VARCHAR(100));

CREATE TABLE borrowers (borrower_id INT,name VARCHAR(100),book_id INT);

INSERT INTO books (book_id, title) VALUES
(1, 'The Alchemist'),
(2, 'The Power of Now'),
(3, 'Think and Grow Rich'),
(4, 'Clean Code');

INSERT INTO borrowers (borrower_id, name, book_id) VALUES
(101, 'Alice', 1),
(102, 'Bob', 2),
(103, 'Charlie', NULL);

1
SELECT books.title, borrowers.name AS borrowed_by FROM books LEFT JOIN borrowers ON books.book_id = borrowers.book_id;

2
SELECT borrowers.name, books.title FROM borrowers LEFT JOIN books ON borrowers.book_id = books.book_id;

3
SELECT books.title FROM books LEFT JOIN borrowers ON books.book_id = borrowers.book_id WHERE borrowers.book_id IS NULL;

4
SELECT borrowers.name, books.title FROM borrowers LEFT JOIN books ON borrowers.book_id = books.book_id;