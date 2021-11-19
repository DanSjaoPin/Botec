import sqlite3
from config import main_token
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll

vk_session = vk_api.VkApi(token = main_token)
global vk
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 203331529)

def sender(id, text):
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : get_random_id()})

def Reit(IDs, vkid):
    base = sqlite3.connect('CocksBase.bd')
    cockBD = base.cursor()
    print("ids = " + IDs)
    print(type(IDs))
    try:
        #cockBD.execute("SELECT RowNum FROM (SELECT ROW_NUMBER() OVER (ORDER BY Length DESC) RowNum, * FROM cock) WHERE user_id = %s" % (IDs))
        cockBD.execute("SELECT RowNum FROM (SELECT ROW_NUMBER() OVER (ORDER BY Length DESC) RowNum, * FROM cock) WHERE user_id = 182821666")

        #cockBD.execute("SELECT user_id FROM cock WHERE user_id = %s" % (IDs))
    except:
        print("\n--------------------------------------------------------Кракнувса рейтинг-------------------------------------------------------\n")
    r = cockBD.fetchone()
    print(r)
    sender(vkid, "Твое место в абсолютном рейтинге: %s" % (r))
