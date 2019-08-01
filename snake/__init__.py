from .page import *
from .logger import logger, logging
from .decorators import *
from telegram import *


import yaml
import attrdict
config = attrdict.AttrDict(yaml.safe_load(open("./config.yml", 'r')))
