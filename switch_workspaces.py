import subprocess
import sys

if __name__ == "__main__":
    
    curr_d_string = (
        subprocess.check_output('xdotool get_desktop', shell=True)        
            .decode('utf-8')
            .strip()
    )
    
    curr_d = int(curr_d_string)

    up = curr_d - 1
    dn = curr_d + 1

    if sys.argv[1] == "Up":
        subprocess.Popen(f'wmctrl -s {up}', shell=True)
    elif sys.argv[1] == "Down":
        subprocess.Popen(f'wmctrl -s {dn}', shell=True)

