# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:51:51 2021

@author: mskoo
"""

import tweepy 
from tweepy import (Stream, OAuthHandler)
from tweepy.streaming import StreamListener
import time
import json


#API credentials
consumer_key ='ZdQjldhzi6OobyMIcFTlrQf6X'
consumer_secret = '9VKBMLCkjeQc39IuPrqOfjkamThfzOyJ2XzGzY4oxngyLDBcQI'
access_token = '1377904369639813120-4x7d66taMhfAdU0KBz1W1Rbw0L3WZJ'
access_token_secret = 'ZlhVW3XwjeEgkdT1KXmgA1uojxKfiLfHUGeQ0yI5WLUeJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


search_term = '#DogeDay'

data=[]
tweet_details={}

#Step 1: Creating a StreamListener
class MyStreamListener(tweepy.StreamListener):
    
    def __init__(self, time_limit=600):
        self.start_time = time.time()
        self.limit = time_limit
        super(MyStreamListener, self).__init__()
        self.counter = 0
        self.counter_limit = 10
        
    
    def on_status(self, status):
        
        print(status.text)
        
        tweet_details['tweet'] = status.text
        dictionary_copy = tweet_details.copy()
        data.append(dictionary_copy)

        
        
        #Time-Limit
        if (time.time() - self.start_time) > self.limit:
            
            with open('data/{}.json'.format(search_term), 'w') as f:
                json.dump(data, f)
            print(time.time(), self.start_time, self.limit)
            return False
        
        #Tweet Limit
        self.counter+=1
        if self.counter < self.counter_limit:
            return True
        else:
            with open('data/{}.json'.format(search_term), 'w') as f:
                json.dump(data, f)
                return False

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

        


#Step 2: Creating a Stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#Step 3: Starting a Stream
myStream.filter(languages=['en'] ,track=search_term)






