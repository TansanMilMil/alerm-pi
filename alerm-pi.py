import subprocess

# ring alerm.
subprocess.run('cd /home/pi/alerm-pi', shell=True)
subprocess.run('sudo amixer cset numid=3 80%', shell=True)
subprocess.run('mpg321 alerm.mp3', shell=True)

