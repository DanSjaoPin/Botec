import os, random
import vk_api
from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from sender import vk, VkBotEventType, vk_session


class Pic:
	
	def RandomPic(self, path):
		self.__file_name = random.choice(os.listdir(path))
		return path + self.__file_name

	def FilePath(self, type):
		pic_type = ['Anima', 'Atmospheric', 'Pepe', 'Girls', 'Boys', 'b']
		path = "PicsForSend/" + pic_type[type] + '/'
		absolut_path = self.RandomPic(path)
		self.file_path = os.path.abspath(absolut_path)


def SendRandomPic(id, type):
	pictuare = Pic()

	pictuare.FilePath(type)

	attachments = []	

	upload = vk_api.VkUpload(vk)
	upload_image = upload.photo_messages(photos=pictuare.file_path)[0]

	attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
	vk_session.method('messages.send', {
	                  'chat_id': id, 'random_id': get_random_id(), 'attachment': ','.join(attachments)})


def ChoosePicType(id, msg):
	if 'анима' in msg or 'анимe' in msg:
		SendRandomPic(id, 0)
	elif 'атмосферно' in msg:
		SendRandomPic(id, 1)
	elif 'пепе' in msg:
		SendRandomPic(id, 2)
	elif 'девушки' in msg or 'тяночки' in msg:
		SendRandomPic(id, 3)
	elif 'мальчики' in msg:
		SendRandomPic(id, 4)
	else:
		SendRandomPic(id, 5)
	return
