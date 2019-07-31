from telegram.ext import Updater, CommandHandler
import yaml
import attrdict


config = attrdict.AttrDict(yaml.safe_load(open("./config.yml", 'r')))
updater = Updater(config.bot.token)


def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))

updater.dispatcher.add_handler(CommandHandler('hello', hello))
