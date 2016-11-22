from bs4 import BeautifulSoup
import requests
from linker import Linker
import re
from urllib.error import HTTPError


link = Linker()


def format_url():
    base_url = "https://web.archive.org/web/"
    date = "20001017050155/"
    return base_url + date + link.getNextLink()


def format_title_to_url(result):
    a = result.text
    b = remove_non_ascii(a)
    c = re.sub('\s+', ' ', b).strip()
    d = c.replace(" ", "-")
    return d.replace(" ", "")


def get_parsed_title(url): #gets title and parses it
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    result = soup.find('span', class_='H1')

    if result is None:
        result = soup.find('h1', {"align": "center"})
        if result is None:
            return "no-wayback"

    return format_title_to_url()


def remove_non_ascii(s):
    return "".join(i for i in s if (ord(i) == 32 or ord(i) >= 65 <= 90 or ord(i) >= 97 <= 122 or ord(i) >= 48 <= 57))


def return_working_title(url):
    try:
        ppage = requests.get(url)

        soup = BeautifulSoup(ppage.text, 'html.parser')

        if "404 " in soup.text:
            return "not in new site"
    except HTTPError:
        return "NOT ON NEW SITE"

    return url


def add_all_links(a,b): #will add the link or note to the sheet
    link.rowNum = a
    for i in range(a,b):
        a = get_parsed_title(format_url())
        current_link = return_working_title("https://abcbirds.org/" + a)
        print(str(i) + " " + a + "  \n  " + "https://abcbirds.org/" + a)

        if a == 'no-wayback' or a is 'no-wayback':
            link.addNote("no-wayback-machine")
            print('WAYBACK')
        else:
            link.addNote(current_link)

    link.save()

try:
    add_all_links(987,link.length())
except:
    link.save()
    print("FAILED")
    raise
