CREATE TABLE hockeyPlayer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(30) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    team VARCHAR(50) NOT NULL
);

DELIMITER //

CREATE PROCEDURE insert_player(
    IN p_fname VARCHAR(30),
    IN p_lname VARCHAR(50),
    IN p_team VARCHAR(50)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT "Chyba" AS zprava;
    END;

    SET autocommit = 0
    START TRANSACTION;
        INSERT INTO hockeyPlayer (fname, lname, team)
        VALUES (p_fname, p_lname, p_team);

    COMMIT;
    SET autocommit = 1

    SELECT "transakce probehla" AS zprava;
END //

DELIMITER ;

CALL insert_player("David", "Pastrňák", "Boston Bruins");

CALL insert_player("Pavel", "Zacha", NULL);

