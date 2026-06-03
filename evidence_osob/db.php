<?php

class Database
{
    private PDO $pdo;

    public function __construct()
    {
        $this->initialize();
    }

    private function initialize(): void
    {
        $databaseFile = __DIR__ . '/database.sqlite';
        $isNew = !file_exists($databaseFile);

        $this->pdo = new PDO('sqlite:' . $databaseFile);
        $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $this->pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

        if ($isNew) {
            $this->createSchema();
        } else {
            $this->createSchema();
        }
    }

    private function createSchema(): void
    {
        $sql = file_get_contents(__DIR__ . '/sql/schema.sql');
        $this->pdo->exec($sql);
    }

    public function getConnection(): PDO
    {
        return $this->pdo;
    }
}

class PersonRepository
{
    private PDO $pdo;

    public function __construct(Database $db)
    {
        $this->pdo = $db->getConnection();
    }

    public function getAll(): array
    {
        $stmt = $this->pdo->query('SELECT * FROM osoby ORDER BY prijmeni, jmeno');
        return $stmt->fetchAll();
    }

    public function getById(int $id): ?array
    {
        $stmt = $this->pdo->prepare('SELECT * FROM osoby WHERE id = :id');
        $stmt->execute([':id' => $id]);
        $person = $stmt->fetch();
        return $person === false ? null : $person;
    }

    public function getByRodneCislo(string $rodneCislo): ?array
    {
        $stmt = $this->pdo->prepare('SELECT * FROM osoby WHERE rodne_cislo = :rodne_cislo');
        $stmt->execute([':rodne_cislo' => $rodneCislo]);
        $person = $stmt->fetch();
        return $person === false ? null : $person;
    }

    public function create(array $data): void
    {
        $stmt = $this->pdo->prepare(
            'INSERT INTO osoby (jmeno, prijmeni, rodne_cislo, ulice, cislo_popisne, psc, mesto)
             VALUES (:jmeno, :prijmeni, :rodne_cislo, :ulice, :cislo_popisne, :psc, :mesto)'
        );

        $stmt->execute([
            ':jmeno' => $data['jmeno'],
            ':prijmeni' => $data['prijmeni'],
            ':rodne_cislo' => $data['rodne_cislo'],
            ':ulice' => $data['ulice'],
            ':cislo_popisne' => $data['cislo_popisne'],
            ':psc' => $data['psc'],
            ':mesto' => $data['mesto'],
        ]);
    }

    public function update(int $id, array $data): void
    {
        $stmt = $this->pdo->prepare(
            'UPDATE osoby SET jmeno = :jmeno, prijmeni = :prijmeni, rodne_cislo = :rodne_cislo,
             ulice = :ulice, cislo_popisne = :cislo_popisne, psc = :psc, mesto = :mesto
             WHERE id = :id'
        );

        $stmt->execute([
            ':jmeno' => $data['jmeno'],
            ':prijmeni' => $data['prijmeni'],
            ':rodne_cislo' => $data['rodne_cislo'],
            ':ulice' => $data['ulice'],
            ':cislo_popisne' => $data['cislo_popisne'],
            ':psc' => $data['psc'],
            ':mesto' => $data['mesto'],
            ':id' => $id,
        ]);
    }

    public function delete(int $id): void
    {
        $stmt = $this->pdo->prepare('DELETE FROM osoby WHERE id = :id');
        $stmt->execute([':id' => $id]);
    }
}
