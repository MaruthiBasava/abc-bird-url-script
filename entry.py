from bs4 import BeautifulSoup
import requests
from linker import Linker
import re
from urllib.request import Request, urlopen
from urllib.error import HTTPError


link = Linker()
current_row = 0

def format_url():
    base_url = "https://web.archive.org/web/"
    date = "20001017050155/"
    return base_url + date + link.getNextLink()


def format_title_to_url(result):
    a = result.text
    b = re.sub('-',' ', a).strip()
    c = re.sub('\s+',' ', b).strip()
    d = remove_non_ascii(c)
    e = d.replace(" ","-")
    return e


def get_title_from_wayback(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    result = soup.find('span', class_='H1')

    if result is None:
        result = soup.find('h1', {"align": "center"})
        if result is None:
            return "no-wayback"

    return format_title_to_url(result)


def remove_non_ascii(s):
    s.lower()
    return "".join(i for i in s if (ord(i) == 32 or ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122 or ord(i) >= 48 and ord(i)<= 57))


def return_working_title(url):

    hdr = {'User-agent': 'Mozilla/5.0'}
    req = Request(url, headers=hdr)

    try:
        page = urlopen(req).read
        ppage = requests.get(url)

        soup = BeautifulSoup(ppage.text, 'html.parser')

        if "404 " in soup.text:
            return "not in new site"
    except HTTPError:
        return "NOT ON NEW SITE"

    return url


def add_all_links(a,b):
    link.rowNum = a
    for i in range(a,b):
        a = get_title_from_wayback(format_url())
        current_link = return_working_title("https://abcbirds.org/" + a)
        print(str(i) + " " + current_link + "  \n  " + "https://abcbirds.org/" + a)

        if a in 'no-wayback':
            link.addNote("no-wayback-machine")
            print('WAYBACK')
        else:
            link.addNote(current_link)

    link.save()

try:
    add_all_links(1,link.length())

except:
    link.save()
    add_all_links(current_row + 1)
    raise
