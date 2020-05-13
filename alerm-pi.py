import subprocess

# ring alerm.
subprocess.run('cd /home/pi/alerm-pi', shell=True)
subprocess.run('sudo amixer ALSA cset numid=3 1', shell=True)
subprocess.run('mpg321 alerm.mp3', shell=True)

