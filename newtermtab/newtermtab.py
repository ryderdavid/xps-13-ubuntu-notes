#%%
import subprocess
import os
import time
from pynput.keyboard import Key, Controller

# subprocess.Popen(['source', 'venv/bin/activate'])

windows = subprocess.check_output(["wmctrl", "-l"]).decode('utf-8').strip()

user = subprocess.check_output(['whoami']).decode('utf_8').strip()
hostname = subprocess.check_output(['hostname']).decode('utf_8').strip()
userstring = user + '@' + hostname + ':'
userstring

i = windows.find(userstring)

keyboard = Controller()

home = '/home/' + user
if i == -1:
    os.chdir(home)
    subprocess.Popen(['gnome-terminal'])
    
else:
    winid = windows[i-27:i-17]
    subprocess.Popen(['wmctrl', '-ia', winid])
    time.sleep(0.15)

    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.shift)
    keyboard.press('t')
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.shift)
    keyboard.release('t') 


# %%
