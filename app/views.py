
# you can read this docs for writing bot
# handler refrence : https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html

from snake import send_action, ChatAction
from .pages import main_page

@send_action(ChatAction.TYPING)
def hello(bot, update):
    bot.send_message(update.message.from_user.id, main_page.text, reply_markup=main_page.markup)
