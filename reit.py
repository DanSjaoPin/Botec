import sqlite3
from sender import sender
from format import format

def Reit(IDs, vkid):
    try:
    	base = sqlite3.connect('CocksBase.bd')
    except:
	    print('Failed connect to DataBase')
    cockBD = base.cursor()
    try:
        i=1
        users = cockBD.execute("SELECT user_id FROM cock ORDER BY length DESC")
        for user in users:
            if format(user) == str(IDs):
                sender(vkid, "Твое место в абсолютном рейтинге: %s" % (i))
                return
            else:
                i = i + 1

    except:
        print("\n--------------------------------------------------------Кракнувса рейтинг-------------------------------------------------------\n")
