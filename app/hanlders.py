from . import views
from telegram import ext


HANDLERS = [
    ext.MessageHandler(ext.Filters.text, views.hello)
]
