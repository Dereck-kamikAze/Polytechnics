import sqlite3

def setup_database():
    conn = sqlite3.connect('prod_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY,
        title TEXT,
        company TEXT,
        location TEXT,
        salary TEXT,
        created_date TEXT,
        closing_date TEXT,
        category TEXT,
        source TEXT,
        UNIQUE(title, company, location, salary, created_date, closing_date, category, source)
    )
''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()