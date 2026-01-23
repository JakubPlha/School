SELECT p.id_polozky, p.nazev, k.nazev AS kategorie,
       p.datum_expirace, p.pocet_kusu
FROM polozka p
JOIN kategorie k ON p.id_kategorie = k.id_kategorie;

INSERT INTO polozka (nazev, id_kategorie, datum_expirace, pocet_kusu)
VALUES ('Bageta', 5, '2026-03-01', 2);

UPDATE polozka
SET pocet_kusu = 5
WHERE id_polozky = 1;

UPDATE polozka
SET datum_expirace = '2026-04-01'
WHERE id_polozky = 2;

DELETE FROM polozka
WHERE id_polozky = 16;

SELECT p.nazev, k.nazev AS kategorie, p.datum_expirace
FROM polozka p
JOIN kategorie k ON p.id_kategorie = k.id_kategorie
WHERE p.datum_expirace <= CURRENT_DATE + INTERVAL 30 DAY;

SELECT SUM(pocet_kusu)
FROM polozka;

SELECT k.nazev, COUNT(p.id_polozky)
FROM kategorie k
LEFT JOIN polozka p ON k.id_kategorie = p.id_kategorie
GROUP BY k.nazev;

SELECT MIN(datum_expirace), MAX(datum_expirace)
FROM polozka;

SELECT nazev, datum_expirace, pocet_kusu
FROM polozka
WHERE datum_expirace <= CURRENT_DATE + INTERVAL 14 DAY
UNION
SELECT nazev, datum_expirace, pocet_kusu
FROM polozka
WHERE pocet_kusu < 2;
