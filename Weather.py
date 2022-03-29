from urllib import response
import requests

API_KEY = "API_KEY"
LDNR = ['луганск', 'Луганск', 'lugansk', 'Lugansk',
        'Donetsk', 'donetsk', 'донецк', 'Донецк', 'dnr', 'DNR', 'днр', 'ДНР', 'ДНР', 'лнр', 'LNR', 'lnr', 'Донбас', 'донбас']


def GetWeather(city):
	s_city = city
	city_id = GetCityId(city)
	if city_id == "Блять, город введи нормально, кретин.":
		return "Блять, город введи нормально, кретин."

	try:
		res = requests.get("http://api.openweathermap.org/data/2.5/weather",
						params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': API_KEY})

		data = res.json()

		message = f"Место: {city.capitalize()}, {data['sys']['country']}\nТемпература: {data['main']['temp']}°C\nПа ашчушчэнням: {data['main']['feels_like']}°C\nВ окне: {data['weather'][0]['description']}\nВлажность трусиков: {data['main']['humidity']}%\nДует: {data['wind']['speed']}м/с\n"
		
		if city in LDNR:
			message += '\nОбстрелы из градов и прочей смертоубийственной хуйни прилагаются'

		return message

	except:
		return "Возникла какая-то ебучая ошибка. Похуй какая, главное, что ты И-Д-И-О-Т!"


def GetCityId(city):

	try:
		res = requests.get("http://api.openweathermap.org/data/2.5/find",
						params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': API_KEY})
		data = res.json()
		return data['list'][0]['id']
	except Exception as e:
		return "Блять, город введи нормально, кретин."
