
# you can read this docs for writing bot
# handler refrence : https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html

from snake import send_action, ChatAction

@send_action(ChatAction.TYPING)
def hello(bot, update):
    print(update)
    bot.send_message(update.message.from_user.id, 'you are such a guy: {}'.format(update.message.text))
