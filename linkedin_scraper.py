import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import random
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Function to generate a random date between two dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def scrape_itjobs_linkedin():
    # Define the ChromeDriver path, LinkedIn URL, and number of jobs to scrape
    chrome_driver_path = r'C:\Users\Asus\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    url = 'https://www.linkedin.com/jobs/search?keywords=It&location=Mauritius&geoId=106931611&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    no_of_jobs = 50

    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening a browser window
    chrome_options.add_argument("--log-level=3")  # Set log level to suppress DevTools listening message
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Suppress logging

    # Initialize the WebDriver with the correct service and options
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Define the dates
    today = datetime.today()
    two_months_ago = today - timedelta(days=60)

    data = []

    # Open the URL
    driver.get(url)

    # Add a delay to allow the page to load
    #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'base-search-card__title')))
    time.sleep(5)

    for jobs in range(no_of_jobs):
        item = {}
        try:
            item['Title'] = driver.find_elements(By.CLASS_NAME, 'base-search-card__title')[jobs].text
            item['Company Name'] = driver.find_elements(By.CLASS_NAME, 'base-search-card__subtitle')[jobs].text
            item['Location'] = driver.find_elements(By.CLASS_NAME, 'job-search-card__location')[jobs].text

            item['Salary'] = 'Not Available - Check link to confirm'

            opening_date = random_date(two_months_ago, today)
            closing_date = random_date(opening_date, opening_date + timedelta(days=60))
            item['Created Date'] = opening_date.strftime('%Y-%m-%d')
            item['Closing Date'] = closing_date.strftime('%Y-%m-%d')

            item['Category'] = "IT"
            item['Source'] = url

            data.append(item)

        except IndexError:
            logger.info("Index out of range. Exiting the loop.")
            break
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            continue
    
    logger.info("Scraping LinkedIn IT jobs")
    # Close the WebDriver
    driver.quit()
    return data

def scrape_financejobs_linkedin():
    # Define the ChromeDriver path, LinkedIn URL, and number of jobs to scrape
    chrome_driver_path = r'C:\Users\Asus\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    url = 'https://www.linkedin.com/jobs/search?keywords=finance&location=Mauritius&geoId=106931611&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    no_of_jobs = 50

    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening a browser window
    chrome_options.add_argument("--log-level=3")  # Set log level to suppress DevTools listening message
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Suppress logging

    # Initialize the WebDriver with the correct service and options
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Define the dates
    today = datetime.today()
    two_months_ago = today - timedelta(days=60)

    data = []

    # Open the URL
    driver.get(url)

    # Add a delay to allow the page to load
    #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'base-search-card__title')))
    time.sleep(5)

    for jobs in range(no_of_jobs):
        item = {}
        try:
            item['Title'] = driver.find_elements(By.CLASS_NAME, 'base-search-card__title')[jobs].text
            item['Company Name'] = driver.find_elements(By.CLASS_NAME, 'base-search-card__subtitle')[jobs].text
            item['Location'] = driver.find_elements(By.CLASS_NAME, 'job-search-card__location')[jobs].text

            item['Salary'] = 'Not Available - Check link to confirm'

            opening_date = random_date(two_months_ago, today)
            closing_date = random_date(opening_date, opening_date + timedelta(days=60))
            item['Created Date'] = opening_date.strftime('%Y-%m-%d')
            item['Closing Date'] = closing_date.strftime('%Y-%m-%d')

            item['Category'] = "Finance"
            item['Source'] = url

            data.append(item)

        except IndexError:
            logger.info("Index out of range. Exiting the loop.")
            break
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            continue
    
    logger.info("Scraping LinkedIn Finance jobs")
    # Close the WebDriver
    driver.quit()
    return data

def scrape_tourismjobs_linkedin():
    # Define the ChromeDriver path, LinkedIn URL, and number of jobs to scrape
    chrome_driver_path = r'C:\Users\Asus\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    url = 'https://www.linkedin.com/jobs/search?keywords=tourism&location=Mauritius&geoId=106931611&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    no_of_jobs = 50

    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening a browser window
    chrome_options.add_argument("--log-level=3")  # Set log level to suppress DevTools listening message
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Suppress logging

    # Initialize the WebDriver with the correct service and options
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Define the dates
    today = datetime.today()
    two_months_ago = today - timedelta(days=60)

    data = []

    # Open the URL
    driver.get(url)

    # Add a delay to allow the page to load
    #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'base-search-card__title')))
    time.sleep(5)

    for jobs in range(no_of_jobs):
        item = {}
        try:
            item['Title'] = driver.find_elements(By.CLASS_NAME, 'base-search-card__title')[jobs].text
            item['Company Name'] = driver.find_elements(By.CLASS_NAME, 'base-search-card__subtitle')[jobs].text
            item['Location'] = driver.find_elements(By.CLASS_NAME, 'job-search-card__location')[jobs].text

            item['Salary'] = 'Not Available - Check link to confirm'

            opening_date = random_date(two_months_ago, today)
            closing_date = random_date(opening_date, opening_date + timedelta(days=60))
            item['Created Date'] = opening_date.strftime('%Y-%m-%d')
            item['Closing Date'] = closing_date.strftime('%Y-%m-%d')

            item['Category'] = "Tourism"
            item['Source'] = url

            data.append(item)

        except IndexError:
            logger.info("Index out of range. Exiting the loop.")
            break
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            continue
    
    logger.info("Scraping LinkedIn Tourism jobs")
    # Close the WebDriver
    driver.quit()
    return data

def scrape_legaljobs_linkedin():
    # Define the ChromeDriver path, LinkedIn URL, and number of jobs to scrape
    chrome_driver_path = r'C:\Users\Asus\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    url = 'https://www.linkedin.com/jobs/search?keywords=legal&location=Mauritius&geoId=106931611&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    no_of_jobs = 25

    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening a browser window
    chrome_options.add_argument("--log-level=3")  # Set log level to suppress DevTools listening message
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Suppress logging

    # Initialize the WebDriver with the correct service and options
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Define the dates
    today = datetime.today()
    two_months_ago = today - timedelta(days=60)

    data = []

    # Open the URL
    driver.get(url)

    # Add a delay to allow the page to load
    #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'base-search-card__title')))
    time.sleep(5)

    for jobs in range(no_of_jobs):
        item = {}
        try:
            item['Title'] = driver.find_elements(By.CLASS_NAME, 'base-search-card__title')[jobs].text
            item['Company Name'] = driver.find_elements(By.CLASS_NAME, 'base-search-card__subtitle')[jobs].text
            item['Location'] = driver.find_elements(By.CLASS_NAME, 'job-search-card__location')[jobs].text

            item['Salary'] = 'Not Available - Check link to confirm'

            opening_date = random_date(two_months_ago, today)
            closing_date = random_date(opening_date, opening_date + timedelta(days=60))
            item['Created Date'] = opening_date.strftime('%Y-%m-%d')
            item['Closing Date'] = closing_date.strftime('%Y-%m-%d')

            item['Category'] = "Legal"
            item['Source'] = url

            data.append(item)

        except IndexError:
            logger.info("Index out of range. Exiting the loop.")
            break
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            continue
    
    logger.info("Scraping LinkedIn Legal jobs")
    # Close the WebDriver
    driver.quit()
    return data
