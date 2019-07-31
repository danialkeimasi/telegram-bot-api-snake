
from snake import config, logger, logging
from telegram.ext import Updater, CommandHandler

logger.setLevel(logging.INFO)
updater = Updater(config.bot.token)
dp = updater.dispatcher


dp.add_handler(CommandHandler('hello', hello))
def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))

