```
# for play bgm

$ sudo apt-get install mpg321
```



```
# for News API

$ pip3 install newsapi-python
```



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


