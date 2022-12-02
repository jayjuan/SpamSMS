# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:25:39 2022

@author: jjuan
"""

import pandas as pd
import numpy as np

df = pd.read_csv('spam.csv', encoding = "ISO-8859-1")
df = df.fillna('')

tmp = df[df['Unnamed: 2'].notna()]
tmp2 = df[df['Unnamed: 3'].notna()]
tmp3 = df[df['Unnamed: 4'].notna()]
df['Unnamed: 2'].isna()

df['Text'] = df['v2'] + df['Unnamed: 2'] + df['Unnamed: 3'] + df['Unnamed: 4']

df_clean = pd.DataFrame()
df_clean['Text'] = df['Text']
df_clean['Target'] = df['v1']

# df_clean.loc[df_clean['Target']=='spam', 'Target'] = 1 

df_clean['Target'] = np.where(df_clean['Target'] == 'spam', 1, 0) # spam is 1 , no spam is 0

