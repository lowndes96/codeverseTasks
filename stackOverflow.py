import requests
from bs4 import BeautifulSoup
import re 

url = "https://stackoverflow.com/?tab=month" 

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')

    questions = []

    for question in soup.select('.s-post-summary'): #selects and loops through each div with the specified class 
        title_element = question.select_one('.s-post-summary--content-title') #finds post title 
        stats_element = question.find('div') #finds all stats (votes, answers, views )

        title = title_element.get_text(strip=True) if title_element else None #get text from both elements 
        stats = stats_element.get_text(strip=True) or '0votes0answer0views' #gets text, or asigns with string listed

        vote_element = re.search('\d+(?=votes)', stats)
        answers_element = re.search('\d+(?=answer)', stats)
        views_element = re.search('\d+(?=views)', stats)

        #these if/else statements default votes to zero if the regex does not work 
        #repetative and could be refactored with loop through list/dict - but wanted to check the logic first 
        if vote_element: 
            votes = vote_element.group()
        else: 
            votes = '0'
        if answers_element:
            answers = answers_element.group()
        else: 
            answers = '0'
        if views_element:
            views = views_element.group()
        else: 
            views = '0'

        questions.append({
            'title': title,
            'votes': votes,
            'answers': answers,
            'views': views,
        })

    print(questions)

else:
    print("Failed to retrieve the page. Status code:", page.status_code)