import os
import sys

from app.main import updater

updater.start_polling()
updater.idle()


import os
import sys
from tkinter import Tk
 
CHECK_INTERVAL = 2000
 
last_mtime = os.path.getmtime(__file__)

root = Tk()
 
def restart_if_changed():
    if os.path.getmtime(__file__) > last_mtime:
        print('file has changed => restarting')
 
        os.execv(sys.executable, ['python'] + sys.argv)
 
    # Reschedule the checking.
    root.after(CHECK_INTERVAL, restart_if_changed)
 
# Schedule the checking.
root.after(CHECK_INTERVAL, restart_if_changed)
 
# Enter the main processing loop.
root.mainloop()
