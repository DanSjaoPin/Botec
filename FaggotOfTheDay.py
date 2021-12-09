import sqlite3
from datetime import date
import traceback
from format import format

from sender import sender
from randomUser import randomUser

def FagsCreate():
    try:
        base = sqlite3.connect('CocksBase.bd')
        print('Connected to DataBase of Faggots')
    except:
        print('Failed connect to DataBase of Faggots')

    cockBD = base.cursor()

    cockBD.execute(
        "CREATE TABLE IF NOT EXISTS faggot(user_id text, DolbaebName text, DolbaebLastName text, chat_id text, date text)")

    cockBD.execute("CREATE TABLE IF NOT EXISTS faggot(user_id text PRIMARY KEY, DolbaebName text, DolbaebLastName text, chat_id text, date text)")

    base.commit()
    base.close()


def WhoIsFaggot(chat_id, degenerat_id):
    base = sqlite3.connect('CocksBase.bd')
    cockBD = base.cursor()

    cockBD.execute("UPDATE cock SET chat_id = %s WHERE user_id = '%s'" % (chat_id, degenerat_id))
    cockBD.execute("SELECT user_id FROM faggot WHERE chat_id = '%s'" % (chat_id))
    check = cockBD.fetchone()

    if check == None:
        row = ("id", "DolbaebName", "DolbaebLastName", chat_id, "date")
        try:
            cockBD.execute("INSERT INTO faggot VALUES(?, ?, ?, ?, ?)", row)
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
            return
        base.commit()

    cockBD.execute("SELECT date FROM faggot WHERE chat_id = '%s'" % (chat_id))
    lastCommitDate = cockBD.fetchone()

    lastCommitDate = format(lastCommitDate)

    if lastCommitDate == str(date.today()):
        cockBD.execute("SELECT user_id FROM faggot WHERE chat_id = '%s'" % (chat_id))
        ID = cockBD.fetchall()

        ID = format(ID)

        cockBD.execute("SELECT DolbaebName FROM faggot WHERE chat_id = '%s'" % (chat_id))
        N = cockBD.fetchall()

        N = format(N)

        cockBD.execute("SELECT DolbaebLastName FROM faggot WHERE chat_id = '%s'" % (chat_id))
        LN = cockBD.fetchall()

        LN = format(LN)

        CT = "Пидор дня: %s %s" % (LN, N)
        sender(chat_id, CT)

    else:
        random_user = randomUser(chat_id)

        ID = random_user[0]
        LN = random_user[1]
        N = random_user[2]

        cockBD.execute("UPDATE faggot SET user_id = '%s', DolbaebName = '%s', DolbaebLastName = '%s', date = '%s' WHERE chat_id = '%s'" % (ID, N, LN, date.today(), chat_id))
        base.commit()
        base.close()

        WhoIsFaggot(chat_id, degenerat_id)

