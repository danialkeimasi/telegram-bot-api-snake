from snake import send_action, ChatAction, is_authenticated
from snake.decorators import debug
from . import pages

@debug
@send_action(ChatAction.TYPING)
def hello(bot, update):
    test = is_authenticated(bot, '@danidev', update.message.from_user.id)
    bot.send_message(update.message.from_user.id, **pages.main_page.send_message)
