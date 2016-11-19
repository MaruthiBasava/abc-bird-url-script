from bs4 import BeautifulSoup
import requests

base_url = "https://web.archive.org/web/"
date = "20161017050155/"
website = "https://www.google.com/"

def format_url(base_url,date,website):
    return base_url + date + website

def get_answers(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    results = soup.find_all('a')
    return [answer.text for answer in results]


a = format_url(base_url=base_url, date=date, website=website)

print(get_answers(a))
