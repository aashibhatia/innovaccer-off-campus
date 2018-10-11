from bs4 import BeautifulSoup
import urllib.request as urllib2
from imdb import IMDb

import requests
import sqlconnect

results = []
names = []
series = []
ids = []

def start():
    tv_series = IMDb()

    print('Email: ')
    email = str(input(''))

    print('How many TV-Series air date has to be reminded?')
    num = int(input())

    print('TV Series: ')

    for i in range(0,num):
	    name = str(input(''))
	    names.append(name)

    for series_name in names:
        title = tv_series.search_movie(series_name)[0]["title"]
        x = tv_series.search_movie(series_name)[0]
        series.append(title)
        y = tv_series.get_imdbID(x)
        ids.append(y)

        url = 'https://www.imdb.com/title/tt' + y + '/'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        div = soup.find_all(class_='article')[1]

        year = 2018

        for link in div.find_all('a', href=True, text='2019'):
            year = link.text

        if year == 2018:
            prev_url = 'https://www.imdb.com/title/tt' + y + '/episodes?year=2018'
            prev_page = requests.get(prev_url)
            prev_soup = BeautifulSoup(prev_page.content, 'html.parser')
            prev_div = prev_soup.find_all(class_='airdate')[-1]
            text = prev_div.text
            text = text.replace('\n', '')
            text = text.replace(' ', '')
            s = list(text)
            year = ''.join(s)[-4:]

            if int(year, base=10) == 2018:
                status = 'The last episode of season was aired on {}'.format(text)
                results.append(status)
            else:
                status = 'The season has been finished streaming!'
                results.append(status)
        else:
            status = 'The season will start in the year {}'.format(year)
            results.append(status)

    # sqlconnect.store_in_database(email, series)
    return results

def get_series_id():
    return ids

def get_series():
    return series