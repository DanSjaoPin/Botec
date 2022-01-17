from bs4 import BeautifulSoup
import requests


def anek():
	url = 'https://baneks.ru/random'
	page = requests.get(url)

	soup = BeautifulSoup(page.text, 'html.parser')

	anek = soup.find('p')

	return(anek.text)
