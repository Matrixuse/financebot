import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
email TEXT UNIQUE,
password TEXT
)
""")

conn.commit()


# ---------------- SIGNUP ----------------

def register_user(username, email, password):

    try:
        cursor.execute(
            "INSERT INTO users(username,email,password) VALUES(?,?,?)",
            (username, email, password)
        )

        conn.commit()
        return True

    except Exception as e:
        print(e)
        return False


# ---------------- LOGIN ----------------

def login_user(email, password):

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    user = cursor.fetchone()

    if user:
        return True
    else:
        return False