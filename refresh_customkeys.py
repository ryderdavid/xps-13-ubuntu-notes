# %%
#!/usr/bin/env python

"""
A tool to maintain the persistence of a simple shell script 'customkeys' which adds Pok3r
style key mappings via Caps Lock as a function key, with xmodmap commands. It works perfectly,
but is reset every time an input device is added or removed. 

This Python script checks every two seconds to see whether key 66 (Caps_Lock) is Caps_Lock 
(It should be modeswitch). If not, it shuts off capslock and runs customkeys.
"""

import subprocess
import time
import re


def refresh():
    # check for whether capslock is on
    xset_outputs = subprocess.check_output(["/usr/bin/xset", "q"]).decode('utf-8').strip()
    if xset_outputs.find('Caps Lock:   on') != -1:
    # turn off capslock if it is on
        subprocess.Popen(['/usr/bin/xdotool', 'key', 'Caps_Lock'])
    
    # run customkeys
    subprocess.Popen("customkeys")
    
    
def is_capslock_capslock():
    xmodmap_layout = subprocess.check_output(["xmodmap", "-pke"]).decode('utf-8').strip()
    capslock_status = re.findall(r"keycode\s+66.+", xmodmap_layout)[0].split()
    
    if capslock_status[3] == 'Caps_Lock':
        return True
    
    else: 
        return False
    

# %%
if __name__ == "__main__":
    while True:
        time.sleep(2)
        if is_capslock_capslock() == True:
            refresh()
