#!/usr/bin/env python

"""
A tool to maintain the persistence of a xmodmap commands which add Pok3r
style key mappings via Caps Lock as a function key, with xmodmap commands. It works perfectly,
but is reset every time an input device is added or removed. 

This Python script checks every two seconds to see whether key 66 (Caps_Lock) is Caps_Lock 
(It should be modeswitch). If not, it shuts off capslock and runs customkeys.
"""

import subprocess
import time
import re

def customkeys():
    
    cmds = [
        r'xmodmap -e "keycode 66 = Mode_switch"',
        r'xmodmap -e "keycode 31 = i I Up Up"',
        r'xmodmap -e "keycode 44 = j J Left Left"',
        r'xmodmap -e "keycode 45 = k K Down Down"',
        r'xmodmap -e "keycode 46 = l L Right Right"',
        r'xmodmap -e "keycode 30 = u U Prior Prior"',
        r'xmodmap -e "keycode 32 = o O Next Next"',
        r'xmodmap -e "keycode 43 = h H Home Home"',
        r'xmodmap -e "keycode 57 = n N End End"',
        r'xmodmap -e "keycode 65 = space space Menu Menu"',
        r'xmodmap -e "keycode 22 = BackSpace BackSpace Delete Delete"',
    ]
    
    for cmd in cmds:
        subprocess.Popen(cmd, shell=True)
    

def is_capslock_capslock():
    xmodmap_layout = subprocess.check_output('xmodmap -pke', shell=True).decode('utf-8').strip()
    capslock_status = re.findall(r'keycode\s+66.+', xmodmap_layout)[0].split()
    
    if capslock_status[3] == 'Caps_Lock':
        return True
    
    else: 
        return False


def is_capslock_on():
    """
    Check whether CapsLock is toggled on
    """
    check = (
        subprocess.check_output('/usr/bin/xset q', shell = True)
            .decode('utf-8')
            .strip()
            .find('Caps Lock:   on')
    )
    
    ret = check != -1
    
    return ret


def capslock_off():
    # check for whether capslock is on
    if is_capslock_on() == True:
        # turn off capslock if it is on
        subprocess.Popen('/usr/bin/xdotool key Caps_Lock', shell=True)
    
    

if __name__ == "__main__":
    
    # run for the first time with 10 second delay
    capslock_off()
    customkeys()
    
    while True:
        time.sleep(2)
        if is_capslock_capslock() == True:
            capslock_off()
            customkeys()

