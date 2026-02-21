<?php
$server name ="localhost";
$server username ="root";
$server password ="";
$database_name ="Yvette";
$conn = new mysqli($server name, $server username, $server password, $database_name);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
    echo "Connected successfully";
}
?>