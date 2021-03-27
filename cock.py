import sqlite3
from datetime import date
import random
from CocksBase import CockUpdate

import vk_api, json
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import main_token

vk_session = vk_api.VkApi(token = main_token)
global vk
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 203331529)

def sender(id, text):
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : get_random_id()})

base = sqlite3.connect('CocksBase.bd')
cockBD = base.cursor();

def CockChange(dolbaebID, dolbaebF, dolbaebN, id):
	cockBD.execute(f"SELECT last_commit_date FROM cock WHERE user_id = '%s'" % (dolbaebID))
	lastCommitDate = cockBD.fetchone()
	for simbol in str(lastCommitDate):
		if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'":
			newd = str(lastCommitDate).replace(simbol, '')
			lastCommitDate = str(newd)
	if lastCommitDate == str(date.today()):
		sender(id, '*id%d(%s %s), на сегодня хватит кока, залетай завтра - повторим' % (dolbaebID, dolbaebF, dolbaebN))

	else:
		plus = 0
		chance = random.randrange(1, 100)

		if chance > 0 and chance <= 40:
			plus = random.randrange(10)
			sender(id, 'Кок *id%d(%s %s) вырос на %d см!' % (dolbaebID, dolbaebF, dolbaebN, plus))

		elif chance > 40 and chance <= 70:
			plus = random.randrange(10, 15)
			sender(id, 'Кок *id%d(%s %s) вырос на %d см!' % (dolbaebID, dolbaebF, dolbaebN, plus))

		elif chance > 70 and chance <= 90:
			plus = random.randrange(15, 20)
			sender(id, 'Кок *id%d(%s %s) вырос на %d см!' % (dolbaebID, dolbaebF, dolbaebN, plus))

		elif chance > 90 and chance <= 99:
			plus = random.randrange(-15, 0)
			sender(id, 'Кок *id%d(%s %s) объевреился на %d см!\nСаси' % (dolbaebID, dolbaebF, dolbaebN, plus))

		elif chance == 100:
			plus = random.randrange(3)
			if plus == 1 or plus == 3:
				sender(id, 'Кок *id%d(%s %s) вырос в 2 раза!' % (dolbaebID, dolbaebF, dolbaebN))
				plus = 666
			elif plus == 2:
				sender(id, 'Кок *id%d(%s %s) отвалился!\nЛох))0)' % (dolbaebID, dolbaebF, dolbaebN))
				plus = 1488

		CockUpdate(dolbaebID, dolbaebN, dolbaebF, id, plus)

		cockBD.execute("SELECT length FROM cock WHERE user_id = '%s'" % (dolbaebID))
		length = str(cockBD.fetchone())

		for simbol in length:
			if simbol == '(' or simbol == ',' or simbol == ')':
				newlength = length.replace(simbol, '')
				length = newlength

		if int(length) >= 0:
			sender(id, 'Длина кока *id%s(%s %s): %s см' % (dolbaebID, dolbaebF, dolbaebN, length))
		else:
			for simbol in str(length):
				if simbol == '-':
					new =  str(length).replace(simbol, '')
					length = new
			sender(id, 'Глубина пизды *id%s(%s %s): %s см' % (dolbaebID, dolbaebF, dolbaebN, length))

def CocksTop(chat_id, id):
	cockBD.execute("UPDATE cock SET chat_id = %s WHERE user_id = '%s'" % (chat_id, id))
	base.commit()
	cockBD.execute("SELECT DolbaebName FROM cock WHERE chat_id = '%s' ORDER BY length DESC" % (chat_id))
	N = cockBD.fetchall()
	cockBD.execute("SELECT DolbaebLastName FROM cock WHERE chat_id = '%s' ORDER BY length DESC" % (chat_id))
	LN = cockBD.fetchall()
	cockBD.execute("SELECT length FROM cock WHERE chat_id = '%s' ORDER BY length DESC" % (chat_id))
	L = cockBD.fetchall()
	i = 0
	CT = 'Топ коков:\n'

	for l in L:
		for simbol in str(N[i]):
			if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'":
				new =  str(N[i]).replace(simbol, '')
				N[i] = new

		for simbol in str(LN[i]):
			if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'":
				new = str(LN[i]).replace(simbol, '')
				LN[i] = new

		for simbol in str(L[i]):
			if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'":
				new = str(L[i]).replace(simbol, '')
				L[i] = new

		CT += "%s. %s %s —  %s см\n" % (i + 1, N[i], LN[i], L[i])
		i += 1
	sender(chat_id, CT)
