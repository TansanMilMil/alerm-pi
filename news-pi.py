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

news_topics_sound = './sounds/decide11.mp3'

def get_day_of_week_jp(dt):
    w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return(w_list[dt.weekday()])

try:
    # load config
    newsapi = configparser.ConfigParser()
    newsapi.read('./credentials/newsapi.ini', encoding='utf-8')

    # get headline
    newsapi = NewsApiClient(api_key=newsapi['DEFAULT']['ApiKey'])
    top_headline = None
    if len(sys.argv) >= 3:
        top_headline = newsapi.get_top_headlines(country='jp', category=sys.argv[2])
    else:
        top_headline = newsapi.get_top_headlines(country='jp')
    if len(top_headline['articles']) > 5:
        random.shuffle(top_headline['articles'])
        top_headline['articles'] = top_headline['articles'][0:5]
    
    # start music
    pygame.mixer.init()
    bgm = sys.argv[1] if len(sys.argv) >= 2 else None
    if bgm == '1':
        pygame.mixer.music.load('./sounds/bgm1.mp3')
        pygame.mixer.music.set_volume(0.1)
    elif bgm == '2':
        pygame.mixer.music.load('./sounds/bgm2.mp3')
        pygame.mixer.music.set_volume(0.07)
    elif bgm == '3':
        pygame.mixer.music.load('./sounds/bgm3.mp3')
        pygame.mixer.music.set_volume(0.07)
    else:
        pygame.mixer.music.load('./sounds/bgm1.mp3')
        pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    time.sleep(3)

    # read news
    dt_now = datetime.datetime.now()
    gcpspeech.start(f'{str(dt_now.month)}月{str(dt_now.day)}日{get_day_of_week_jp(dt_now)}のニュースをお伝えします。')

    for news in top_headline['articles']:
        subprocess.run('mpg321 ' + news_topics_sound, shell=True)
        time.sleep(0.5)
        print(news['title'])
        gcpspeech.start(str(news['title'])) 

        print(news['description'])
        gcpspeech.start(str(news['description']))

        print('\n')  
        time.sleep(0.5) 
    
    if dt_now.weekday() == 1:
        gcpspeech.start(f'{get_day_of_week_jp(dt_now)}は燃えるゴミの日です。面倒くさがらずに出しましょう。')
    if dt_now.weekday() == 3:
        gcpspeech.start(f'{get_day_of_week_jp(dt_now)}は資源ゴミの日です。忘れないようにしましょう。')      
    if dt_now.weekday() == 4:
        gcpspeech.start(f'{get_day_of_week_jp(dt_now)}は燃えるゴミの日です。花金ですししっかり出しましょう。')          
    time.sleep(0.5)
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
