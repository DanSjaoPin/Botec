import sqlite3
from datetime import date
import random
from CocksBase import CockUpdate
from sender import sender
from format import format

base = sqlite3.connect('CocksBase.bd')
cockBD = base.cursor()

def CockChange(dolbaebID, dolbaebF, dolbaebN, id):
	cockBD.execute(f"SELECT last_commit_date FROM cock WHERE user_id = '%s'" % (dolbaebID))
	lastCommitDate = cockBD.fetchone()
	
	lastCommitDate = format(lastCommitDate)

	if lastCommitDate == str(date.today()):
		sender(id, '%s %s, на сегодня хватит кока, залетай завтра - повторим' % (dolbaebF, dolbaebN))

	else:
		plus = 0
		chance = random.randrange(1, 101)

		if chance > 0 and chance <= 40:
			plus = random.randrange(10)
			sender(id, 'Кок %s %s вырос на %d см!' % (dolbaebF, dolbaebN, plus))

		elif chance > 40 and chance <= 70:
			plus = random.randrange(10, 15)
			sender(id, 'Кок %s %s вырос на %d см!' % (dolbaebF, dolbaebN, plus))

		elif chance > 70 and chance <= 78:
			plus = random.randrange(15, 20)
			sender(id, 'Кок %s %s вырос на %d см!' % (dolbaebF, dolbaebN, plus))

		elif chance > 78 and chance <= 97:
			plus = random.randrange(-25, 0)
			sender(id, 'Кок %s %s объевреился на %d см!\nСаси' % (dolbaebF, dolbaebN, plus))

		elif chance > 97 and chance <= 99:
			sender(id, 'Кок *%s %s вырос в 2 раза!' % (dolbaebF, dolbaebN))
			plus = 666

		elif chance == 100:
			sender(id, 'Кок %s %s отвалился!\nЛох))0)' % (dolbaebF, dolbaebN))
			plus = 1488

		CockUpdate(dolbaebID, dolbaebN, dolbaebF, id, plus)

		cockBD.execute("SELECT length FROM cock WHERE user_id = '%s'" % (dolbaebID))
		length = str(cockBD.fetchone())

		length = format(length)

		if int(length) >= 0:
			sender(id, 'Длина кока %s %s: %s см' % (dolbaebF, dolbaebN, length))
		else:
			for simbol in str(length):
				if simbol == '-':
					new =  str(length).replace(simbol, '')
					length = new
			sender(id, 'Глубина пизды %s %s: %s см' % (dolbaebF, dolbaebN, length))

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
		NN = format(N[i])
		LNN = format(LN[i])
		LL = format(L[i])

		CT += "%s. %s %s —  %s см\n" % (i + 1, NN, LNN, LL)
		i += 1
		
	sender(chat_id, CT)
