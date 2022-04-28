from pasta import pasta
from anek import *
from say import say
from fuck import fuck
from menu import menu
from reit import Reit
import random
from fap import fapContent
from sender import sender, longpoll, vk, VkBotEventType
import traceback
from datetime import datetime
from format import formatInput
from cock import CockChange, CocksTop
from roll import Roll
from FaggotOfTheDay import FagsCreate, WhoIsFaggot
from WhoIsMe import WhoIsMe
from Weather import GetWeather
from POSLAT import *
from Pics import ChoosePicType
FagsCreate()

while True:
	try:
		for event in longpoll.listen():
			try:
				if event.type == VkBotEventType.MESSAGE_NEW:

					ts = int(event.message.date)
					dateNtime = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
					logMessage = "\n\n---\nFrom User: 'id%s'   From Chat: '%s'   Date'N'Time: '%s'\n '%s'\n---" % (
						event.message.from_id, event.chat_id, dateNtime, event.message.text)
					print(logMessage)

					if event.message.peer_id != event.message.from_id:
						msg = event.message.text.lower()
						id = event.chat_id
						try:
							dolbaeb = vk.users.get(user_ids=event.message.from_id)[0]
						except:
							print("\n--------------------------------------------------------кракнувса-------------------------------------------------------\n")

						if len(msg) >= 1:
							msg = formatInput(msg)

							if msg == 'бот':
								if dolbaeb['id'] == 182821666:
									sender(id, 'Здорова, Батя!))0)')
								else:
									sender(id, 'Иди нахуй, %s %s' %
										(dolbaeb['first_name'], dolbaeb['last_name']))
							
							elif msg in POSLAT:
								sender(id, 'Иди нахуй' + OTVET[random.randint(0, len(OTVET)-1)])

							elif msg == 'бот меню':
								sender(id, menu)

							#elif msg.startswith('кай') or msg.startswith('s g d'):
							#	msg_id = event.message.conversation_message_id
							#	vk.messages.delete(peer_id=2000000000 + id,
							#					delete_for_all=1, cmids=msg_id)
								
							#elif event.message.from_id == -170393012:
							#	sender(id, 'А Кай педик ебанный.))0)')

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

							elif msg == 'ботик':
								sender(id, 'Мя ^.^')

							elif msg == 'ботец':
								sender(id, 'Сосни хуец, педрила')

							elif msg == '()':
								sender(id, 'Гы, пизда.))0)')

							elif msg[0] == ')' or msg[-1] == ')':
								sender(id, '))0)')

							elif msg == ':с' or msg == ':(' or msg[0] == '(' or msg[-1] == '(' or msg == '😔':
								sender(id, 'Думай позитивно - стакан всегда наполовину полон, всегда\nТолько не думай что в стакане\nДумай, что в стакане вода')

							elif msg == 'кок бот':
								sender(id, 'Ты шо, дурак блять?')

							elif msg == 'бот ролл':
								sender(id, Roll())

							elif msg == 'бот фап':
								sender(id, fapContent[random.randint(0, len(fapContent)-1)])

							elif msg == 'бот почитать':
								try:
									sender(id, pasta())
								except Exception as e:
									print('Ошибка:\n', traceback.format_exc())
								
							elif msg == 'бот анек':
								try:
									sender(id, anek())
								except Exception as e:
									print('Ошибка:\n', traceback.format_exc())

							elif msg == 'бот данек':
								sender(id, Danek())
							
							elif msg.startswith('бот пикча'):
								ChoosePicType(id, msg)

							elif msg == 'бот кок':
								sender(id, CockChange(dolbaeb['id'], dolbaeb['first_name'],
                                                                    dolbaeb['last_name'], id))

							elif msg == 'бот топ коков':
								sender(id, CocksTop(id, dolbaeb['id']))

							elif msg == 'бот пидор дня':
								WhoIsFaggot(id, dolbaeb['id'])

							elif msg == 'бот абсолют':
								sender(id, Reit(dolbaeb['id']))

							elif msg == 'бот хочу ебаться':
								sender(id, fuck(id, dolbaeb['id'], dolbaeb['first_name'], dolbaeb['last_name']))

							elif msg[:9] == 'бот скажи':
								sender(id, say(msg[9:]))

							elif msg == 'бот кто я':
								sender(id, WhoIsMe(
									dolbaeb['id'], dolbaeb['first_name'], dolbaeb['last_name']))
							
							elif msg.startswith('бот погода'):
								sender(id, GetWeather(msg[11:]))

							elif dolbaeb['id'] == 182821666 and msg == 'бот призываю тебя заебать всех нахуй':
								sender(id, 'Пагнали наши городские!')
								i = 1
								while i <= 666:
									sender(id, '@all %d/666' % i)
									i += 1

							elif msg == 'бот сидеть':
								sender(id, """Держи


                                                _____________¶¶¶¶¶¶¶¶¶
                                                _____________¶¶¶¶¶¶¶¶¶
                                                _____________¶¶¶¶¶¶¶¶¶
                                                _____________¶¶¶¶¶¶¶¶¶
                                                _____________88888888
                                                _____________¶¶¶¶¶¶¶¶¶
                                                _____________¶¶¶¶¶¶¶¶¶
                                                _____________¶¶¶¶¶¶¶¶¶
                                                _____________¶¶¶¶¶¶¶¶¶
                                                ____________¶¶¶¶¶¶¶¶¶¶¶
                                                ___________¶¶¶¶¶¶¶¶¶¶¶¶¶
                                                __________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                                                _________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                                                _________¶¶¶|___________|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|11Сваяк11|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|111111111|¶¶¶
                                                _________¶¶¶|___________|¶¶¶
                                                _________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
								""")
			except:
				print("\n--------------------------------------------------------Кракнувса-------------------------------------------------------\n")
	except:
		print("\n--------------------------------------------------------Зломавса-------------------------------------------------------\n")
