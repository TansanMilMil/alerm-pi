import subprocess
import datetime
import sys
from newsapi import NewsApiClient

# get headline
newsapi = NewsApiClient(api_key='671c92cd456f4d639703ea2e24671bbf')
top_headline = newsapi.get_top_headlines(country='jp')
if len(top_headline['articles']) > 5:
	top_headline['articles'] = top_headline['articles'][0:5]

# start music
#subprocess.run('mpg321 ./bgm.mp3 &', shell=True)

# read news
dt_now = datetime.datetime.now()
subprocess.run('./jsay.sh ' + str(dt_now.month) + '月' + str(dt_now.day) + '日のニュースをお伝えします。'
		, shell=True)

for news in top_headline['articles']:
	news['title'] = """ ' """ + news['title'] + """ ' """
	print(news['title'])
	subprocess.run('./jsay.sh ' + news['title'], shell=True)

	news['description'] = """ ' """ + news['description'] + """ ' """
	print(news['description'])
	# subprocess.run('./jsay.sh ' + news['description'], shell=True)

	print('---------------')


subprocess.run('./jsay.sh ' + '以上、ニュースをお伝えしました。', shell=True)

sys.exit()
