import sqlite3

# Create SQLite database instead of MySQL for easier setup
conn = sqlite3.connect('ai_quiz.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    subject TEXT NOT NULL,
    score INTEGER NOT NULL,
    hint_count INTEGER DEFAULT 0,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

# Insert sample data
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('alice', 'pass123')")
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('bob', 'pass456')")

cursor.execute("INSERT OR IGNORE INTO scores (user_id, subject, score, hint_count) VALUES (1, 'Python', 5, 1)")
cursor.execute("INSERT OR IGNORE INTO scores (user_id, subject, score, hint_count) VALUES (2, 'HTML', 4, 0)")

conn.commit()
conn.close()
print("Database setup complete!")
