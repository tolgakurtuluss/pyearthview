import os
from random import randint
import urllib.request
import requests
import platform
import ctypes

def set_wallpaper_windows(filename):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filename , 0)

def set_wallpaper_mac(filename):
    import subprocess
    SCRIPT = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "{}"
    end tell
    END"""
    subprocess.Popen(SCRIPT.format(filename), shell=True)

def set_wallpaper_linux(filename):
    import subprocess
    subprocess.call(["feh", "--bg-fill", filename])

def set_wallpaper(filename):
    system = platform.system()
    if system == "Windows":
        set_wallpaper_windows(filename)
    elif system == "Darwin":
        set_wallpaper_mac(filename)
    else:
        set_wallpaper_linux(filename)

def randomize(min_value=1000, max_value=2000):
    status = True
    while status:
        value = randint(min_value, max_value)
        link = f"https://earthview.withgoogle.com/download/{value}.jpg"
        r = requests.get(link)
        if r.status_code == 200:
            print(r.status_code)
            print(link)
            filename = os.path.join(os.getcwd(), 'wallpaper.jpg')
            print(filename)
            urllib.request.urlretrieve(link, filename)
            set_wallpaper(filename)
            status = False

if __name__ == '__main__':
    randomize()
