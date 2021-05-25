# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:06:26 2021

@author: mskoo
"""

import os
import tweepy
import pandas as pd
import json
import numpy as np
import nltk.tokenize
import string
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
import re

#nltk.download('stopwords')

#define tokenizer
tokenizer = TweetTokenizer(
    preserve_case=False,
    strip_handles=True,
    reduce_len=True)



english_stopwords = stopwords.words('english')

# function used for removing nested lists in python. 
def reemovNestings(df_tolist,tweet_list):
    for i in df_tolist:
        if type(i) == list:
            reemovNestings(i,tweet_list)
        else:
            tweet_list.append(i)

    return tweet_list

def Process_data(data):
    data = data_df

    # empty variables
    tweet_list = []
    tweet_tokens = []
    cleaned = []
    stemmed = []
    # rules for preprocessing of data
    START_OF_LINE = r"^"
    OPTIONAL = "?"
    ANYTHING = "."
    ZERO_OR_MORE = "*"
    ONE_OR_MORE = "+"

    SPACE = "\s"
    SPACES = SPACE + ONE_OR_MORE
    NOT_SPACE = "[^\s]" + ONE_OR_MORE
    EVERYTHING_OR_NOTHING = ANYTHING + ZERO_OR_MORE

    ERASE = ""
    FORWARD_SLASH = "\/"
    NEWLINES = r"[\r\n]"

    # removing retweets, hyperlinks, hashtags
    HYPERLINKS = ("http" + "s" + OPTIONAL + ":" + FORWARD_SLASH + FORWARD_SLASH + NOT_SPACE + NEWLINES + ZERO_OR_MORE)
    HASH = "#"
    RE_TWEET = START_OF_LINE + "RT" + SPACES

    # for loop to clean data, using the rules above
    for index in data_df.index:
        data_df['tweet'][index] = re.sub(RE_TWEET, ERASE, data_df['tweet'][index])
        data_df['tweet'][index] = re.sub(HYPERLINKS, ERASE, data_df['tweet'][index])
        data_df['tweet'][index] = re.sub(HASH, ERASE, data_df['tweet'][index])

    # create single list of tweets, probably not most efficient way to do it (using fuction above)
    df_tolist = data_df.values.tolist()
    #print('the dataframe after some processing', df_tolist[1:4])
    tweet_list=reemovNestings(df_tolist,tweet_list)
    #print('removed nesting, what happend', tweet_list[1:4])
    # tokenizing the tweets
    for sent in tweet_list:
        tweet_tokens.append(tokenizer.tokenize(sent))

    # removing stop words and punctuation
    # Download line:
    for ander in tweet_tokens:
        cleaned.append([word for word in ander if (word not in english_stopwords and word not in string.punctuation)])

    # Stemming --using Porterstemmer
    stemmer = PorterStemmer()
    for noganders in cleaned:
        stemmed.append([stemmer.stem(word) for word in noganders])

    return tweet_list,tweet_tokens,cleaned,stemmed
if __name__=='__main__':
    #read data in dataframe
    data_df = pd.read_json('data/#FCBB04_2.json', orient='records')

    x,y,z,a=Process_data(data_df)
    print(a)
    

    
    