import subprocess
import datetime
import sys
from newsapi import NewsApiClient
import traceback
from mutagen.mp3 import MP3 as mp3
import pygame
import time
import random
from my_module import gcpspeech
import configparser

try:
    # load config
    newsapi = configparser.ConfigParser()
    newsapi.read('./credentials/newsapi.ini', encoding='utf-8')

    # get headline
    newsapi = NewsApiClient(api_key=newsapi['DEFAULT']['ApiKey'])
    top_headline = newsapi.get_top_headlines(country='jp')
    
    if len(top_headline['articles']) > 5:
        random.shuffle(top_headline['articles'])
        top_headline['articles'] = top_headline['articles'][0:5]
    
    # start music
    pygame.mixer.init()
    pygame.mixer.music.load('./bgm.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(0)

    # read news
    dt_now = datetime.datetime.now()
    gcpspeech.start(str(dt_now.month) + '月' + str(dt_now.day) + '日のニュースをお伝えします。')

    for news in top_headline['articles']:
        print(news['title'])
        gcpspeech.start(str(news['title'])) 

        print(news['description'])
        gcpspeech.start(str(news['description']))

        print('\n')   
    
    gcpspeech.start('以上、ニュースをお伝えしました。')
except:
    e = traceback.format_exc()
    print(e)
    dt_now = datetime.datetime.now()
    path = './news-pi-err.log'
    with open(path, mode='a') as f:
        f.write(dt_now.strftime('- Exception - %Y/%m/%d %H:%M:%S \n'))
        f.write(e + '\n\n')
finally:
    pygame.mixer.music.fadeout(5000)
    time.sleep(5)
