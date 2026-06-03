CREATE TABLE IF NOT EXISTS osoby (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jmeno TEXT NOT NULL,
    prijmeni TEXT NOT NULL,
    rodne_cislo TEXT NOT NULL UNIQUE,
    ulice TEXT NOT NULL,
    cislo_popisne TEXT NOT NULL,
    psc TEXT NOT NULL,
    mesto TEXT NOT NULL
);
