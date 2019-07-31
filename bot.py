import os
import sys

from watchgod import run_process
from app.main import updater

updater.start_polling()
updater.idle()


def run():
    print('restarting')
    os.execv(sys.executable, ['python'] + sys.argv)

run_process('./', run)
