import imp
from bs4 import BeautifulSoup
import requests
import random
from danek import danek


def anek():
	url = 'https://baneks.ru/random'
	page = requests.get(url)

	soup = BeautifulSoup(page.text, 'html.parser')

	anek = soup.find('p')

	return(anek.text)

def Danek():
	i = random.randrange(len(danek))
	return danek[i]