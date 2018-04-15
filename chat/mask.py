import re
import requests
from bs4 import BeautifulSoup


def search_list(film):
    film = "+".join(film.split())
    base = "https://movie.naver.com"
    movies = "/movie/search/result.nhn?query={}&section=all&ie=utf8".format(film)
    prereq = requests.get(base + movies)
    presoup = BeautifulSoup(prereq.content, "html.parser")
    atag = presoup.find("a", {"href": re.compile(r'.movie[&].'), "class": "more_list"})
    if atag:
        link = atag.get("href")
    else:
        link = presoup.find('a',{'href': re.compile(r'.section=movie[&]query=.')}).get('href')
    filmlist = []
    page = 1
    while 1:
        req = requests.get(base + link + "&page={}".format(page))
        soup = BeautifulSoup(req.content, "html.parser")
        lis = [
            li for li in soup.find('ul', {'class': 'search_list_1'}).find_all('li')
            if "출연" in li.find('dl').find_all('dd', {'class': 'etc'})[1].text
               and "감독" in li.find('dl').find_all('dd', {'class': 'etc'})[1].text
        ]
        for li in lis:
            code = li.find('a', {'href': re.compile(r'^/movie/bi/mi')}).get('href').split('=')[-1]
            image = li.find('img').get('src')
            name = li.find('dt').text
            genre = ", ".join([gen.text for gen in li.find_all('a', {'href': re.compile(r'.genre.')})])
            nation = ", ".join([nat.text for nat in li.find_all('a', {'href': re.compile(r'.nation.')})])
            people = li.find_all('dd', {'class': 'etc'})[1].text.lstrip('감독 : ').split('|출연 : ')
            director = people[0]
            actor = people[1]
            filmlist.append((code, name, image, genre, nation, director, actor))
        if not soup.find("td", {"class": "next"}):
            break
        page += 1
    return filmlist
