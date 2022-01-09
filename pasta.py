from bs4 import BeautifulSoup
import requests

def pasta():
	url = 'https://pastach.ru/p/random'
	page = requests.get(url)

	soup = BeautifulSoup(page.text, 'html.parser') 

	title = soup.find('h1', class_='header-title')
	body = soup.find('section', class_='paste-content')
	link = 'https://pastach.ru/p/' + soup.find_all("a")[6].text[1:]

	past = str(title.text) + '\n' + str(body.text) + '\n\n' + str(link)

	return(past)


 

