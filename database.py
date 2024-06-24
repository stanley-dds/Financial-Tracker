import sqlite3

def create_connection():
    conn = sqlite3.connect('finance.db')
    return conn

def create_tables(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                date TEXT,
                category TEXT,
                amount REAL,
                type TEXT
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')

if __name__ == "__main__":
    conn = create_connection()
    create_tables(conn)
    conn.close()
