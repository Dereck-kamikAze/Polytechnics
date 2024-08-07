# database.py
import sqlite3

from jobsmu import scrape_itjobs_jobsmu

# Scrape IT jobs from LinkedIn
legal_jobs_linkedin = scrape_itjobs_jobsmu()

if legal_jobs_linkedin is None:
    print("No tourism jobs were scraped from LinkedIn.")
    legal_jobs_linkedin = []

# Convert MyJob.mu data to list of tuples
legal_data_linkedin = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], job['Category'], job['Source']) for job in legal_jobs_linkedin]


# Connect to SQLite database (creates a new database if not exists)
conn = sqlite3.connect('test_database.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create a table with a unique constraint on title, company, and location
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

# Function to insert a job into the database
def insert_job(cursor, job):
    try:
        cursor.execute('''
            INSERT INTO jobs (title, company, location, salary, created_date, closing_date, category, source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', job)
    except sqlite3.IntegrityError:
        # Ignore the duplicate entry
        pass

# Insert data into the table
for job in legal_data_linkedin:
    insert_job(cursor, job)

# Commit the transaction
conn.commit()

# Query data from the table
cursor.execute('SELECT * FROM jobs')

# Fetch all rows
rows = cursor.fetchall()

# Print fetched rows (if you want to print the rows)
# for row in rows:
#     print(row)

# Close the cursor and connection
cursor.close()
conn.close()
