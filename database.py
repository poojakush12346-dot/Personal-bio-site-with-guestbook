import sqlite3

def init_db():
    conn = sqlite3.connect("guestbook.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_message(name, email, message):
    conn = sqlite3.connect("guestbook.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages(name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )

    conn.commit()
    conn.close()


def get_messages():
    conn = sqlite3.connect("guestbook.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data