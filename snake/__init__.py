from .page import *
from .logger import logger, logging
from .decorators import send_action, admin_only

import yaml
import attrdict


config = attrdict.AttrDict(yaml.safe_load(open("./config.yml", 'r')))
