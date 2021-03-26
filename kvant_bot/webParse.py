from bs4 import BeautifulSoup
import requests
from datetime import datetime
news_url = 'http://kvantorium.iroso.ru/news'
news_already = []
def get_html(url):
	result = requests.get(url)
	return result.text

def get_title(html):
	soup = BeautifulSoup(html, 'lxml')
	title = soup.find('h5').text
	return title

def get_url(html):
	soup = BeautifulSoup(html, 'lxml')
	url = soup.find('h5').find('a').get('href')
	return url
def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	data = soup.find('span', class_='short-news_date').text
	return data

def main():
	url = get_url(get_html('http://kvantorium.iroso.ru/news'))
	print(url)
main()


