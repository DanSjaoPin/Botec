from sender import sender
from randomUser import randomUser
import random


def fuck(chat_id, degenerat_id, name, sname):
    
    random_user = randomUser(chat_id)

    ID = random_user[0]
    LN = random_user[1]
    N = random_user[2]
    
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

    return CT

