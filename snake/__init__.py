from .page import *
from .logger import logger, logging
from .decorators import send_action, admin_only

from telegram import ext, ChatAction, KeyboardButton, InlineKeyboardButton

import yaml
import attrdict


config = attrdict.AttrDict(yaml.safe_load(open("./config.yml", 'r')))
updater = ext.Updater(config.bot.token)


from app.hanlders import HANDLERS

for handler in HANDLERS:
    updater.dispatcher.add_handler(handler)
