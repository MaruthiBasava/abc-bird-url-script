from bs4 import BeautifulSoup
import requests
from linker import Linker

link = Linker()


def format_url():
    base_url = "https://web.archive.org/web/"
    date = "20001017050155/"
    return base_url + date + link.getNextLink()


def get_answers(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    result = soup.find('span', class_='H1')

    if result == None:
        result = soup.find('h1', {"align":"center"})
        if result == None:
            return "[FAILED]"

    return result.text


def add_all_titles(length):
    for _ in range(length):
        get_answers(format_url())


add_all_titles(20)

