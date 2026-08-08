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

dup_samples = CheckDuplicateSamples()


def CheckDuplicateCoordinantes():
    duplicates = df_clean[ df_clean.duplicated ( subset=["X_in_utm","Y_in_utm"] , keep=False )]
    return duplicates


dup_coords = CheckDuplicateCoordinantes()

dup_samples.to_excel("duplicated_sample_number.xlsx",index=False)

dup_coords.to_excel("duplicated_sample_coordinantes.xlsx",index=False)

df_clean.to_excel("cleaned date.xlsx",index=False)

########################################################################
#some cleaning report

def GenerateReport(df_original, df_clean):
    """Generate cleaning report"""
    print("=" * 60)
    print("Mining Data Cleaning Report")
    print("=" * 60)
    print(f"Total original records: {len(df_original)}")
    print(f"Total cleaned records: {len(df_clean)}")
    print(f"Total removed records: {len(df_original) - len(df_clean)}")
    print(f"Total original columns: {len(df_original.columns)}")
    print(f"Total cleaned columns: {len(df_clean.columns)}")
    print(f"Duplicate Sample_number: {len(dup_samples)}")
    print(f"Duplicate coordinates: {len(dup_coords)}")
    print("=" * 60)

    if len(dup_samples) > 0:
        print(f"\n{len(dup_samples)} duplicate Sample_number rows:")
        print(dup_samples[['Sample_number', 'X_in_utm', 'Y_in_utm']].head())

    if len(dup_coords) > 0:
        print(f"\n{len(dup_coords)} duplicate coordinate rows:")
        print(dup_coords[['Sample_number', 'X_in_utm', 'Y_in_utm']].head())

    return dup_samples, dup_coords

dup_samples, dup_coords = GenerateReport(df_raw, df_clean)