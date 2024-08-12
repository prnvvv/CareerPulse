import requests
from bs4 import BeautifulSoup
import pandas as pd

def courses_webscraped_function(course_name):
    
    course_split =  course_name.split()

    if(len(course_split) == 1):
        url = f"https://www.coursera.org/search?query={course_split[0]}"

    elif(len(course_split) == 2):
        url = f"https://www.coursera.org/search?query={course_split[0]}%20{course_split[1]}"

    elif(len(course_split) == 3):
        url = f"https://www.coursera.org/search?query={course_split[0]}%20{course_split[1]}%20{course_split[2]}"

    elif(len(course_split) == 4):
        url = f"https://www.coursera.org/search?query={course_split[0]}%20{course_split[1]}%20{course_split[2]}%20{course_split[3]}"

    elif(len(course_split) == 4):
        url = f"https://www.coursera.org/search?query={course_split[0]}%20{course_split[1]}%20{course_split[2]}%20{course_split[3]}%20{course_split[4]}"
    
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    educators_list = []
    educators = soup.find_all("p", class_ = "cds-ProductCard-partnerNames css-vac8rf")
    for educator in educators[:5]:
        educators_list.append(educator.text)

    course_titles_list = []
    course_titles = soup.find_all("h3", class_ = "cds-CommonCard-title css-6ecy9b")
    for title in course_titles[:5]:
        course_titles_list.append(title.text)

    skills_list = []
    skills = soup.find_all("div", class_ = "cds-CommonCard-bodyContent")
    for skill in skills[:5]:
        skills_list.append(skill.text)

    ratings_list = []
    ratings = soup.find_all("p", class_ = "css-2xargn")
    for rating in ratings[:5]:
        ratings_list.append(rating.text)

    hyperlinks_list = []
    hyperlinks = soup.find_all("a", class_ = "cds-119 cds-113 cds-115 cds-CommonCard-titleLink css-si869u cds-142")
    for hyperlink in hyperlinks[: 5]:
        hyperlinks_list.append("https://www.coursera.org/" + hyperlink["href"])

    levels_list = []
    levels = soup.find_all("div", class_ = "cds-CommonCard-metadata")
    for level in levels[: 5]:
        level = level.text.split()
        levels_list.append(level[0])

    courses_dataframe = pd.DataFrame({"Course Title": course_titles_list, "Educators": educators_list, "Skills You'll Gain": skills_list, "Skill Level": levels_list, "Ratings": ratings_list, "Hyperlink": hyperlinks_list})

    return courses_dataframe

print(courses_webscraped_function("Machine Learning"))