#!/usr/bin/env python3

import pandas as pd 
import numpy as np 

def LoadData():  #load excel database
    df = pd.read_excel("TakabDatabase.xls", sheet_name="Sheet1")
    return df

def RemoveEmptyColumns(df): #remove columns thiw > 90% missing values
    threshold = len(df) * 0.9
    df_clean = df.dropna(axis=1, thresh=threshold)
    return df_clean

df_raw = LoadData()
df_clean = RemoveEmptyColumns(df_raw)
