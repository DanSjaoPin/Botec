from sender import vk
import random

def randomUser(id):
    users = vk.messages.getConversationMembers(peer_id=2000000000 + id)
    user = users['profiles']

    n = random.randrange(0, len(user))

    return [str(user[n]['id']), str(user[n]['last_name']), str(user[n]['first_name'])]
