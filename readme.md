```
# for play bgm

$ sudo apt-get install mpg321
```

```
# for News API

$ pip3 install newsapi-python
```

```
# for ring voice read news.

$ sudo apt-get install open-jtalk
$ sudo apt-get install open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001

# apply female voice.
$ wget http://downloads.sourceforge.net/project/mmdagent/MMDAgent_Example/MMDAgent_Example-1.6/MMDAgent_Example-1.6.zip
$ unzip MMDAgent_Example-1.6.zip
$ sudo cp -R ./MMDAgent_Example-1.6/Voice/mei /usr/share/hts-voice/

# please fix below code in jsay.sh.

-m /usr/share/hts-voice/mei/mei_normal.htsvoice \

```

```
# crontab -e

# ring alerm only weekday.
10 8 * * 1,2,3,4,5 python3 /home/pi/alerm-pi/news-pi.py
55 8 * * 1,2,3,4,5 python3 /home/pi/alerm-pi/alerm-pi.py
50 11 * * 1,2,3,4,5 python3 /home/pi/alerm-pi/alerm-pi.py
45 12 * * 1,2,3,4,5 python3 /home/pi/alerm-pi/alerm-pi.py
28 13 * * 1,2,3,4,5 python3 /home/pi/alerm-pi/alerm-pi.py
20 17 * * 1,2,3,4,5 python3 /home/pi/alerm-pi/alerm-pi.sh
```
