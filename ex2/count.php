<?php

echo "What is your string? \n";
$handle = fopen ("php://stdin", "f");
$user_string = fgets($handle);
$user_string = trim(preg_replace('/\s+/', ' ', $user_string));
$count = strlen($user_string);
echo "Your string, $user_string, has $count characters! \n";
fclose($handle);

?>

