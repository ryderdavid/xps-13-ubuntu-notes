# %%
#!/usr/bin/env python

"""
A tool to maintain the persistence of a simple shell script 'customkeys' which adds Pok3r
style key mappings via Caps Lock as a function key, with xmodmap commands. It works perfectly,
but is reset every time an input device is added or removed. 

This Python script monitors the input devices folder at /dev/input and anytime a file is added 
or removed (device added or removed), it executes customkeys (after turning off Caps Lock if it is on).
"""

import subprocess
import time

folder = "/dev/input"
command_to_run = "command_to_run"

def get_drlist(folder):
    return subprocess.check_output(["ls", folder]).decode('utf-8').strip().split("\n")

deviceslist = get_drlist(folder=folder)

while True:
    drlist1 = get_drlist(folder)
    time.sleep(5)
    drlist2 = get_drlist(folder)
    
    if len(drlist1) != len(drlist2):
        
        # check for whether capslock is on
        xset_outputs = subprocess.check_output(["/usr/bin/xset", "q"]).decode('utf-8').strip()
        if xset_outputs.find('Caps Lock:   on') != -1:
        # turn off capslock if it is on
            subprocess.Popen(['/usr/bin/xdotool', 'key', 'Caps_Lock'])
        
        # run customkeys
        subprocess.Popen("customkeys")
