# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:17:03 2022

@author: grper
"""

import pandas as pd
import numpy as np
# %% File reads

loc_keys = {'ARBID':str,'Zip Code':str,'FACID':str,'NAICS Code':str,'Year':str}

raw_loc = pd.read_csv('Input_data/FacilityEmissions.csv',dtype=loc_keys,skipfooter=1
                       ,index_col='ARBID')
emit = pd.read_csv('Pct_Data.csv',dtype=loc_keys,index_col=["ARBID",'Year'])


# %% Drop columns
keep_col = ['Facility','NAICS Code','Address','Latitude','Longitude',
            'Cap-and-Trade']
keep_loc = raw_loc[keep_col]
keep_loc = keep_loc.rename(columns={'Cap-and-Trade':'cap_and_trade'})

# %% Merges
emit.reset_index(inplace=True)
emit.set_index('ARBID',inplace=True)
merged = emit.merge(keep_loc,on='ARBID',how='right',indicator=True)
print(merged["_merge"].value_counts())
merged.drop(columns='_merge',inplace=True)
merged = merged.set_index(['Year'],append=True)
cap_only = merged.query('cap_and_trade == "Yes"')
cap_only.drop(columns='cap_and_trade',inplace=True)
cap_only = cap_only.replace(cap_only['pct_emission']==0,np.nan)
cap_only.to_csv('geo_merged.csv')