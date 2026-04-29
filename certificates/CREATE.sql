CREATE DATABASE certifikaty_db;
USE certifikaty_db;

CREATE TABLE clients (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(40) NOT NULL,
    lastname VARCHAR(60) NOT NULL,
    birthdate DATE NOT NULL,
    street VARCHAR(40) NOT NULL,
    housenum VARCHAR(10),
    postal VARCHAR(5),
    city VARCHAR(40),
    username VARCHAR(20) NOT NULL,
    password VARCHAR(28) NOT NULL,
    email VARCHAR(128) NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE certificates (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    clients_id INT UNSIGNED NOT NULL,
    certifkey VARCHAR(16) NOT NULL UNIQUE,
    FOREIGN KEY (clients_id) REFERENCES clients(id)
);

INSERT INTO clients (firstname, lastname, birthdate, street, housenum, postal, city, username, password, email, phone) VALUES
('Jan', 'Novák', '1998-04-12', 'Jabloňová', '15', '11000', 'Praha', 'jnovak', 'heslo123', 'jan.novak@email.cz', '+420777123456'),
('Eva', 'Bagrová', '1995-09-30', 'Lipová', '8A', '60200', 'Brno', 'ebagrova', 'tajne456', 'eva.ba@email.cz', '+420776987654'),
('Petr', 'Maják', '2001-01-18', 'Nádražní', '22', '70030', 'Rumburk', 'pmajak', 'abc789', 'petr.m@email.cz', '+420775111222');

INSERT INTO certificates (clients_id, certifkey) VALUES
(1, 'ABCD1234EFGH5678'),
(1, 'ZXCV9876QWER5432'),
(2, 'LMNO4567PQRS8901'),
(3, 'TYUI1122GHJK3344');