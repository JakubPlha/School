<?php
require_once __DIR__ . '/db.php';

session_start();

function redirectWithError(string $error, array $old = []): void
{
    $_SESSION['error'] = $error;
    $_SESSION['old'] = $old;
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

$jmeno = trim($_POST['jmeno'] ?? '');
$prijmeni = trim($_POST['prijmeni'] ?? '');
$rodneCislo = trim($_POST['rodne_cislo'] ?? '');
$ulice = trim($_POST['ulice'] ?? '');
$cisloPopisne = trim($_POST['cislo_popisne'] ?? '');
$psc = trim($_POST['psc'] ?? '');
$mesto = trim($_POST['mesto'] ?? '');

$old = [
    'jmeno' => $jmeno,
    'prijmeni' => $prijmeni,
    'rodne_cislo' => $rodneCislo,
    'ulice' => $ulice,
    'cislo_popisne' => $cisloPopisne,
    'psc' => $psc,
    'mesto' => $mesto,
];

if ($jmeno === '' || $prijmeni === '' || $rodneCislo === '' || $ulice === '' || $cisloPopisne === '' || $psc === '' || $mesto === '') {
    redirectWithError('Všechna pole jsou povinná.', $old);
}

if (!validateCisloPopisne($cisloPopisne)) {
    redirectWithError('Číslo popisné musí obsahovat pouze čísla.', $old);
}

if (!validatePsc($psc)) {
    redirectWithError('PSČ musí obsahovat 5 číslic.', $old);
}

$db = new Database();
$repo = new PersonRepository($db);

if ($repo->getByRodneCislo($rodneCislo) !== null) {
    redirectWithError('Zadané rodné číslo již existuje.', $old);
}

try {
    $repo->create([
        'jmeno' => $jmeno,
        'prijmeni' => $prijmeni,
        'rodne_cislo' => $rodneCislo,
        'ulice' => $ulice,
        'cislo_popisne' => $cisloPopisne,
        'psc' => $psc,
        'mesto' => $mesto,
    ]);
    $_SESSION['message'] = 'Osoba byla úspěšně přidána.';
    header('Location: index.php');
    exit;
} catch (PDOException $e) {
    redirectWithError('Chyba při ukládání do databáze.', $old);
}
