import os
import sys

from watchgod import run_process
from app.main import updater

updater.start_polling()
updater.idle()


def run():
    print('restarting')
    os.execv(sys.executable, ['python3.6'] + sys.argv)


run_process('./', run)
run_process('./snake/', run)
run_process('./app/', run)

