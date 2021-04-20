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

def create_df():
    return data_df

if __name__=='__main__':
    data_df = pd.read_json('data/#DogeDay.json', orient='records')

    #data = create_df()