
from snake import config, logger, logging
from telegram.ext import Updater, CommandHandler

logger.setLevel(logging.INFO)
updater = Updater(config.bot.token)
dp = updater.dispatcher


def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))


dp.add_handler(CommandHandler('hello', hello))
