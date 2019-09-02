import logging

from telegram import ext
from app.hanlders import HANDLERS


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

updater = ext.Updater("869742149:AAFceL3S-AlQQwR7FhrD5rfe2oN8NsX-o34")

for handler in HANDLERS:
    updater.dispatcher.add_handler(handler)


updater.start_polling()
print('service started ...')
updater.idle()
