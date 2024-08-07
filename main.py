# database.py
import sqlite3
from myjobmu_scraper import scrape_itjobs_myjobmu
from myjobmu_scraper import scrape_financejobs_myjobmu
from myjobmu_scraper import scrape_tourismjobs_myjobmu
from myjobmu_scraper import scrape_pharmajobs_myjobmu
from myjobmu_scraper import scrape_legaljobs_myjobmu

from linkedin_scraper import scrape_itjobs_linkedin
from linkedin_scraper import scrape_financejobs_linkedin
from linkedin_scraper import scrape_tourismjobs_linkedin
from linkedin_scraper import scrape_legaljobs_linkedin

from jobsmu import scrape_itjobs_jobsmu
from jobsmu import scrape_financejobs_jobsmu
from jobsmu import scrape_tourismjobs_jobsmu
from jobsmu import scrape_legaljobs_jobsmu

# Scrape jobs from MyJob.mu
it_jobs = scrape_itjobs_myjobmu()
finance_jobs = scrape_financejobs_myjobmu()
tourism_jobs = scrape_tourismjobs_myjobmu()
pharma_jobs = scrape_pharmajobs_myjobmu()
legal_jobs = scrape_legaljobs_myjobmu()

# Scrape jobs from LinkedIn
it_jobs_linkedin = scrape_itjobs_linkedin()
finance_jobs_linkedin = scrape_financejobs_linkedin()
tourism_jobs_linkedin = scrape_tourismjobs_linkedin()
legal_jobs_linkedin = scrape_legaljobs_linkedin()

# Scrape jobs from Jobs.mu
it_jobs_jobsmu = scrape_itjobs_jobsmu()
finance_jobs_jobsmu = scrape_financejobs_jobsmu()
tourism_jobs_jobsmu = scrape_tourismjobs_jobsmu()
legal_jobs_jobsmu = scrape_legaljobs_jobsmu()


# Check if data is None
if it_jobs is None:
    print("No IT jobs were scraped from MyJob.mu.")
    it_jobs_myjobmu = []

if finance_jobs is None:
    print("No finance jobs were scraped.")
    finance_jobs = []

if tourism_jobs is None:
    print("No tourism jobs were scraped.")
    tourism_jobs = []

if pharma_jobs is None:
    print("No pharma jobs were scraped.")
    pharma_jobs = []

if legal_jobs is None:
    print("No legal jobs were scraped.")
    legal_jobs = []

if it_jobs_linkedin is None:
    print("No IT jobs were scraped from LinkedIn.")
    it_jobs_linkedin = []

if finance_jobs_linkedin is None:
    print("No finance jobs were scraped from LinkedIn.")
    finance_jobs_linkedin = []

if tourism_jobs_linkedin is None:
    print("No tourism jobs were scraped from LinkedIn.")
    tourism_jobs_linkedin = []

if legal_jobs_linkedin is None:
    print("No tourism jobs were scraped from LinkedIn.")
    legal_jobs_linkedin = []

if it_jobs_jobsmu is None:
    print("No IT jobs were scraped from LinkedIn.")
    it_jobs_jobsmu = []

if finance_jobs_jobsmu is None:
    print("No finance jobs were scraped from LinkedIn.")
    finance_jobs_jobsmu = []

if tourism_jobs_jobsmu is None:
    print("No tourism jobs were scraped from LinkedIn.")
    tourism_jobs_jobsmu = []

if legal_jobs_jobsmu is None:
    print("No legal jobs were scraped from LinkedIn.")
    legal_jobs_jobsmu = []

# Convert MyJob.mu data to list of tuples
it_data = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], 'IT', job['Source']) for job in it_jobs]
finance_data = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], 'Finance', job['Source']) for job in finance_jobs]
tourism_data = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], 'Tourism', job['Source']) for job in tourism_jobs]
pharma_data = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], 'Pharma', job['Source']) for job in pharma_jobs]
legal_data = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], 'Legal', job['Source']) for job in legal_jobs]

# Convert LinkedIn data to list of tuples
it_data_linkedin = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], job['Category'], job['Source']) for job in it_jobs_linkedin]
finance_data_linkedin = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], job['Category'], job['Source']) for job in finance_jobs_linkedin]
tourism_data_linkedin = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], job['Category'], job['Source']) for job in tourism_jobs_linkedin]
legal_data_linkedin = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], job['Category'], job['Source']) for job in legal_jobs_linkedin]

# Convert jobsmu data to list of tuples
it_data_jobsmu = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], job['Category'], job['Source']) for job in it_jobs_jobsmu]
finance_data_jobsmu = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], job['Category'], job['Source']) for job in finance_jobs_jobsmu]
tourism_data_jobsmu = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], job['Category'], job['Source']) for job in tourism_jobs_jobsmu]
legal_data_jobsmu = [(job['Title'], job['Company Name'], job['Location'], job['Salary'], job['Created Date'], job['Closing Date'], job['Category'], job['Source']) for job in legal_jobs_jobsmu]


# Connect to SQLite database (creates a new database if not exists)
conn = sqlite3.connect('prod_database.db')

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
for job in it_data:
    insert_job(cursor, job)

for job in finance_data:
    insert_job(cursor, job)

for job in tourism_data:
    insert_job(cursor, job)

for job in pharma_data:
    insert_job(cursor, job)

for job in legal_data:
    insert_job(cursor, job)

for job in finance_data_linkedin:
    insert_job(cursor, job)

for job in tourism_data_linkedin:
    insert_job(cursor, job)

for job in legal_data_linkedin:
    insert_job(cursor, job)

for job in it_data_jobsmu:
    insert_job(cursor, job)

for job in finance_data_jobsmu:
    insert_job(cursor, job)

for job in tourism_data_jobsmu:
    insert_job(cursor, job)

for job in legal_data_jobsmu:
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
