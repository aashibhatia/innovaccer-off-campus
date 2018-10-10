from bs4 import BeautifulSoup
import urllib.request as urllib2
from imdb import IMDb

import requests

tv_series = IMDb()

print('TV Series: ')
name = str(input(''))
tv_series_name = tv_series.search_movie(name)[0]
series_id = tv_series.get_imdbID(tv_series_name)

url = 'https://www.imdb.com/title/tt' + series_id + '/'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
div = soup.find_all(class_='article')[1]

year = 2018
upcoming_year = 2019

for link in div.find_all('a', href=True, text='2019'):
	upcoming_year = link.text

if year < 2019 :
	prev_url = 'https://www.imdb.com/title/tt' + series_id + '/episodes?year=2018'
	prev_page = requests.get(prev_url)
	prev_soup = BeautifulSoup(prev_page.content, 'html.parser')
	prev_div = prev_soup.find_all(class_='airdate')[-1]
	text = prev_div.text
	text = text.replace('\n', '')
	text = text.replace(' ', '')
	s = list(text)
	year = ''.join(s)[-4:]

	if int(year, base=10) < 2019 and int(year, base=10) >= 2018:
		print('The last episode of season was aired on {}'.format(text))

	# for link in div.find_all('a', href=True, text='2018'):
		# if link.text == 2018:
		# print('Last episode was aired in year {}'.format(link.text))
	else:
		print('The season has been finished streaming!')
else:
	print('The season will start in the year {}'.format(upcoming_year))
