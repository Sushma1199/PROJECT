<?php
// Get user input from the login form
$username = $_POST['username'];
$password = $_POST['password'];

// Construct the SQL query
$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";

// Execute the query and check for a matching user
$result = mysql_query($query);
$row = mysql_fetch_assoc($result);

if ($row) {
    // User authentication successful
    echo "Login successful!";
} else {
    // User authentication failed
    echo "Invalid username or password.";
}
?>
