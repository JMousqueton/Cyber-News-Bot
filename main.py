import tweepy
from datetime import datetime, timezone
from configparser import ConfigParser

config = ConfigParser(interpolation=None)
config.read('config.cfg')
log = config.get('Bot','log')
API_key = config.get('Twitter', 'API_Key')
API_key_secret = config.get('Twitter', 'API_Key_secret')
access_token = config.get('Twitter', 'Access_token')
access_token_secret = config.get('Twitter', 'Access_token_secret')
Bearer_token = config.get('Twitter', 'Bearer_token', raw=True)
hashtags = config.get('Bot', 'Hashtags')
hashtags = hashtags.split(',')
LastRun = config.get('Bot','LastRun')
now = datetime.utcnow().isoformat(timespec='seconds')+'Z'
if LastRun == '': 
	config.set('Bot', 'LastRun', str(now)) 
	with open("config.cfg", 'w') as f:
	    config.write(f)
	exit()

config.set('Bot', 'LastRun', str(now)) 
with open("config.cfg", 'w') as f:
	config.write(f)

client = tweepy.Client(bearer_token=Bearer_token.replace("'", ""), consumer_key=API_key, consumer_secret=API_key_secret, access_token=access_token, access_token_secret=access_token_secret)
for hash in hashtags:
	tweets=client.search_recent_tweets(query='#' + hash.replace("'", "").replace(' ', '') + ' -RT',start_time=LastRun, tweet_fields=['context_annotations', 'created_at'], max_results=50)
	if not tweets.data: 
		if log == 'True': 
			print('no new tweet for #'+hash.replace("'", "").replace(' ', ''))
	else:
		for tweet in tweets.data:
			if log == 'True': 
				print('#' + hash.replace("'", "").replace(' ', '') + ' ' + str(tweet.id) + ' ' + str(tweet.created_at))
			client.retweet(tweet.id)