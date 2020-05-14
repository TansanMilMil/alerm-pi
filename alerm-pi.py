import subprocess
import datetime
import traceback

try:
    # ring alerm.
    subprocess.run('cd /home/pi/alerm-pi', shell=True)
    subprocess.run('sudo amixer ALSA cset numid=3 1', shell=True)
    subprocess.run('mpg321 alerm.mp3', shell=True)
except:
    e = traceback.format_exc()
    print(e)
    dt_now = datetime.datetime.now()
    path = './alerm-pi-error-log.txt'
    with open(path, mode='a') as f:
        f.write(dt_now.strftime('- Exception - %Y/%m/%d %H:%M:%S \n'))
        f.write(e + '\n\n')

