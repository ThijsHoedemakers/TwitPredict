# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:45:48 2021

@author: mskoo
"""

import os
import tweepy as tw
import pandas as pd
import json
import numpy as np


consumer_key ='ZdQjldhzi6OobyMIcFTlrQf6X'
consumer_secret = '9VKBMLCkjeQc39IuPrqOfjkamThfzOyJ2XzGzY4oxngyLDBcQI'
access_token = '1377904369639813120-4x7d66taMhfAdU0KBz1W1Rbw0L3WZJ'
access_token_secret = 'ZlhVW3XwjeEgkdT1KXmgA1uojxKfiLfHUGeQ0yI5WLUeJ'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)




# Define the search term and the date since date as variables
search_terms    = ['#LIVREA']
date_until      = '2021-04-07'

def stream_tweets(search_term):
    data = [] #empty list to which tweet_details obj will be added
    counter = 0 #counter to keep track of each iteration
    for tweet in tw.Cursor(api.search, q='\"{}\" -filter:retweets'.format(search_term), result_type= 'recent', count=100, until = date_until,  lang='en', tweet_mode='extended').items():
        tweet_details={}
        tweet_details['name'] = tweet.user.screen_name
        tweet_details['tweet'] = tweet.full_text
        tweet_details['retweets'] = tweet.retweet_count
        tweet_details['location'] = tweet.user.location
        tweet_details['created'] = tweet.created_at.strftime("%d-%b-%Y")
        tweet_details['followers'] = tweet.user.followers_count
        tweet_details['is_user_verified'] = tweet.user.verified
        data.append(tweet_details)
        
        counter += 1 
        if counter ==100:
            break
        else:
            pass
    with open('data/{}.json'.format(search_term), 'w') as f:
        json.dump(data, f)
    print('done!')
    
def create_df():
    data_df = pd.read_json('data/#BAYPSG.json', orient='records')
    return data_df


if __name__=='__main__':
    print('Starting to stream...')
    for search_term in search_terms:
        stream_tweets(search_term)
    print('finished!')
    
    data_df = pd.read_json('data/#REALIV.json', orient='records')
    print('dataframe created')