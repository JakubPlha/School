<?php
require_once __DIR__ . '/db.php';

session_start();

$db = new Database();
$repo = new PersonRepository($db);
$people = $repo->getAll();

$message = $_SESSION['message'] ?? null;
$error = $_SESSION['error'] ?? null;
$old = $_SESSION['old'] ?? [];

unset($_SESSION['message'], $_SESSION['error'], $_SESSION['old']);

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
    <title>Evidence osob</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="page-shell">
    <main class="container">
        <section class="panel panel-large">
            <div class="panel-header">
                <div>
                    <h2>Nová osoba</h2>
                    <p>Vložte kompletní osobní údaje a adresu.</p>
                </div>
            </div>

            <?php if ($message): ?>
                <div class="alert success"><?= escape($message) ?></div>
            <?php endif; ?>
            <?php if ($error): ?>
                <div class="alert error"><?= escape($error) ?></div>
            <?php endif; ?>

            <form action="save.php" method="post" class="form-grid">
                <fieldset>
                    <legend>OSOBNÍ ÚDAJE</legend>
                    <label>
                        <span>Jméno</span>
                        <input type="text" name="jmeno" value="<?= escape($old['jmeno'] ?? '') ?>" required>
                    </label>
                    <label>
                        <span>Příjmení</span>
                        <input type="text" name="prijmeni" value="<?= escape($old['prijmeni'] ?? '') ?>" required>
                    </label>
                    <label>
                        <span>Rodné číslo</span>
                        <input type="text" name="rodne_cislo" value="<?= escape($old['rodne_cislo'] ?? '') ?>" pattern="\d{6}/\d{3,4}" placeholder="850512/1234" title="Rodné číslo ve formátu 850512/1234" inputmode="numeric" required>
                    </label>
                </fieldset>

                <fieldset>
                    <legend>ADRESA</legend>
                    <label>
                        <span>Ulice</span>
                        <input type="text" name="ulice" value="<?= escape($old['ulice'] ?? '') ?>" required>
                    </label>
                    <label>
                        <span>Číslo popisné</span>
                        <input type="text" name="cislo_popisne" value="<?= escape($old['cislo_popisne'] ?? '') ?>" pattern="\d+" placeholder="123" title="Zadejte pouze čísla" inputmode="numeric" required>
                    </label>
                    <label>
                        <span>PSČ</span>
                        <input type="text" name="psc" value="<?= escape($old['psc'] ?? '') ?>" pattern="\d{5}" placeholder="12345" title="Zadejte PSČ jako 5 číslic" inputmode="numeric" required>
                    </label>
                    <label>
                        <span>Město</span>
                        <input type="text" name="mesto" value="<?= escape($old['mesto'] ?? '') ?>" required>
                    </label>
                </fieldset>

                <div class="form-actions">
                    <button type="submit" class="btn btn-primary">Uložit</button>
                    <button type="reset" class="btn btn-secondary">Zrušit</button>
                </div>
            </form>
        </section>

        <section class="panel">
            <div class="panel-header">
                <div>
                    <h2>Seznam osob</h2>
                    <p>Aktuální záznamy v databázi.</p>
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
                        <?php foreach ($people as $person): ?>
                            <tr>
                                <td><?= escape($person['jmeno']) ?></td>
                                <td><?= escape($person['prijmeni']) ?></td>
                                <td><?= escape($person['rodne_cislo']) ?></td>
                                <td>
                                    <?= escape($person['ulice']) ?> <?= escape($person['cislo_popisne']) ?><br>
                                    <?= escape($person['psc']) ?> <?= escape($person['mesto']) ?>
                                </td>
                                <td class="actions">
                                    <a href="edit.php?id=<?= $person['id'] ?>" class="btn btn-muted">Upravit</a>
                                    <form action="delete.php" method="post" onsubmit="return confirm('Opravdu chcete smazat tento záznam?');" class="inline-form">
                                        <input type="hidden" name="id" value="<?= $person['id'] ?>">
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
