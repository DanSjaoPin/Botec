import sqlite3
from datetime import date

try:
	base = sqlite3.connect('CocksBase.bd')
	print('Connected to DataBase')
except:
	print('Failed connect to DataBase')

cockBD = base.cursor()

cockBD.execute(f"CREATE TABLE IF NOT EXISTS cock(user_id text PRIMARY KEY, DolbaebName text, DolbaebLastName text, chat_id int, length int, last_commit_date text)")

base.commit()
base.close()

def CockUpdate(id, DolbaebLastName, DolbaebName, chat_id, plus):
	base = sqlite3.connect('CocksBase.bd')
	cockBD = base.cursor()
	cockBD.execute(f"SELECT length FROM cock WHERE user_id = '%s'" % (id))
	check = cockBD.fetchone()

	if check == None:
		row = (id, DolbaebName, DolbaebLastName, chat_id, 0, date.today())
		cockBD.execute("INSERT INTO cock VALUES(?, ?, ?, ?, ?, ?)", row)
		base.commit()

	if plus == 666:
		cockBD.execute("UPDATE cock SET length = length * 2 WHERE user_id = '%s'" % (id))
	elif plus == 1488:
		cockBD.execute("UPDATE cock SET length = %d WHERE user_id = '%s'" % (0, id))
	else:
		cockBD.execute("UPDATE cock SET length = length + %d WHERE user_id = '%s'" % (plus, id))

	cockBD.execute("UPDATE cock SET last_commit_date = '%s', chat_id = %s WHERE user_id = '%s'" % (date.today(), chat_id, id))
	base.commit()
	base.close()