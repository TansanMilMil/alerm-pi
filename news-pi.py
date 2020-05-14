import subprocess
import datetime
import sys
from newsapi import NewsApiClient
import traceback
from mutagen.mp3 import MP3 as mp3
import pygame
import time

try:
    # get headline
    newsapi = NewsApiClient(api_key='671c92cd456f4d639703ea2e24671bbf')
    top_headline = newsapi.get_top_headlines(country='jp')
    
    if len(top_headline['articles']) > 5:
        top_headline['articles'] = top_headline['articles'][0:5]
    
    # start music
    #subprocess.run('sudo amixer ALSA cset numid=3 1', shell=True)
    #subprocess.run('mpg321 ./bgm.mp3 &', shell=True)
    pygame.mixer.init()
    pygame.mixer.music.load('./bgm.mp3')
    pygame.mixer.music.play(1)

    # read news
    dt_now = datetime.datetime.now()
    subprocess.run('./jsay.sh ' + str(dt_now.month) + '月' + str(dt_now.day) + '日のニュースをお伝えします。', shell=True)
    
    for news in top_headline['articles']:
        news['title'] = """ ' """ + news['title'] + """ ' """
        print(news['title'])
        subprocess.run('./jsay.sh ' + news['title'], shell=True)
            
        news['description'] = """ ' """ + news['description'] + """ ' """
        print(news['description'])
        # subprocess.run('./jsay.sh ' + news['description'], shell=True)
        
        print('---------------')   
    
    subprocess.run('./jsay.sh ' + '以上、ニュースをお伝えしました。', shell=True)
except:
    e = traceback.format_exc()
    print(e)
    dt_now = datetime.datetime.now()
    path = './news-pi-error-log.txt'
    with open(path, mode='a') as f:
        f.write(dt_now.strftime('- Exception - %Y/%m/%d %H:%M:%S \n'))
        f.write(e + '\n\n')
finally:
    pygame.mixer.music.stop()
