import vk_api, json
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import main_token
from cock import CockChange, CocksTop
from roll import Roll

vk_session = vk_api.VkApi(token = main_token)
global vk
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 203331529)

while True:
	try:
		longpoll = VkBotLongPoll(vk_session, 203331529)
	except:
		print("Зломався")

def sender(id, text):
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : get_random_id()})

while True:
	try:
		for event in longpoll.listen():
			try:
				if event.type == VkBotEventType.MESSAGE_NEW:
					print(event)
					if event.message.peer_id != event.message.from_id:
						msg = event.message.text.lower()
						id = event.chat_id
						try:
							dolbaeb = vk.users.get(user_ids=event.message.from_id)[0]
						except:
							print("\n--------------------------------------------------------Кракнувса-------------------------------------------------------\n")

						if len(msg) >= 1:
							for simbol in msg:
								if simbol == ',' or simbol == '.' or simbol == '!' or simbol == '?':
									newmsg = msg.replace(simbol, '')
									msg = newmsg

							if dolbaeb['id'] == 162958234:
								sender(id, 'Броооооо *id%d(🖤)' % dolbaeb['id'])

							if msg == 'бот':
								sender(id, 'Иди нахуй, *id%d(%s %s)' % (dolbaeb['id'], dolbaeb['first_name'], dolbaeb['last_name']))

							elif msg == 'бот меню':
								str = ''
								with open("menu.txt", "r") as menu:
									for line in menu:
										str += line
									sender(id, str)
								menu.close()

							elif msg == 'я':
								sender(id, 'Головка от хуя')

							elif msg == 'кок':
								sender(id, 'кок')

							elif msg == 'бiбр' or msg == 'бібр' or msg == 'бибр' or msg == 'бобр'')':
								sender(id, 'Бiбр.')

							elif msg == 'ы':
								sender(id, 'Гы))0)')

							elif msg == ':0':
								sender(id, '0:')

							elif msg == '0:':
								sender(id, ':0')

							elif msg == '()':
								sender(id, 'Гы, пизда.))0)')

							elif msg[0] == ')' or msg[-1] == ')':
								sender(id, '))0)')

							elif msg == ':с' or msg == ':(' or msg[0] == '(' or msg[-1] == '(' or msg == '😔':
								sender(id, 'Думай позитивно - стакан всегда наполовину полон, всегда\nТолько не думай что в стакане\nДумай, что в стакане вода')

							elif msg == 'бот ролл':
								Roll()
								dice = Roll()
								sender(id, dice)

							elif msg == 'кок бот':
								sender(id, 'Ты шо, дурак блять?')

							elif msg == 'бот кок':
								CockChange(dolbaeb['id'], dolbaeb['first_name'], dolbaeb['last_name'], id)

							elif msg == 'бот топ коков':
								CocksTop(id, dolbaeb['id'])

							elif dolbaeb['id'] == 182821666 and msg == 'бот призываю тебя заебать всех нахуй':
								sender(id, 'Пагнали наши городские!')
								i = 1
								while i <= 666:
									sender(id, '@all %d/666' % i)
									i += 1

			except:
				print("\n--------------------------------------------------------Кракнувса-------------------------------------------------------\n")
	except:
		print("Зломався")