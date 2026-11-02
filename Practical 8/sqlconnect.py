import sqlite3

connection = sqlite3.connect("students.db")

print("Database connected successfully!")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_no TEXT UNIQUE NOT NULL,
    marks REAL CHECK(marks >= 0 AND marks <= 100)
)
""")

connection.commit()

connection.close()

print("Students table created successfully!")