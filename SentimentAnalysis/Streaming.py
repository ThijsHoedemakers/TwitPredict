# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:51:51 2021

@author: mskoo
"""

import tweepy 
import time


#APi credentials
consumer_key ='ZdQjldhzi6OobyMIcFTlrQf6X'
consumer_secret = '9VKBMLCkjeQc39IuPrqOfjkamThfzOyJ2XzGzY4oxngyLDBcQI'
access_token = '1377904369639813120-4x7d66taMhfAdU0KBz1W1Rbw0L3WZJ'
access_token_secret = 'ZlhVW3XwjeEgkdT1KXmgA1uojxKfiLfHUGeQ0yI5WLUeJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Step 1: Creating a StreamListener
class MyStreamListener(tweepy.StreamListener):
    
    def __init__(self, start_time, time_limit=60):
        self.time = start_time
        self.limit = time_limit

    def on_status(self, status):
        print(status.text)
        
    def on_data(self, data):
        while(time.time()-self.time) < self.limit:
            try: 
                saveFile = open('abcd.json', 'a')
                saveFile.write(data)
                saveFile.write('\n')
                saveFile.close()
                return True
            except BaseException as e:
                print('failed ondata,'), str(e)
                time.sleep(5)
        return True
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        
#Step 2: Creating a Stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())

#Step 3: Starting a Stream
myStream.filter(track=['python'])






