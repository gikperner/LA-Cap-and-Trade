# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 20:37:26 2022

@author: grper
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

keys = {'Tract':str,'ZIP':str,'ARBID':str,'Year':str,'Zip Code':str,'NAICS Code':str}

data16 = pd.read_csv('Buffer_Data.csv',dtype=keys)
data16.drop(columns=['fid','fid_2'],inplace=True)
data80 = pd.read_csv('Buffer_Data_8000.csv',dtype=keys)
data80.drop(columns=['fid','fid_2'],inplace=True)
def graph(data):
    pop_pct = data[['PopChar','pct_emission']]
    
    pop_pct['PopChar'] = pop_pct['PopChar'].replace((-999),np.nan)
    
    fig1, ax1 = plt.subplots()
    sns.regplot('pct_emission','PopChar',data=pop_pct)
    
    
    # unreadble, but at least can look at something
    arb_pop = data[['Facility Name','PopChar']]
    arb_pop['PopChar'] = arb_pop['PopChar'].replace((-999),np.nan)
    arb_pop = arb_pop.groupby('Facility Name')
    arb_pop = arb_pop['PopChar'].mean()
    fig2, ax2 = plt.subplots()
    arb_pop.plot.barh(ax=ax2)
    fig2.tight_layout()
    
    naics_pop = data[['North American Industry Classification System (NAICS)  Code and Description','PopChar']]
    naics_pop['PopChar'] = naics_pop['PopChar'].replace((-999),np.nan)
    naics_pop = naics_pop.groupby('North American Industry Classification System (NAICS)  Code and Description')
    naics_pop = naics_pop['PopChar'].mean()
    fig3, ax3 = plt.subplots()
    naics_pop.plot.barh(ax=ax3)
    fig3.tight_layout()
    
    
graph(data=data16)
graph(data=data80)


# better to do this as merge data and probably make a function
print(data16['NAICS Code'].value_counts())
print(data16['ARBID'].value_counts())