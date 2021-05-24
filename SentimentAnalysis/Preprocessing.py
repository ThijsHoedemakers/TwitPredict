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

#define tokenizer
tokenizer = TweetTokenizer(
    preserve_case=False,
    strip_handles=True,
    reduce_len=True)

#empty variables
tweet_list=[]
tweet_tokens=[]
cleaned=[]
stemmed = []

english_stopwords = stopwords.words('english')

# function used for removing nested lists in python. 
def reemovNestings(df_tolist):
    for i in df_tolist:
        if type(i) == list:
            reemovNestings(i)
        else:
            tweet_list.append(i)

if __name__=='__main__':
    #read data in dataframe
    data_df = pd.read_json('data/#FCBB04_2.json', orient='records')
    
    #rules for preprocessing of data
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
    
    #removing retweets, hyperlinks, hashtags
    HYPERLINKS = ("http" + "s" + OPTIONAL + ":" + FORWARD_SLASH + FORWARD_SLASH + NOT_SPACE + NEWLINES + ZERO_OR_MORE)
    HASH = "#"
    RE_TWEET = START_OF_LINE + "RT" + SPACES
    
    #for loop to clean data, using the rules above
    for index in data_df.index:
        data_df['tweet'][index]= re.sub(RE_TWEET, ERASE, data_df['tweet'][index])
        data_df['tweet'][index]= re.sub(HYPERLINKS, ERASE, data_df['tweet'][index])
        data_df['tweet'][index]= re.sub(HASH, ERASE, data_df['tweet'][index])
        
    #create single list of tweets, probably not most efficient way to do it (using fuction above)
    df_tolist = data_df.values.tolist()
    reemovNestings(df_tolist)
    
    #tokenizing the tweets
    for sent in tweet_list:
        tweet_tokens.append(tokenizer.tokenize(sent))
    
    #removing stop words and punctuation
    #Download line: nltk.download('stopwords')
    for ander in tweet_tokens:
        cleaned.append([word for word in ander if (word not in english_stopwords and word not in string.punctuation)])
    
    #Stemming --using Porterstemmer   
    stemmer = PorterStemmer()         
    for noganders in cleaned: 
        stemmed.append([stemmer.stem(word) for word in noganders])
    
    