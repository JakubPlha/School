CREATE DATABASE mrazak;
USE mrazak;

CREATE TABLE kategorie (
    id_kategorie INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE polozka (
    id_polozky INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(100) NOT NULL,
    datum_expirace DATE NOT NULL,
    pocet_kusu INT NOT NULL,
    id_kategorie INT NOT NULL,

    CONSTRAINT chk_expirace
        CHECK (datum_expirace >= CURRENT_DATE),

    CONSTRAINT chk_pocet
        CHECK (pocet_kusu > 0),

    CONSTRAINT fk_kategorie
        FOREIGN KEY (id_kategorie)
        REFERENCES kategorie(id_kategorie)
);
