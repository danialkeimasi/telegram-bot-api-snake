import os
import sys

from watchgod import run_process
from snake.telebot import updater
from snake import logger, logging

logger.setLevel(logging.DEBUG)

updater.start_polling()
updater.idle()


# def run():
#     print('restarting')
#     os.execv(sys.executable, ['python3.6'] + sys.argv)


# run_process('./', run)
# run_process('./snake/', run)
# run_process('./app/', run)
