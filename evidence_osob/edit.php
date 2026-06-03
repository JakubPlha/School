<?php
require_once __DIR__ . '/db.php';

session_start();

$db = new Database();
$repo = new PersonRepository($db);

$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false || $id === null) {
    header('Location: index.php');
    exit;
}

$person = $repo->getById($id);
if ($person === null) {
    header('Location: index.php');
    exit;
}

$people = $repo->getAll();
$message = $_SESSION['message'] ?? null;
$error = $_SESSION['error'] ?? null;
unset($_SESSION['message'], $_SESSION['error']);

function escape(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
}
?>
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upravit osobu | Evidence osob</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="page-shell">
    <main class="container">
        <section class="panel panel-large">
            <div class="panel-header">
                <div>
                    <h2>Upravit osobu</h2>
                    <p>Změňte údaje ve formuláři a uložte aktualizaci.</p>
                </div>
            </div>

            <?php if ($message): ?>
                <div class="alert success"><?= escape($message) ?></div>
            <?php endif; ?>
            <?php if ($error): ?>
                <div class="alert error"><?= escape($error) ?></div>
            <?php endif; ?>

            <form action="update.php" method="post" class="form-grid">
                <input type="hidden" name="id" value="<?= $person['id'] ?>">

                <fieldset>
                    <legend>OSOBNÍ ÚDAJE</legend>
                    <label>
                        <span>Jméno</span>
                        <input type="text" name="jmeno" value="<?= escape($person['jmeno']) ?>" required placeholder="Jan">
                    </label>
                    <label>
                        <span>Příjmení</span>
                        <input type="text" name="prijmeni" value="<?= escape($person['prijmeni']) ?>" required placeholder="Novák">
                    </label>
                    <label>
                        <span>Rodné číslo</span>
                        <input type="text" name="rodne_cislo" value="<?= escape($person['rodne_cislo']) ?>"  placeholder="850512/1234" title="Rodné číslo ve formátu 850512/1234" inputmode="numeric" required>
                    </label>
                </fieldset>

                <fieldset>
                    <legend>ADRESA</legend>
                    <label>
                        <span>Ulice</span>
                        <input type="text" name="ulice" value="<?= escape($person['ulice']) ?>" placeholder="bažina" required>
                    </label>
                    <label>
                        <span>Číslo popisné</span>
                        <input type="text" name="cislo_popisne" value="<?= escape($person['cislo_popisne']) ?>" placeholder="123" title="Zadejte pouze čísla" inputmode="numeric" required>
                    </label>
                    <label>
                        <span>PSČ</span>
                        <input type="text" name="psc" value="<?= escape($person['psc']) ?>" placeholder="12345" title="Zadejte PSČ jako 5 číslic" inputmode="numeric" required>
                    </label>
                    <label>
                        <span>Město</span>
                        <input type="text" name="mesto" value="<?= escape($person['mesto']) ?>" required>
                    </label>
                </fieldset>

                <div class="form-actions">
                    <button type="submit" class="btn btn-primary">Aktualizovat</button>
                    <a href="index.php" class="btn btn-secondary">Zrušit</a>
                </div>
            </form>
        </section>

        <section class="panel">
            <div class="panel-header">
                <div>
                    <h2>Seznam osob</h2>
                </div>
            </div>
            <div class="table-wrap">
                <table>
                    <thead>
                    <tr>
                        <th>Jméno</th>
                        <th>Příjmení</th>
                        <th>Rodné číslo</th>
                        <th>Adresa</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    <?php if (count($people) === 0): ?>
                        <tr>
                            <td colspan="5" class="empty">Žádné záznamy.</td>
                        </tr>
                    <?php else: ?>
                        <?php foreach ($people as $row): ?>
                            <tr>
                                <td><?= escape($row['jmeno']) ?></td>
                                <td><?= escape($row['prijmeni']) ?></td>
                                <td><?= escape($row['rodne_cislo']) ?></td>
                                <td>
                                    <?= escape($row['ulice']) ?> <?= escape($row['cislo_popisne']) ?><br>
                                    <?= escape($row['psc']) ?> <?= escape($row['mesto']) ?>
                                </td>
                                <td class="actions">
                                    <a href="edit.php?id=<?= $row['id'] ?>" class="btn btn-muted">Upravit</a>
                                    <form action="delete.php" method="post" onsubmit="return confirm('Opravdu chcete smazat tento záznam?');" class="inline-form">
                                        <input type="hidden" name="id" value="<?= $row['id'] ?>">
                                        <button type="submit" class="btn btn-danger">Smazat</button>
                                    </form>
                                </td>
                            </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                    </tbody>
                </table>
            </div>
        </section>
    </main>
</div>
</body>
</html>
