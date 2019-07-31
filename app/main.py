
# you can read this docs for writing bot
# handler refrence : https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html

from pprint import pprint
from snake import config, logger, logging
from telegram import ext


logger.setLevel(logging.INFO)
updater = ext.Updater(config.bot.token)
dp = updater.dispatcher


def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))

    pprint(bot)
    pprint(update)


dp.add_handler(ext.MessageHandler(ext.Filters.text, hello))
