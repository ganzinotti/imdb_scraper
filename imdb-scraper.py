import requests
from bs4 import BeautifulSoup


def _beautiful_soup(url):
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'lxml')

    movie = {}
    try:
        title = soup.find("h1", itemprop="name").text.strip().strip()
    except:
        title = 'Unavailable'
    movie['title'] = title

    try:
        releaseyear = soup.find("span", id="titleYear").text.strip()
    except:
        releaseyear = 'Unavailable'
    movie['releaseyear'] = releaseyear

    try:
        duration = soup.find("time", itemprop="duration").text.strip()
    except:
        duration = 'Unavailable'
    movie['duration'] = duration

    try:
        plot = soup.find("div", itemprop="description").text.strip()
    except:
        plot = 'Unavailable'
    movie['plot'] = plot

    try:
        rating = soup.find("span", itemprop="ratingValue").text.strip()
    except:
        rating = 'Unavailable'
    movie['rating'] = rating

    try:
        votes = soup.find("span", itemprop="ratingCount").text.strip()
    except:
        votes = 'Unavailable'
    movie['votes'] = votes

    try:
        awards = soup.find("span", itemprop="awards").text.strip()
    except:
        awards = 'Unavailable'
    movie['awards'] = awards

    genres = soup.find_all("span", itemprop="genre")
    genre_string = ''
    for i, val in enumerate(genres):
        if i < len(genres) - 1:
            genre_string += val.text + ', '
        else:
            genre_string += val.text

    if genre_string == '':
        genres = 'Unavailable'
    else:
        genres = genre_string
    movie['genres'] = genres

    try:
        director = soup.find("span", itemprop="director").text.strip()
    except:
        director = 'Unavailable'
    movie['director'] = director

    actors = soup.find_all("span", itemprop="actors")
    actor_string = ''
    for i, actor in enumerate(actors):
        if i < len(actors) - 1:
            actor_string += actor.a.span.text + ', '
        else:
            actor_string += actor.a.span.text

    if actor_string == '':
        actors = 'Unavailable'
    else:
        actors = actor_string
    movie['actors'] = actors

    try:
        imgurl = soup.find("div", {"class": "poster"}).img['src']
    except:
        imgurl = "/static/images/not_available.jpg"
    movie['imgurl'] = imgurl

    return movie


movie = _beautiful_soup('http://www.imdb.com/title/tt3748528')
print(movie)