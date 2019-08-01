
# you can read this docs for writing bot
# handler refrence : https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html

from pprint import pprint
from snake import config, logger, logging
from telegram import ext

from snake import send_action
from telegram import ChatAction

logger.setLevel(logging.INFO)
updater = ext.Updater(config.bot.token)
dp = updater.dispatcher

@send_action(ChatAction.TYPING)
def hello(bot, update):
    print(update)

    bot.send_message(update.message.from_user.id, 'you are such a guy: {}'.format(update.message.text))


dp.add_handler(ext.MessageHandler(ext.Filters.text, hello))
