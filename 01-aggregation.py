# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:48:49 2022

@author: grper
"""

import pandas as pd

# %% Reading files
# Individual files need 
files = {
    '2011-ghg-emissions-2018-11-05.xlsx': {'header':8},
    '2012-ghg-emissions-2019-11-04.xlsx': {'header':8},
    '2013-ghg-emissions-2019-11-04.xlsx': {'header':8},
    '2014-ghg-emissions-2019-11-04.xlsx': {'header':8}, 
    '2015-ghg-emissions-2019-11-04.xlsx': {'header':8},
    '2016-ghg-emissions-2020-11-04.xlsx': {'header':8},
    '2017-ghg-emissions-2020-11-04.xlsx': {'header':8},
    '2018-ghg-emissions-2021-11-04.xlsx': {'header':8},
    '2019-ghg-emissions-2021-11-04.xlsx': {'header':9},
    '2020-ghg-emissions-2021-11-04.xlsx': {'header':8}
    }

sheet_name = 'GHG Data'
arb = {"Report\nYear":str,"ARB ID":str,"Zip Code":str}
raw_emit = pd.DataFrame()
datalist=[]

for cur in files:
    parts = cur.split('-')
    year = parts[0]
    file_info = files[cur]
    hlines = file_info['header']
    fh = pd.read_excel('Input_data/'+cur,sheet_name = year+" "+sheet_name,header=hlines,
                       index_col='ARB ID',dtype=arb)
    datalist.append(fh)
    print(f'File read: {cur}')
print(datalist[0].index)

# %%
raw_emit = pd.concat(datalist)
drops = [c for c in raw_emit.columns if c.startswith("Unnamed")]
raw_emit = raw_emit.drop(columns = drops)
raw_emit = raw_emit.reset_index()
raw_emit.columns = raw_emit.columns.str.replace(r'\s',' ',regex=True)
raw_emit = raw_emit.rename(columns={'Report Year':'Year',"ARB ID":'ARBID','Total CO2e  (combustion, process, vented, and supplier)':'Total CO2e'})
raw_emit.set_index(["ARBID",'Year'],inplace=True)
keep_col = ['Facility Name','Total CO2e','Total Covered Emissions','Total Non-Covered Emissions ','Zip Code',
            'North American Industry Classification System (NAICS)  Code and Description']
# drop_col = ['AEL','Emissions Data','Product Data','Verification Body','U.S.EPA/ARB Subparts']
# raw_emit.drop(columns = drop_col,inplace=True)
raw_emit = raw_emit[keep_col]
raw_emit.to_csv('Stack_Ag_Emit.csv')