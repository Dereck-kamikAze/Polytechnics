# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import sqlite3

def scrape_itjobs_myjobmu():
    current_page = 1

    data = []

    proceed = True

    while(proceed):
        print("Currently scrapping IT category in myjob.mu page:"+str(current_page))

        #Variable for url page
        url = "https://www.myjob.mu/Jobs/ICT-IT-Web/?Page="+str(current_page)

        # Fetch the web page
        response = requests.get(url)

        #if response.status_code == 200:
        #    page_content = response.text
        #    print(f"Succeed to retrieve the webpage. Status code: {response.status_code}")
        #else:
        #    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            #exit()

        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")

        if url == "https://www.myjob.mu/Jobs/ICT-IT-Web/?Page=5":
            proceed = False
        else:
            all_jobs = soup.find_all("div",class_="module job-result")
        
            for job in all_jobs:
                item = {}

                item['Title'] = job.find("h2").text
                item['Company Name'] = job.find("h3").text.strip()
                location_tag = job.find("li", class_="location").find("a")
                item['Location'] = location_tag.text.strip()
                salary_tag = job.find("li", class_="salary")
                item['Salary'] = salary_tag.text
                addeddate_tag = job.find("li", class_="updated-time")
                item['Created Date'] = addeddate_tag.text
                closeddate_tag = job.find("li", class_="closed-time")
                item['Closing Date'] = closeddate_tag.text
                item['Category'] = "IT"
                item['Source'] = url
        
                #print(item['Title'])
                #print(item['Company Name'])
                #print(item['Location'])
                #print(item['Salary'])
                #print(item['Created Date'])
                #print(item['Closing Date'])
                #print(item['Category'])
                #print(item['Source'])
                data.append(item)
            
        current_page = current_page + 1
        #proceed = False
    return data
   
def scrape_financejobs_myjobmu():
    current_page = 1

    data = []

    proceed = True

    while(proceed):
        print("Currently scrapping Finance category in myjob.mu page:"+str(current_page))

        #Variable for url page
        url = "https://www.myjob.mu/Jobs/Accounting-Auditing-Tax-Services-Finance/?Page="+str(current_page)

        # Fetch the web page
        response = requests.get(url)

        #if response.status_code == 200:
        #    page_content = response.text
        #    print(f"Succeed to retrieve the webpage. Status code: {response.status_code}")
        #else:
        #    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            #exit()

        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")

        if url == "https://www.myjob.mu/Jobs/Accounting-Auditing-Tax-Services-Finance/?Page=5":
            proceed = False
        else:
            all_jobs = soup.find_all("div",class_="module job-result")
        
            for job in all_jobs:
                item = {}

                item['Title'] = job.find("h2").text
                item['Company Name'] = job.find("h3").text.strip()
                location_tag = job.find("li", class_="location").find("a")
                item['Location'] = location_tag.text.strip()
                salary_tag = job.find("li", class_="salary")
                item['Salary'] = salary_tag.text
                addeddate_tag = job.find("li", class_="updated-time")
                item['Created Date'] = addeddate_tag.text
                closeddate_tag = job.find("li", class_="closed-time")
                item['Closing Date'] = closeddate_tag.text
                item['Category'] = "Finance"
                item['Source'] = url
        
                #print(item['Title'])
                #print(item['Company Name'])
                #print(item['Location'])
                #print(item['Salary'])
                #print(item['Created Date'])
                #print(item['Closing Date'])
                #print(item['Category'])
                #print(item['Source'])
                data.append(item)
            
        current_page = current_page + 1
        #proceed = False
    return data
    
def scrape_tourismjobs_myjobmu():
    current_page = 1

    data = []

    proceed = True

    while(proceed):
        print("Currently scrapping Tourism category in myjob.mu page:"+str(current_page))

        #Variable for url page
        url = "https://www.myjob.mu/Jobs/Tourism-Travel/?Page="+str(current_page)

        # Fetch the web page
        response = requests.get(url)

        #if response.status_code == 200:
        #    page_content = response.text
        #    print(f"Succeed to retrieve the webpage. Status code: {response.status_code}")
        #else:
        #    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            #exit()

        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")

        if url == "https://www.myjob.mu/Jobs/Tourism-Travel/?Page=5":
            proceed = False
        else:
            all_jobs = soup.find_all("div",class_="module job-result")
        
            for job in all_jobs:
                item = {}

                item['Title'] = job.find("h2").text
                item['Company Name'] = job.find("h3").text.strip()
                location_tag = job.find("li", class_="location").find("a")
                item['Location'] = location_tag.text.strip()
                salary_tag = job.find("li", class_="salary")
                item['Salary'] = salary_tag.text
                addeddate_tag = job.find("li", class_="updated-time")
                item['Created Date'] = addeddate_tag.text
                closeddate_tag = job.find("li", class_="closed-time")
                item['Closing Date'] = closeddate_tag.text
                item['Category'] = "Tourism"
                item['Source'] = url
        
                #print(item['Title'])
                #print(item['Company Name'])
                #print(item['Location'])
                #print(item['Salary'])
                #print(item['Created Date'])
                #print(item['Closing Date'])
                #print(item['Category'])
                #print(item['Source'])
                data.append(item)
            
        current_page = current_page + 1
        #proceed = False
    return data

def scrape_pharmajobs_myjobmu():
    current_page = 1

    data = []

    proceed = True

    while(proceed):
        print("Currently scrapping Pharmaceutical category in myjob.mu page:"+str(current_page))

        #Variable for url page
        url = "https://www.myjob.mu/Jobs/Pharmaceutical-Science/?Page="+str(current_page)

        # Fetch the web page
        response = requests.get(url)

        #if response.status_code == 200:
        #    page_content = response.text
        #    print(f"Succeed to retrieve the webpage. Status code: {response.status_code}")
        #else:
        #    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            #exit()

        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")

        if url == "https://www.myjob.mu/Jobs/Pharmaceutical-Science/?Page=5":
            proceed = False
        else:
            all_jobs = soup.find_all("div",class_="module job-result")
        
            for job in all_jobs:
                item = {}

                item['Title'] = job.find("h2").text
                item['Company Name'] = job.find("h3").text.strip()
                location_tag = job.find("li", class_="location").find("a")
                item['Location'] = location_tag.text.strip()
                salary_tag = job.find("li", class_="salary")
                item['Salary'] = salary_tag.text
                addeddate_tag = job.find("li", class_="updated-time")
                item['Created Date'] = addeddate_tag.text
                closeddate_tag = job.find("li", class_="closed-time")
                item['Closing Date'] = closeddate_tag.text
                item['Category'] = "Pharmaceutical"
                item['Source'] = url
        
                #print(item['Title'])
                #print(item['Company Name'])
                #print(item['Location'])
                #print(item['Salary'])
                #print(item['Created Date'])
                #print(item['Closing Date'])
                #print(item['Category'])
                #print(item['Source'])
                data.append(item)
            
        current_page = current_page + 1
        #proceed = False
    return data

def scrape_legaljobs_myjobmu():
    current_page = 1

    data = []

    proceed = True

    while(proceed):
        print("Currently scrapping Legal category in myjob.mu page:"+str(current_page))

        #Variable for url page
        url = "https://www.myjob.mu/Jobs/Legal/?Page="+str(current_page)

        # Fetch the web page
        response = requests.get(url)

        #if response.status_code == 200:
        #    page_content = response.text
        #    print(f"Succeed to retrieve the webpage. Status code: {response.status_code}")
        #else:
        #    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            #exit()

        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")

        if url == "https://www.myjob.mu/Jobs/Legal/?Page=5":
            proceed = False
        else:
            all_jobs = soup.find_all("div",class_="module job-result")
        
            for job in all_jobs:
                item = {}

                item['Title'] = job.find("h2").text
                item['Company Name'] = job.find("h3").text.strip()
                location_tag = job.find("li", class_="location").find("a")
                item['Location'] = location_tag.text.strip()
                salary_tag = job.find("li", class_="salary")
                item['Salary'] = salary_tag.text
                addeddate_tag = job.find("li", class_="updated-time")
                item['Created Date'] = addeddate_tag.text
                closeddate_tag = job.find("li", class_="closed-time")
                item['Closing Date'] = closeddate_tag.text
                item['Category'] = "Legal"
                item['Source'] = url
        
                #print(item['Title'])
                #print(item['Company Name'])
                #print(item['Location'])
                #print(item['Salary'])
                #print(item['Created Date'])
                #print(item['Closing Date'])
                #print(item['Category'])
                #print(item['Source'])
                data.append(item)
            
        current_page = current_page + 1
        #proceed = False
    return data

    #df = pd.DataFrame(data)
    #df.to_excel("jobs.xlsx", index=False, engine='openpyxl')

    return data

#if __name__ == "__main__":
#    jobs = scrape_jobs_myjobmu()
#    for job in jobs:
#        print(job)
