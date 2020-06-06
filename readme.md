# install applications
- please install below applications.
```
# install for play se.
$ sudo apt-get install mpg321=0.3.2

# install for play bgm.
$ sudo apt-get install python-pygame=1.9.3

# install for News API
$ pip3 install newsapi-python==0.2.6

# install for treat mp3
$ pip3 install mutagen==1.44.0

# install for GCP Text-to-Speech API
$ pip3 install google-cloud-texttospeech==1.0.1
```

# GCP settings
1. create new GCP Cloud project.(cf. https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries?hl=ja)
1. enable "Cloud Text-to-Speech API".
1. create new "Service Account Key" and DL credential json.
  - "GOOGLE_APPLICATION_CREDENTIALS" is used at crontab settings. please save this carefully.
  
# NewsAPI settings
1. create NewsAPIkey for your project.(cf. https://newsapi.org/)
  - "API Key" is used at get news json data. please save this carefully.

# create credential files
1. create `credentials` directory at any path.
1. create `gcp-service-account.json` and `newsapi.ini` in credentials directory.
1. write below code to `gcp-service-account.json`.
```
{
	  "type": "service_account",
	  "project_id": "**************************************",
	  "private_key_id": "**************************************",
	  "private_key": "**************************************",
	  "client_email": "**************************************",
	  "client_id": "**************************************",
	  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
	  "token_uri": "https://oauth2.googleapis.com/token",
	  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
	  "client_x509_cert_url": "**************************************"
}
```
4. write below code to `newsapi.ini`. "ApiKey" is NewsAPI Key.
```
[DEFAULT]
ApiKey = ***********************************
```
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

