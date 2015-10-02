#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '2xNsI9iktjW7kTijjwqY2U12l'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '8OIGTb9og7Hi2wAocApON7iF7pCuRmqXxqW7ziFK3HUEsPIzYz'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '123623980-mZqL9Mng0q11i6P53GlA2wgQxXAIcQu06xWeu05t'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'EdcEWQGiv3SX3Y2BVXiGsoyGTQvWg2IeGAYkuHp0r7ZsV'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(status="The testscript has tweeted")
time.sleep(900)#Tweet every 15 minutes