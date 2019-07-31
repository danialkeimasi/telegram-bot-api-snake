from .page import *
from .logger import logger, logging

import yaml
import attrdict


config = attrdict.AttrDict(yaml.safe_load(open("./config.yml", 'r')))
