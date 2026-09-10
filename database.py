import sqlite3


DATABASE = "users.db"


def create_database():
    connection = sqlite3.connect(DATABASE)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_user(username, hashed_password):
    connection = sqlite3.connect(DATABASE)

    try:
        connection.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        connection.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        connection.close()


def get_user(username):
    connection = sqlite3.connect(DATABASE)

    user = connection.execute(
        "SELECT id, username, password FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    connection.close()

    return user