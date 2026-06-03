<?php
require_once __DIR__ . '/db.php';

session_start();

$id = filter_input(INPUT_POST, 'id', FILTER_VALIDATE_INT);
if ($id === false || $id === null) {
    $_SESSION['error'] = 'Neplatné ID záznamu.';
    header('Location: index.php');
    exit;
}

$db = new Database();
$repo = new PersonRepository($db);
try {
    $repo->delete($id);
    $_SESSION['message'] = 'Záznam byl úspěšně smazán.';
} catch (PDOException $e) {
    $_SESSION['error'] = 'Chyba při mazání záznamu.';
}

header('Location: index.php');
exit;
