import logging
import sys

from telegram import ext
from app.hanlders import HANDLERS


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

updater = ext.Updater(sys.argv[1])

for handler in HANDLERS:
    updater.dispatcher.add_handler(handler)


updater.start_polling()
print('service started ...')
updater.idle()
