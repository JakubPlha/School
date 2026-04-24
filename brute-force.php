<?php

$hash = "5c4c3d6b1e6c7c0c5a5f9e3c6f4e3c0d";
$max_attempts = 1000000;
$start = microtime(true);
$found = false;

for ($attempt = 0; $attempt < $max_attempts; $attempt++) {
    $password = (string)$attempt;
    if (md5($password) === $hash) {
        echo "Heslo je: " . $password . "\n";
        $found = true;
        break;
    }
}

if (!$found) {
    echo "Útok nebyl úpěšný.\n";
}

$end = microtime(true);
$duration = $end - $start;

echo "Počet pokusů: " . ($attempt + 1) . "\n";
echo "Délka trvání: " . $duration . " sekund\n";
