
# you can read this docs for writing bot
# handler refrence : https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html


from snake import ext
from . import views


HANDLERS = [
    ext.MessageHandler(ext.Filters.text, views.hello)
]
