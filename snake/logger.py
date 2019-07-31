import logging
import colorlog


stream_handler = colorlog.StreamHandler()
stream_handler.setFormatter(colorlog.ColoredFormatter())

logging.basicConfig(
    datefmt='%y-%b-%d %H:%M:%S',
    format='%(levelname)8s:[%(asctime)s][%(filename)20s:%(lineno)4s -%(funcName)20s() ]: %(message)s',

    handlers=[
        stream_handler,
    ]
)

logger = logging.getLogger('bot')
