import subprocess
import datetime
import traceback
import time
from mutagen.mp3 import MP3 as mp3
import pygame

try:
    loopCount = 3
    # ring alerm.
    pygame.mixer.init()
    pygame.mixer.music.load('./sounds/alerm.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(loopCount)
    time.sleep(8 * loopCount)
except:
    e = traceback.format_exc()
    print(e)
    dt_now = datetime.datetime.now()
    path = './alerm-pi-err.log'
    with open(path, mode='a') as f:
        f.write(dt_now.strftime('- Exception - %Y/%m/%d %H:%M:%S \n'))
        f.write(e + '\n\n')
finally:
    pygame.mixer.music.stop()
