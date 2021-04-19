# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 13:52:23 2021

@author: mskoo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


no_pages = 2

def get_data(pageNo):
    headers = {}