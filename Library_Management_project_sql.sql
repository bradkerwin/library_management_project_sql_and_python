CREATE DATABASE Library_Management;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(75) NOT NULL,
    availability VARCHAR(50) DEFAULT 'available' NOT NULL    
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO users (user_name, email, phone)
VALUES ('Mark Hoppus', 'markh@gmail.com', '123-456-7890'),
('Tom DeLonge', 'tdelonge@yahoo.com', '098-765-4321'),
('Travis Barker', 'travisbarker1999@email.com', '111-222-3345');

INSERT INTO books (title, author)
VALUES ('The Great Gatsby', 'F. Scott Fitzgerald'),
('The Outsiders', 'S.E. Hinton'),
('The TB12 Method: How to Achieve a Lifetime of Sustained Peak Performance', 'Tom Brady');

-- SELECT * FROM books;
-- SELECT * FROM users;