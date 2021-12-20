from sender import sender

def say(id, msg):
    if msg[2] == 'а':
        msgg = 'хуя' + msg[3:]
    elif msg[2] == 'о':
        msgg = 'хуё' + msg[3:]
    else:
        msgg = 'хуи' + msg[3:]
    sender(id, msgg)
