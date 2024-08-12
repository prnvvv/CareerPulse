import requests
from bs4 import BeautifulSoup
import pandas as pd


job_name = input("Enter job name: ")

job_name_split = job_name.split()

if(len(job_name_split) == 1):
    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords={job_name_split[0]}&txtLocation="

elif(len(job_name_split) == 2):
    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords={job_name_split[0]}+{job_name_split[1]}&txtLocation="

elif(len(job_name_split) == 3):
    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords={job_name_split[0]}+{job_name_split[1]}+{job_name_split[2]}&txtLocation="

elif(len(job_name_split) == 4):
    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords={job_name_split[0]}+{job_name_split[1]}+{job_name_split[2]}+{job_name_split[3]}&txtLocation="