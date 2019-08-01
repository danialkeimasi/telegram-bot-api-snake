
from snake import send_action, ChatAction
from . import pages

@send_action(ChatAction.TYPING)
def hello(bot, update):
    bot.send_message(update.message.from_user.id, pages.main_page.text, reply_markup=pages.main_page.markup)
