<?php

echo "Hello, what is your name? \n";
$handle = fopen ("php://stdin", "f");
$name = fgets($handle);
$name = trim(preg_replace('/\s+/', ' ', $name));
echo "Hello, $name, it's nice to meet you! \n";
fclose($handle);

?>

