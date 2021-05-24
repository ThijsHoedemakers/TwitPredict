# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:39:36 2021

@author: mskoo
"""

import pandas as pd

data_df = pd.read_json('data/#FCBB04_2.json', orient='records')
data_df["tweet"] = data_df["tweet"].astype(str)
data_df["label"] = "" 
data_df = data_df.replace(r'\\n',' ', regex=True) 

#print(data_df.dtypes)

data_df.to_csv("labelledtweets.csv")

l = [['aa', 'bb'],['aaa', 'bbb', 'ccc']]

test = [''.join(x) for x in l]
print(test)