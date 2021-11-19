import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import main_token

vk_session = vk_api.VkApi(token = main_token)
global vk
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 203331529)

def sender(id, text):
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : get_random_id()})