#!/usr/bin/python3 
# -*- coding: utf-8 -*-
##################################################
## Twitter Bot 
##################################################
## Apache 2.0
##################################################
## Author: #JMousqueton (Julien Mousqueton)
## Copyright: Copyright 2021, Cyber-News-Bot 
## Credits: Original idea 0z09e
## License: Apache 2.0 
## Version: 1.0.1
## Maintainer: #JMousqueton (Julien Mousqueton)
## Email: julien_at_mousqueton.io 
##################################################
# Generic/Built-in 
from datetime import datetime, timezone
import time
# Other Libs
from configparser import ConfigParser
import tweepy

config = ConfigParser(interpolation=None)
config.read('config.cfg')
debug = config.get('Bot','DEBUG')
lang = config.get('Bot','lang')
API_key = config.get('Twitter', 'API_Key')
API_key_secret = config.get('Twitter', 'API_Key_secret')
access_token = config.get('Twitter', 'Access_token')
access_token_secret = config.get('Twitter', 'Access_token_secret')
Bearer_token = config.get('Twitter', 'Bearer_token', raw=True)
hashtags = config.get('Bot', 'Hashtags')
hashtags = hashtags.split(',')
LastRun = config.get('Bot','LastRun')
now = datetime.utcnow().isoformat(timespec='seconds')+'Z'

#### Logger for debug 
def logger(s):
    if str(debug) == 'True':
        print(s)

#### Main 
logger('Debug		: '+ debug)
logger('Date 		: '+ now)

if LastRun == '': 
	logger("[+]First Run ... wait 30 seconds")
	LastRun = now 
	time.sleep(30)
	
logger('Last Run	: '+LastRun)
config.set('Bot', 'LastRun', str(now)) 
with open("config.cfg", 'w') as f:
	config.write(f)
logger('---')
client = tweepy.Client(bearer_token=Bearer_token.replace("'", ""), consumer_key=API_key.replace("'", ""), consumer_secret=API_key_secret.replace("'", ""), access_token=access_token.replace("'", ""), access_token_secret=access_token_secret.replace("'", ""),wait_on_rate_limit=True)
for hash in hashtags:
	query = '#' + hash.replace("'", "").replace(' ', '') + ' -#Roblox -#imessage -#twitterdown -#CheatSheet -#100DaysOfCode -#Web3 -#Geek -is:retweet -is:reply lang:' + lang.replace("'", "").replace(' ', '')
	logger('Query : ' +  query)
	tweets=client.search_recent_tweets(query=query,start_time=LastRun, tweet_fields=['context_annotations', 'created_at'], max_results=50)
	if not tweets.data: 
		logger('[-]No new tweet for #'+hash.replace("'", "").replace(' ', ''))
	else:
		try: 
			for tweet in tweets.data:
				if "RT @" not in tweet.text:
					logger('[+] #' + hash.replace("'", "").replace(' ', '') + ' ' + str(tweet.id) + ' ' + str(tweet.created_at))
					client.retweet(str(tweet.id))
				else:
					logger('[!] tweet '+ str(tweet.id) + ' is a RT')
		except:
				logger ('[!] Unkwown Error')
# END 
