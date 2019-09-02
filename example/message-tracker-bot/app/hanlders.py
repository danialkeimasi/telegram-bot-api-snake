# you can read this docs for writing bot
# handler reference : https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html

from telegram import ext
from . import views

HANDLERS = [
    ext.CommandHandler('start', views.start),
    ext.CommandHandler('getme', views.getme),
    ext.CommandHandler('clear', views.clear),

    ext.MessageHandler(ext.Filters.text, views.message)
]
