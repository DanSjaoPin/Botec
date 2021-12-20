import sqlite3
from datetime import date
import traceback

try:
	base = sqlite3.connect('CocksBase.bd')
	print('Connected to DataBase')
except:
	print('Failed connect to DataBase')

cockBD = base.cursor()

cockBD.execute("CREATE TABLE IF NOT EXISTS cock(user_id text PRIMARY KEY, DolbaebName text, DolbaebLastName text, chat_id int, length int, last_commit_date text)")

base.commit()
base.close()

def CockUpdate(id, DolbaebLastName, DolbaebName, chat_id, plus):
    base = sqlite3.connect('CocksBase.bd')
    cockBD = base.cursor()
    cockBD.execute("SELECT length FROM cock WHERE user_id = '%s'" % (id))
    check = cockBD.fetchone()

    if check == None:
        try:
            row = (str(id), str(DolbaebName), str(DolbaebLastName), chat_id, 0, str(date.today()), 0)
            cockBD.execute("INSERT INTO cock VALUES(?, ?, ?, ?, ?, ?, ?)", row)
            base.commit()
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())

    if plus == 666:
    	cockBD.execute("UPDATE cock SET length = length * 2 WHERE user_id = '%s'" % (id))
    elif plus == 1488:
    	cockBD.execute("UPDATE cock SET length = %d WHERE user_id = '%s'" % (0, id))
    else:
    	cockBD.execute("UPDATE cock SET length = length + %d WHERE user_id = '%s'" % (plus, id))

    cockBD.execute("UPDATE cock SET last_commit_date = '%s', chat_id = %s WHERE user_id = '%s'" % (date.today(), chat_id, id))
    base.commit()
    base.close()