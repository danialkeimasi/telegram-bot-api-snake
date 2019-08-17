from snake import ChatAction, is_authenticated
from snake.decorators import debug, send_action
from . import pages


@send_action(ChatAction.TYPING)
def hello(bot, update):
    test = is_authenticated(bot, '@danidev', update.message.from_user.id)
    update.message.reply_text(**pages.main_page.text_remove_keyboard)
