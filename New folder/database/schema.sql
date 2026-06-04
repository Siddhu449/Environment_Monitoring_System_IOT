
CREATE DATABASE IF NOT EXISTS ai_quiz;
USE ai_quiz;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(255)
);

CREATE TABLE scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    subject VARCHAR(100),
    score INT,
    hint_count INT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (username, password) VALUES
('alice', 'pass123'),
('bob', 'pass456');

INSERT INTO scores (user_id, subject, score, hint_count) VALUES
(1, 'Python', 5, 1),
(2, 'HTML', 4, 0);
