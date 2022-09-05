# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:44:22 2022

@author: grper
"""

import pandas as pd

files = {
    '2013compliancereport.xlsx':{'Year':['2013','2011','2012','2014']},
    '2015compliancereport.xlsx':{'Year':['2015']},
    '2016compliancereport.xlsx':{'Year':['2016','2017']},
    '2018compliancereport.xlsx':{'Year':['2018']},
    '2019compliancereport.xlsx':{'Year':['2019','2020']}
    }

# %% Data read
state_years = pd.DataFrame()
for cur in files:
    file_info = files[cur]
    for year in file_info['Year']:
        file_base = file_info['Year']
        file_base = file_base[0]
        if file_base == '2':
            sheet = year+' Compliance Summary'
            state = pd.read_excel('Input_data/'+cur,sheet_name = sheet,header=4,skipfooter=11)
            state['Year'] = year
            state_years = pd.concat([state_years,state])
            
        else:
            sheet = file_base+' Compliance Summary'
            state = pd.read_excel('Input_data/'+cur,sheet_name = sheet,header=4,skipfooter=11)
            state['Year'] = year
            state_years = pd.concat([state_years,state])
# notes about the data as well as totals kept at the bottom of the spreadsheet
# and are not needed for this script.

emit = pd.read_csv('Stack_Ag_Emit.csv',dtype={'ARBID':str,'Year':str})
emit.set_index(['ARBID'],inplace=True)

# %% Cleaning
# spreadsheet was formatted for presentation in Excel, including new lines in
# column names.
state_years.columns = state_years.columns.str.replace(r'\s',' ',regex=True)

state_years.set_index(['Entity ID','Legal Name','Year'],inplace=True)
# some ARBIDs are stored as integers, but leading zeroes are not a concern
state_years = state_years['ARB GHG ID'].astype(str)

state_years = state_years.reset_index()

# %% Finding ARBIDs for all Entities

state_years.set_index(['Entity ID'],inplace=True)
# some lists will have white spaces between the comma and the next ID
state_years['ARB GHG ID'] = state_years['ARB GHG ID'].str.replace(r'\s','',regex=True)
# splits any entity with multiple sites into a list of ARBIDs
state_years['ARBID'] = state_years['ARB GHG ID'].str.split(',')

state_years.drop(columns='ARB GHG ID',inplace=True)

state_years.to_csv('Yearly_Entities_ARBID.csv')

# %% Finding total emissions by entity
# creates an entity id for all the ARBIDs
entity = state_years.explode('ARBID')
entity = entity.reset_index()
entity = entity.set_index('ARBID')

# merges the entity ids onto the merged data sets
merged = emit.merge(entity,on=['ARBID','Year'],how = 'left',indicator=True)

# groups all entities on year and entity id and sums all emissions
grouped_total = merged.groupby(['Year','Entity ID']).sum()

# creates a new dataframe for total covered emissions
grouped_covered = grouped_total[['Total Covered Emissions']]
entity = entity.reset_index()
entity.set_index('Entity ID',inplace=True)
grouped_covered.reset_index(inplace=True)
grouped_covered.set_index('Entity ID')
# creates a dataframe of total entity emissions
new_entity = grouped_covered.merge(entity,on=['Entity ID','Year'],how='outer')
new_entity = new_entity.rename(columns={'Total Covered Emissions':'Entity Emissions'})

# %% Share of emissions
new_entity.set_index(['ARBID','Year'],inplace=True)
emit.set_index('Year',append=True,inplace=True)
cov_merge = emit.merge(new_entity,on=['ARBID','Year'],how='left')
cov_merge['pct_emission'] = 100*cov_merge['Total Covered Emissions']/cov_merge['Entity Emissions']
cov_merge.to_csv('Pct_Data.csv')