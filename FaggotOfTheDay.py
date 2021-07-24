import sqlite3
from datetime import date

import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import main_token

def sender(id, text):
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : get_random_id()})

vk_session = vk_api.VkApi(token = main_token)
global vk
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 203331529)

def FagsCreate():
    try:
        base = sqlite3.connect('CocksBase.bd')
        print('Connected to DataBase of Faggots')
    except:
        print('Failed connect to DataBase of Faggots')

    cockBD = base.cursor();

    cockBD.execute("CREATE TABLE IF NOT EXISTS faggot(user_id text PRIMARY KEY, DolbaebName text, DolbaebLastName text, chat_id text, date text)")

    base.commit()
    base.close()


def WhoIsFaggot(chat_id, degenerat_id):
    base = sqlite3.connect('CocksBase.bd')
    cockBD = base.cursor();
    cockBD.execute("UPDATE cock SET chat_id = %s WHERE user_id = '%s'" % (chat_id, degenerat_id))
    cockBD.execute("SELECT user_id FROM faggot WHERE chat_id = '%s'" % (chat_id))
    check = cockBD.fetchone()
    if check == None:
        row = ("id", "DolbaebName", "DolbaebLastName", chat_id, "date")
        cockBD.execute("INSERT INTO faggot VALUES(?, ?, ?, ?, ?)", row)
        base.commit()

    cockBD.execute("SELECT date FROM faggot WHERE chat_id = '%s'" % (chat_id))
    lastCommitDate = cockBD.fetchone()
    for simbol in str(lastCommitDate):
        if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'":
            newd = str(lastCommitDate).replace(simbol, '')
            lastCommitDate = str(newd)

    if lastCommitDate == str(date.today()):
        cockBD.execute("SELECT user_id FROM faggot WHERE chat_id = '%s'" % (chat_id))
        ID = cockBD.fetchall()

        for simbol in str(ID):
            if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'" or simbol == "["  or simbol == "]":
                newd = str(ID).replace(simbol, '')
                ID = str(newd)

        cockBD.execute("SELECT DolbaebName FROM faggot WHERE chat_id = '%s'" % (chat_id))
        N = cockBD.fetchall()
        for simbol in str(N):
            if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'" or simbol == "["  or simbol == "]":
                newd = str(N).replace(simbol, '')
                N = str(newd)

        cockBD.execute("SELECT DolbaebLastName FROM faggot WHERE chat_id = '%s'" % (chat_id))
        LN = cockBD.fetchall()
        for simbol in str(LN):
            if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'" or simbol == "["  or simbol == "]":
                newd = str(LN).replace(simbol, '')
                LN = str(newd)

        CT = "Пидор дня: *id%s(%s %s)" % (ID, LN, N)
        sender(chat_id, CT)

    else:
        cockBD.execute("SELECT user_id FROM cock WHERE chat_id = '%s' ORDER BY RANDOM() LIMIT 1" % (chat_id));
        ID = cockBD.fetchall()
        for simbol in str(ID):
            if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'" or simbol == "["  or simbol == "]":
                newd = str(ID).replace(simbol, '')
                ID = str(newd)
        print(ID)
        cockBD.execute("SELECT DolbaebName FROM cock WHERE user_id = '%s'" % (ID))
        N = cockBD.fetchall()
        for simbol in str(N):
            if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'" or simbol == "["  or simbol == "]":
                newd = str(N).replace(simbol, '')
                N = str(newd)
        cockBD.execute("SELECT DolbaebLastName FROM cock WHERE user_id = '%s'" % (ID))
        LN = cockBD.fetchall()
        for simbol in str(LN):
            if simbol == '(' or simbol == ',' or simbol == ')' or simbol == "'" or simbol == "["  or simbol == "]":
                newd = str(LN).replace(simbol, '')
                LN = str(newd)

        cockBD.execute("UPDATE faggot SET user_id = '%s', DolbaebName = '%s', DolbaebLastName = '%s', date = '%s' WHERE chat_id = '%s'" % (ID, N, LN, date.today(), chat_id))
        base.commit()
        base.close()
        WhoIsFaggot(chat_id, degenerat_id)

