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

def scrape_itjobs_jobsmu():
    chrome_driver_path = r'C:\Users\Asus\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    url = 'https://www.jobs.mu/jobs/?searchId=1721580488.4903&action=refine&JobCategory[multi_like][]=706'
    no_of_jobs = 10

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    data = []
    driver.get(url)
    time.sleep(5)

    for jobs in range(no_of_jobs):
            item = {}
            try:
                title_elements = driver.find_elements(By.CLASS_NAME, 'utf-job-listing-title')
                company_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-feather-briefcase + span')
                location_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-location-on + span')
                salary_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-line-awesome-money + span')
                created_date_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-access-time + span')
                closing_date_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-access-alarm + span')

                # Add logging to check if elements were found
                #logger.info(f'Found {len(title_elements)} titles, {len(company_elements)} companies, {len(location_elements)} locations, {len(salary_elements)} salaries, {len(created_date_elements)} created dates, {len(closing_date_elements)} closing dates')

                if jobs < len(title_elements):
                    item['Title'] = title_elements[jobs].text
                if jobs < len(company_elements):
                    item['Company Name'] = company_elements[jobs].text
                if jobs < len(location_elements):
                    item['Location'] = location_elements[jobs].text
                if jobs < len(salary_elements):
                    item['Salary'] = salary_elements[jobs].text
                if jobs < len(created_date_elements):
                    item['Created Date'] = created_date_elements[jobs].text
                if jobs < len(closing_date_elements):
                    item['Closing Date'] = closing_date_elements[jobs].text

                item['Category'] = "IT"
                item['Source'] = url

                data.append(item)

            except IndexError:
                logger.info("Index out of range. Exiting the loop.")
                break
            except Exception as e:
                logger.error(f"An error occurred: {e}")
                continue

    
    driver.quit()
    return data

def scrape_financejobs_jobsmu():
    chrome_driver_path = r'C:\Users\Asus\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    url = 'https://www.jobs.mu/jobs/?searchId=1721585151.2767&action=refine&JobCategory[multi_like][]=707'
    no_of_jobs = 10

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    data = []
    driver.get(url)
    time.sleep(5)

    for jobs in range(no_of_jobs):
            item = {}
            try:
                title_elements = driver.find_elements(By.CLASS_NAME, 'utf-job-listing-title')
                company_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-feather-briefcase + span')
                location_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-location-on + span')
                salary_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-line-awesome-money + span')
                created_date_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-access-time + span')
                closing_date_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-access-alarm + span')

                # Add logging to check if elements were found
                #logger.info(f'Found {len(title_elements)} titles, {len(company_elements)} companies, {len(location_elements)} locations, {len(salary_elements)} salaries, {len(created_date_elements)} created dates, {len(closing_date_elements)} closing dates')

                if jobs < len(title_elements):
                    item['Title'] = title_elements[jobs].text
                if jobs < len(company_elements):
                    item['Company Name'] = company_elements[jobs].text
                if jobs < len(location_elements):
                    item['Location'] = location_elements[jobs].text
                if jobs < len(salary_elements):
                    item['Salary'] = salary_elements[jobs].text
                if jobs < len(created_date_elements):
                    item['Created Date'] = created_date_elements[jobs].text
                if jobs < len(closing_date_elements):
                    item['Closing Date'] = closing_date_elements[jobs].text

                item['Category'] = "Finance"
                item['Source'] = url

                data.append(item)

            except IndexError:
                logger.info("Index out of range. Exiting the loop.")
                break
            except Exception as e:
                logger.error(f"An error occurred: {e}")
                continue

    
    driver.quit()
    return data

def scrape_tourismjobs_jobsmu():
    chrome_driver_path = r'C:\Users\Asus\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    url = 'https://www.jobs.mu/jobs/?searchId=1721585644.9792&action=refine&JobCategory[multi_like][]=710'
    no_of_jobs = 10

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    data = []
    driver.get(url)
    time.sleep(5)

    for jobs in range(no_of_jobs):
            item = {}
            try:
                title_elements = driver.find_elements(By.CLASS_NAME, 'utf-job-listing-title')
                company_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-feather-briefcase + span')
                location_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-location-on + span')
                salary_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-line-awesome-money + span')
                created_date_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-access-time + span')
                closing_date_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-access-alarm + span')

                # Add logging to check if elements were found
                #logger.info(f'Found {len(title_elements)} titles, {len(company_elements)} companies, {len(location_elements)} locations, {len(salary_elements)} salaries, {len(created_date_elements)} created dates, {len(closing_date_elements)} closing dates')

                if jobs < len(title_elements):
                    item['Title'] = title_elements[jobs].text
                if jobs < len(company_elements):
                    item['Company Name'] = company_elements[jobs].text
                if jobs < len(location_elements):
                    item['Location'] = location_elements[jobs].text
                if jobs < len(salary_elements):
                    item['Salary'] = salary_elements[jobs].text
                if jobs < len(created_date_elements):
                    item['Created Date'] = created_date_elements[jobs].text
                if jobs < len(closing_date_elements):
                    item['Closing Date'] = closing_date_elements[jobs].text

                item['Category'] = "Tourism"
                item['Source'] = url

                data.append(item)

            except IndexError:
                logger.info("Index out of range. Exiting the loop.")
                break
            except Exception as e:
                logger.error(f"An error occurred: {e}")
                continue

    
    driver.quit()
    return data

def scrape_legaljobs_jobsmu():
    chrome_driver_path = r'C:\Users\Asus\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    url = 'https://www.jobs.mu/jobs/?searchId=1721586029.4612&action=refine&JobCategory[multi_like][]=708'
    no_of_jobs = 10

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    data = []
    driver.get(url)
    time.sleep(5)

    for jobs in range(no_of_jobs):
            item = {}
            try:
                title_elements = driver.find_elements(By.CLASS_NAME, 'utf-job-listing-title')
                company_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-feather-briefcase + span')
                location_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-location-on + span')
                salary_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-line-awesome-money + span')
                created_date_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-access-time + span')
                closing_date_elements = driver.find_elements(By.CSS_SELECTOR, '.utf-job-listing-footer .icon-material-outline-access-alarm + span')

                # Add logging to check if elements were found
                #logger.info(f'Found {len(title_elements)} titles, {len(company_elements)} companies, {len(location_elements)} locations, {len(salary_elements)} salaries, {len(created_date_elements)} created dates, {len(closing_date_elements)} closing dates')

                if jobs < len(title_elements):
                    item['Title'] = title_elements[jobs].text
                if jobs < len(company_elements):
                    item['Company Name'] = company_elements[jobs].text
                if jobs < len(location_elements):
                    item['Location'] = location_elements[jobs].text
                if jobs < len(salary_elements):
                    item['Salary'] = salary_elements[jobs].text
                if jobs < len(created_date_elements):
                    item['Created Date'] = created_date_elements[jobs].text
                if jobs < len(closing_date_elements):
                    item['Closing Date'] = closing_date_elements[jobs].text

                item['Category'] = "Legal"
                item['Source'] = url

                data.append(item)

            except IndexError:
                logger.info("Index out of range. Exiting the loop.")
                break
            except Exception as e:
                logger.error(f"An error occurred: {e}")
                continue

    
    driver.quit()
    return data
