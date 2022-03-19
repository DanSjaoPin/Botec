from soupsieve import select
from WhoIsMeList import *
import random
import sqlite3
import traceback
from datetime import date
from format import format


def WhoIsMe(user_id, name, sname):
	construction_index = random.randrange(len(introductory_construction))

	try:
		base = sqlite3.connect('CocksBase.bd')
	except:
		print('Failed connect to DataBase of WhoIsMe')

	whoDB = base.cursor()

	whoDB.execute(
		"CREATE TABLE IF NOT EXISTS WhoIsMe(user_id text PRIMARY KEY, DolbaebName text, DolbaebLastName text, date text, Who text)")
	
	whoDB.execute(
		"SELECT user_id FROM WhoIsMe WHERE user_id = '%s'" % (user_id))
	check = whoDB.fetchone()

	if check == None:
		row = (user_id, name, sname, '', '')
		try:
			whoDB.execute("INSERT INTO WhoIsMe VALUES(?, ?, ?, ?, ?)", row)
		except Exception as e:
			print('Ошибка:\n', traceback.format_exc())
			return
		base.commit()

	whoDB.execute("SELECT date FROM WhoIsMe WHERE user_id = '%s'" % (user_id))
	lastCommitDate = whoDB.fetchone()

	if format(lastCommitDate) == str(date.today()):
		try:
			return WhoIsMeSelect(user_id, construction_index)
		except Exception as e:
			print('Ошибка:\n', traceback.format_exc())
			return
	else:
		try:
			who_index = random.randrange(len(who_is_me_list))
			whoDB.execute(
				f"UPDATE WhoIsMe SET date = '{str(date.today())}', Who = '{who_is_me_list[who_index]}' WHERE user_id = {user_id}")
			base.commit()
			return WhoIsMeSelect(user_id, construction_index)
		except Exception as e:
			print('Ошибка:\n', traceback.format_exc())
			return
		

	base.commit()
	base.close()


def WhoIsMeSelect(user_id, construction_index):
	try:
		base = sqlite3.connect('CocksBase.bd')
	except:
		print('Failed connect to DataBase of WhoIsMe')

	whoDB = base.cursor()

	whoDB.execute(
			"SELECT DolbaebName FROM WhoIsMe WHERE user_id='%s'" % (user_id))
	dolbaeb_name = format(whoDB.fetchall())

	whoDB.execute(
		"SELECT DolbaebLastName FROM WhoIsMe WHERE user_id='%s'" % (user_id))
	dolbaeb_last_name = format(whoDB.fetchall())

	whoDB.execute(
		"SELECT Who FROM WhoIsMe WHERE user_id='%s'" % (user_id))
	who = format(whoDB.fetchall())
	
	return f"Сегодня {dolbaeb_name} {dolbaeb_last_name} {introductory_construction[construction_index]} {who}."
