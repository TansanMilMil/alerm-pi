import subprocess
import datetime
import traceback
import time
from mutagen.mp3 import MP3 as mp3
import pygame

try:
    # ring alerm.
    #subprocess.run('cd /home/pi/alerm-pi', shell=True)
    #subprocess.run('sudo amixer ALSA cset numid=3 1', shell=True)
    #subprocess.run('mpg321 alerm.mp3', shell=True)
    pygame.mixer.init()
    pygame.mixer.music.load('./alerm.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(1)
    time.sleep(10)
except:
    e = traceback.format_exc()
    print(e)
    dt_now = datetime.datetime.now()
    path = './alerm-pi-error-log.txt'
    with open(path, mode='a') as f:
        f.write(dt_now.strftime('- Exception - %Y/%m/%d %H:%M:%S \n'))
        f.write(e + '\n\n')
finally:
    pygame.mixer.music.stop()
