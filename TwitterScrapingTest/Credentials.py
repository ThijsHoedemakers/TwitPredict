# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:45:16 2021

@author: mskoo
"""

import tweepy as tw
from tweepy import OAuthHandler

def Credentials():    
    consumer_key ='ZdQjldhzi6OobyMIcFTlrQf6X'
    consumer_secret = '9VKBMLCkjeQc39IuPrqOfjkamThfzOyJ2XzGzY4oxngyLDBcQI'
    access_token = '1377904369639813120-4x7d66taMhfAdU0KBz1W1Rbw0L3WZJ'
    access_token_secret = 'ZlhVW3XwjeEgkdT1KXmgA1uojxKfiLfHUGeQ0yI5WLUeJ'

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    return auth

if __name__=='__main__':
    print('LOL')
    
    x = Credentials()
    print(x)