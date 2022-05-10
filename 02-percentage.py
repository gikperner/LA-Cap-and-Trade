# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:44:22 2022

@author: grper
"""

import pandas as pd

# %% Data read

sheet = '2019 Compliance Summary'
state = pd.read_excel('2019compliancereport.xlsx',sheet_name = sheet,header=4,skipfooter=11)

emit = pd.read_csv('Stack_Ag_Emit.csv',dtype={'ARBID':str,'Year':str})
emit.set_index(['ARBID'],inplace=True)

# %% Cleaning

state.columns = state.columns.str.replace(r'\s',' ',regex=True)

state.set_index(['Entity ID','Legal Name'],inplace=True)

state = state['ARB GHG ID'].astype(str)

state = state.reset_index()

state.set_index(['Entity ID'],inplace=True)

state['ARB GHG ID'] = state['ARB GHG ID'].str.replace(r'\s','',regex=True)

state['ARBID'] = state['ARB GHG ID'].str.split(',')

state.drop(columns='ARB GHG ID',inplace=True)

state.to_csv('Entities_ARBID.csv')

# %%

entity = state.explode('ARBID')
entity = entity.reset_index()
entity = entity.set_index('ARBID')

merged = emit.merge(entity,on='ARBID',how = 'left')

grouped_total = merged.groupby(['Year','Entity ID']).sum()

grouped_covered = grouped_total[['Total Covered Emissions']]
entity = entity.reset_index()
entity.set_index('Entity ID',inplace=True)
grouped_covered.reset_index(inplace=True)
grouped_covered.set_index('Entity ID')
new_entity = grouped_covered.merge(entity,on='Entity ID',how='outer')
new_entity = new_entity.rename(columns={'Total Covered Emissions':'Entity Emissions'})
# entity = entity.join(grouped_covered)
# grouped_total.reset_index(inplace=True)
# new_entity.set_index('Entity ID',inplace=True)
# entity = entity.reset_index()
# entity.set_index('Entity ID',inplace=True)
# ent_tot = entity.merge(grouped_total,on='Entity ID', how='left')

# %% Share of emissions
new_entity.set_index(['ARBID','Year'],inplace=True)
emit.set_index('Year',append=True,inplace=True)
cov_merge = emit.merge(new_entity,on=['ARBID','Year'],how='left')
cov_merge['pct_emission'] = 100*cov_merge['Total Covered Emissions']/cov_merge['Entity Emissions']
cov_merge.to_csv('Pct_Data.csv')