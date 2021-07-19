import enum
from bs4 import BeautifulSoup
import requests, time

def fun():
    site_url=requests.get('https://www.shine.com/job-search/computer-engineering-jobs').text
    soup = BeautifulSoup(site_url, 'lxml')
    jobs = soup.find_all('div', class_ = 'w-90 ml-25')
    for index, job in enumerate(jobs):
        job_title = job.find('a', class_='job_title_anchor').text
        time = job.find('li', class_ = 'w-30 mr-10 result-display__profile__years').text.replace(' ','')
        more_info = job.h2.a['href']
        with open(f'files/{index}.txt', 'w') as f:
            f.write(f"Job title : {job_title}\n")
            f.write(f"uploaded time : {time}")
            f.write(f"More info : shine.com{more_info}")
if __name__=='__main__':
    while True:
        fun()
        time_wait=10
        print(f'Waiting {time_wait} Minutes..')
        time.sleep(time_wait*60)