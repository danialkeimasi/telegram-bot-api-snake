from snake import send_action, ChatAction, is_authenticated
from . import pages


@send_action(ChatAction.TYPING)
def hello(bot, update):
    test = is_authenticated(bot, '@danidev', update.message.from_user.id)
    bot.send_message(update.message.from_user.id, 'goh', reply_markup=pages.main_page.markup)
