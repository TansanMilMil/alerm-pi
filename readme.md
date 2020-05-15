# install applications
- please install below applications.
```
# install for play se.
$ sudo apt-get install mpg321

# install for play bgm.
$ sudo apt-get install python-pygame

# install for News API
$ pip3 install newsapi-python
```

# GCP settings
1. please create new GCP Cloud project.(cf. https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries?hl=ja)
1. enable "Cloud Text-to-Speech API".
1. create new "Service Account Key" and DL credential json.
  - "GOOGLE_APPLICATION_CREDENTIALS" is used at crontab settings.

# crontab settings
- edit crontab and write settings, any events when triggered.
- don't forget setting "LANG", "SHELL", "PATH" and "GOOGLE_APPLICATION_CREDENTIALS" that must be in credentials directory.
```
$ crontab -e

# apply japanese language script.
LANG=ja_JP.UTP-8
# enable bash.
SHELL=/bin/bash
# set path.
PATH=*******************************
# set environment variables.
GOOGLE_APPLICATION_CREDENTIALS="******************.json"

# ring alerm only weekday.
10 8 * * 1,2,3,4,5 /home/pi/alerm-pi/news-pi.sh
55 8 * * 1,2,3,4,5 /home/pi/alerm-pi/alerm-pi.sh
50 11 * * 1,2,3,4,5 /home/pi/alerm-pi/alerm-pi.sh
45 12 * * 1,2,3,4,5 /home/pi/alerm-pi/alerm-pi.sh
28 13 * * 1,2,3,4,5 /home/pi/alerm-pi/alerm-pi.sh
20 17 * * 1,2,3,4,5 /home/pi/alerm-pi/alerm-pi.sh
```

# allow execution
```
$ chmod 777 /home/pi/alerm-pi/alerm-pi.sh
$ chmod 777 /home/pi/alerm-pi/alerm-pi.py
$ chmod 777 /home/pi/alerm-pi/news-pi.sh
$ chmod 777 /home/pi/alerm-pi/news-pi.py
```

