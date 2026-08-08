#!/usr/bin/env python3

import pandas as pd 
import numpy as np 

def LoadData():  #load excel database
    df = pd.read_excel("takab-data.xls", sheet_name="Sheet1")
    return df

