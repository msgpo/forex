#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 15:20:22 2017

@author: applesauce
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


file_name = 'EUR_USD_M1'
df = pd.read_pickle('../data/'+file_name)
df.sort_values('time', inplace=True)
df.set_index('time', inplace=True)
df = df.loc[datetime(2015, 1, 1):, :]
fig, ax = plt.subplots()
ax.plot(df.close)
ax.set_title(file_name)
plt.show()
