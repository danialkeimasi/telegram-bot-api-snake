
# you can read this docs for writing bot
# handler refrence : https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html

from snake import config, logger, logging
from telegram import ext

logger.setLevel(logging.INFO)
updater = ext.Updater(config.bot.token)
dp = updater.dispatcher


def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))


dp.add_handler(ext.CommandHandler('hello', hello))
