import os
import sys

from tkinter import Tk
from app.main import updater

updater.start_polling()
updater.idle()


CHECK_INTERVAL = 2000

last_mtime = os.path.getmtime(__file__)

root = Tk()

def restart_if_changed():
    if os.path.getmtime(__file__) > last_mtime:
        print('file has changed => restarting')

        os.execv(sys.executable, ['python'] + sys.argv)

    root.after(CHECK_INTERVAL, restart_if_changed)

root.after(CHECK_INTERVAL, restart_if_changed)
root.mainloop()
