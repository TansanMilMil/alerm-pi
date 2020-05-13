import subprocess
from newsapi import NewsApiClient

# get headline
newsapi = NewsApiClient(api_key='671c92cd456f4d639703ea2e24671bbf')
top_headline = newsapi.get_top_headlines(country='jp')
if len(top_headline['articles']) > 5:
	top_headline['articles'] = top_headline['articles'][0:5]

# read news
for news in top_headline['articles']:
	print(news['title'])
	print(news['description'])
	print('---------------')

