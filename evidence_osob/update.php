<?php
require_once __DIR__ . '/db.php';

session_start();

function redirectWithError(string $error): void
{
    $_SESSION['error'] = $error;
    header('Location: index.php');
    exit;
}

function validateCisloPopisne(string $value): bool
{
    return $value !== '' && ctype_digit($value);
}

function validatePsc(string $value): bool
{
    return ctype_digit($value) && strlen($value) === 5;
}

$id = filter_input(INPUT_POST, 'id', FILTER_VALIDATE_INT);
$jmeno = trim($_POST['jmeno'] ?? '');
$prijmeni = trim($_POST['prijmeni'] ?? '');
$rodneCislo = trim($_POST['rodne_cislo'] ?? '');
$ulice = trim($_POST['ulice'] ?? '');
$cisloPopisne = trim($_POST['cislo_popisne'] ?? '');
$psc = trim($_POST['psc'] ?? '');
$mesto = trim($_POST['mesto'] ?? '');

if ($id === false || $id === null) {
    redirectWithError('Neplatné ID záznamu.');
}

if ($jmeno === '' || $prijmeni === '' || $rodneCislo === '' || $ulice === '' || $cisloPopisne === '' || $psc === '' || $mesto === '') {
    redirectWithError('Všechna pole jsou povinná.');
}

if (!validateCisloPopisne($cisloPopisne)) {
    redirectWithError('Číslo popisné musí obsahovat pouze čísla.');
}

if (!validatePsc($psc)) {
    redirectWithError('PSČ musí obsahovat 5 číslic.');
}

$db = new Database();
$repo = new PersonRepository($db);
$current = $repo->getById($id);
if ($current === null) {
    redirectWithError('Záznam nebyl nalezen.');
}

$existing = $repo->getByRodneCislo($rodneCislo);
if ($existing !== null && $existing['id'] !== $id) {
    redirectWithError('Zadané rodné číslo již existuje.');
}

try {
    $repo->update($id, [
        'jmeno' => $jmeno,
        'prijmeni' => $prijmeni,
        'rodne_cislo' => $rodneCislo,
        'ulice' => $ulice,
        'cislo_popisne' => $cisloPopisne,
        'psc' => $psc,
        'mesto' => $mesto,
    ]);
    $_SESSION['message'] = 'Osoba byla úspěšně aktualizována.';
    header('Location: index.php');
    exit;
} catch (PDOException $e) {
    redirectWithError('Chyba při aktualizaci záznamu.');
}
