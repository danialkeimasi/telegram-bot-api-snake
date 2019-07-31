from .page import *
from .logger import logger
import telegram.ext
import yaml
import attrdict


config = attrdict.AttrDict(yaml.safe_load(open("./config.yml", 'r')))
