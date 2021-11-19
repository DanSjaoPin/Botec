import sqlite3
from sender import sender
from format import format


def fuck(chat_id, degenerat_id, name, sname):
    base = sqlite3.connect('CocksBase.bd')
    
    cockBD = base.cursor()
    cockBD.execute("UPDATE cock SET chat_id = %s WHERE user_id = '%s'" % (chat_id, degenerat_id))
    cockBD.execute("SELECT user_id FROM faggot WHERE chat_id = '%s'" % (chat_id))

    cockBD.execute("SELECT user_id FROM cock WHERE chat_id = '%s' ORDER BY RANDOM() LIMIT 1" % (chat_id))
    ID = cockBD.fetchall()
    ID = format(ID)

    cockBD.execute("SELECT DolbaebName FROM cock WHERE user_id = '%s'" % (ID))
    N = cockBD.fetchall()
    N = format(N)

    cockBD.execute("SELECT DolbaebLastName FROM cock WHERE user_id = '%s'" % (ID))
    LN = cockBD.fetchall()
    LN = format(LN)

    base.close()

    CT = "%s %s трахнул *id%s(%s %s)" % (name, sname, ID, LN, N)

    if str(ID) == str(degenerat_id):
        CT = "%s %s никого не выебал, просто подрочил" % (name, sname)

    elif str(ID) == '182821666':
        CT = "%s %s попытался выебать Даню и получил пизды. Никто не может ебать Даню!" % (name, sname)

    elif str(ID) == '182821666' and str(degenerat_id) == '162958234':
        CT = "Даня прописал смачныый фистинг Славе Кахановскому"

    elif str(ID) == '162958234' and str(degenerat_id) == '182821666':
        CT = "Даня дал на клык Кахановскому"

    elif str(ID) == '162958234':
        CT = "%s %s попытался выебать Славика, но в итоге схватил от него за щеку" % (name, sname)

    sender(chat_id, CT)

