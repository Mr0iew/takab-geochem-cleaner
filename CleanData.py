#!/usr/bin/env python3

import pandas as pd 
import numpy as np 

def LoadData():  #load excel database
    df = pd.read_excel("TakabDatabase.xls", sheet_name="Sheet1")
    return df

def RemoveEmptyColumns(df): #remove columns thiw > 90% missing values
    threshold = len(df) * 0.9
    df_clean = df.dropna(axis=1, thresh=threshold)
    ## remove column1
    df_clean2 = df_clean.drop(df_clean.columns[[0,3,4]],axis=1)    
    return df_clean2




df_raw = LoadData()
df_clean = RemoveEmptyColumns(df_raw)

def CheckDuplicateSamples():
    duplicates = df_clean[df_clean["Sample_number"].duplicated(keep=False)]
    return duplicates

ch_du_sa = CheckDuplicateSamples()


def CheckDuplicateCoordinantes():
    duplicates = df_clean[ df_clean.duplicated ( subset=["X_in_utm","Y_in_utm"] , keep=False )]
    return duplicates


ch_du_co = CheckDuplicateCoordinantes()

ch_du_sa.to_excel("duplicated_sample_number.xlsx",index=False)

ch_du_co.to_excel("duplicated_sample_coordinantes.xlsx",index=False)

df_clean.to_excel("cleaned date.xlsx",index=False)
