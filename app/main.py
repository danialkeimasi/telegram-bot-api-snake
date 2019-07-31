from snake import config, logger, telegram

updater = telegram.ext.Updater(config.bot.token)


def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))

updater.dispatcher.add_handler(telegram.ext.CommandHandler('hello', hello))
