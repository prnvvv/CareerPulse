import requests
from bs4 import BeautifulSoup
import pandas as pd


job_name = input("Enter job name: ")

job_name_split = job_name.split()

job_name_title = job_name.title()

if(len(job_name_split) == 1):
    url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText="{job_name_title}"&txtKeywords={job_name_split[0]}&txtLocation='

elif(len(job_name_split) == 2):
    url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText="{job_name_title}"&txtKeywords={job_name_split[0]}+{job_name_split[1]}&txtLocation='

elif(len(job_name_split) == 3):
    url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText="{job_name_title}"&txtKeywords={job_name_split[0]}+{job_name_split[1]}+{job_name_split[2]}&txtLocation='

elif(len(job_name_split) == 4):
    url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText="{job_name_title}"&txtKeywords={job_name_split[0]}+{job_name_split[1]}+{job_name_split[2]}+{job_name_split[3]}&txtLocation='

elif(len(job_name_split) == 4):
    url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText="{job_name_title}"&txtKeywords={job_name_split[0]}+{job_name_split[1]}+{job_name_split[2]}+{job_name_split[3]}+{job_name_split[4]}&txtLocation='

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

job_titles_list = []
job_titles_list_final = []
job_titles = soup.find_all("strong", class_ = "blkclor")
for job_title in job_titles[: 10]:
    job_titles_list.append(job_title.text)

for i in range(0, len(job_titles_list) - 1, 2):
    job_title = job_titles_list[i] + " " + job_titles_list[i + 1]
    job_titles_list_final.append(job_title)

print(job_titles_list_final)

