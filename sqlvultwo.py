import sqlite3

def get_user(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user

if __name__ == "__main__":
    username = input("Enter a username: ")
    user = get_user(username)
    print(user)
