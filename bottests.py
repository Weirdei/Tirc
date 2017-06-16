import telepot
from telepot.loop import MessageLoop
from pprint import pprint

API_KEY = '323157985:AAH6_R0PyQemilBWZ4RsV9ttzfvDDqgourA'

MESSAGE_ID_CONTAINER_FILENAME = 'message_id_container'


def read_update_id(filename):
    with open(filename) as f:
        return int(f.read())


def write_update_id(filename, num):
    with open(filename, 'w') as f:
        f.write(num)


bot = telepot.Bot(API_KEY)

# temporary container aka list for storing all received messages

# Receive message later then highest_update_id, return tuple (list_of_messages,highest_update_id)
def message_receiver(update_id):
    msg = bot.getUpdates(offset=update_id)
    update_id_container = []
    for i in msg:
        update_id_container.append(i['update_id'])
    if update_id_container:
        update_id = (max(update_id_container) + 1)
    return msg, update_id


def hand(msg):
    pprint(msg)

MessageLoop(bot, hand).run_as_thread()