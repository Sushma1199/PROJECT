import mysql.connector

# Get user input from the login form
username = input("Username: ")
password = input("Password: ")

# Construct the SQL query
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Execute the query
cursor.execute(query)

# Fetch the results
result = cursor.fetchall()

# Check for a matching user
if len(result) > 0:
    print("Login successful!")
else:
    print("Invalid username or password.")

# Close the cursor and database connection
cursor.close()
db.close()
