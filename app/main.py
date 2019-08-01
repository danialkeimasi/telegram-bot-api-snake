
# you can read this docs for writing bot
# handler refrence : https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html

from pprint import pprint
from snake import config, logger, logging
from telegram import ext


logger.setLevel(logging.INFO)
updater = ext.Updater(config.bot.token)
dp = updater.dispatcher


def hello(bot, update):
    print(update)

    bot.send_message(update.message.from_user.id, 'you are such a bith: {}'.format(update.message.text))


dp.add_handler(ext.MessageHandler(ext.Filters.text, hello))
