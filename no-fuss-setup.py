import os
import sys
import subprocess

try:
    MAX_LEN = os.get_terminal_size().columns
except:
    MAX_LEN = 120

def inbetter(msg, option=None):
    msg = msg.split(' ')
    line = []
    lines = []
    length = 0
    item = iter(msg)
    while True:
        try:
            i = next(item)
            if length + len(i) >= MAX_LEN:
                length = 0
                lines.append(' '.join(line)+'\n')
                line = []
            length += len(i)+1
            line.append(i)
        except StopIteration:
            lines.append(' '.join(line)+'\n')
            break
    msg = ''.join(lines)
    if option == 'print':
        print(msg)
    else:
        chk = input(msg)
        return chk
    

inbetter("  You have chosen the automatic installer. To ensure we install the packages to the correct location, please be so kind as to answer the following:\n", 'print')
chk = inbetter("  When installing packages via pip (aka `pip install ...`), do you normally use `--user`? In other words, should we use it for numpy and pygame? [y/N/quit]\n")

if chk.lower() == 'y':
    user = '--user'
elif chk.lower() == 'n':
    user = ''
else:
    sys.exit()


try:
    import numpy
    print("\nNumpy found.")

except ImportError:
    print("\nNumpy not found. Fetching numpy...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy', user])
    except:
        print("\nI encountered issues that I am not yet prepared to deal with. Exiting...")
except ModuleNotFoundError:
    print("\nNumpy not found. Fetching numpy...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy', user])
    except:
        print("\nI encountered issues that I am not yet prepared to deal with. Exiting...")
try:
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame
    print("\nPygame found.")
except ImportError:
    print("\nPygame not found. Fetching pygame...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygame', user])
except ModuleNotFoundError:
    print("\nPygame not found. Fetching pygame...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygame', user])


chk = inbetter("\nStart `gameoflife.py` now? [y/N]\n")
if chk.lower() == 'y':
    import gameoflife
else:
    sys.exit()