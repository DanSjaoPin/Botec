from sender import sender


def say(msg):
	if msg[2] == 'а':
		msgg = 'Хуя' + msg[3:]
	elif msg[2] == 'о':
		msgg = 'Хуё' + msg[3:]
	else:
		msgg = 'Ху' + msg[2:]
	return msgg
