from telegram import ext
from app.hanlders import HANDLERS

import yaml
import attrdict
config = attrdict.AttrDict(yaml.safe_load(open("./config.yml", 'r')))


updater = ext.Updater(config.bot.token)

for handler in HANDLERS:
    updater.dispatcher.add_handler(handler)
