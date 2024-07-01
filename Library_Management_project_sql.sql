CREATE DATABASE Library_Management;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(75) NOT NULL,
    availability BOOLEAN DEFAULT 1    
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO users (name, email, phone)
VALUES ('Mark Hoppus', 'markh@gmail.com', '123-456-7890'),
('Tom DeLonge', 'tdelonge@yahoo.com', '098-765-4321'),
('Travis Barker', 'travisbarker1999@email.com', '111-222-3345');

INSERT INTO books (id, title, author, availability)
VALUES ('101', 'The Great Gatsby', 'F. Scott Fitzgerald', 1),
('102', 'The Outsiders', 'S.E. Hinton', 1),
('103', 'The TB12 Method: How to Achieve a Lifetime of Sustained Peak Performance', 'Tom Brady', 1);

-- SELECT * FROM users;