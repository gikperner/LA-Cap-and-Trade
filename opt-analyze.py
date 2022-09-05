# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:51:26 2022

@author: grper
"""

import pandas as pd
import matplotlib.pyplot as plt

loc_keys = {'ARBID':str,'Zip Code':str,'FACID':str,'NAICS Code':str,'Year':str}

emit = pd.read_csv('geo_merged.csv',index_col=["ARBID",'Year'])

# %% Do some summary stats
hi_low = emit.sort_values('Total Covered Emissions',ascending=False)

highest = hi_low[:20]
highest = highest.reset_index()
highest.set_index((highest['Legal Name'])+" "+(highest['Year'].astype(str)),inplace=True)
high_emit = highest['Total Covered Emissions']

fig1,ax1 = plt.subplots(dpi=300)
ax1.set_title('Top Emitters')
ax1.set_xlabel('Metric Tons of CO2e')
high_emit.plot.barh(ax=ax1,figsize=(50,20))

year_emit = emit['Total Covered Emissions'].groupby('Year').rank(method='min',ascending=False)
year_order = year_emit.sort_values()

year_graph = emit[(year_emit==1)|(year_emit==2)]
year_graph = year_graph.reset_index()
year_graph.set_index((year_graph['Legal Name'])+" "+(year_graph['Year'].astype(str)),inplace=True)
year_graph = year_graph['Total Covered Emissions']
year_graph = year_graph.sort_values()
fig2,ax2 = plt.subplots(dpi=300)
ax2.set_title('Top 2 Emitters Each Year')
ax2.set_xlabel('Metric Tons of CO2e')
year_graph.plot.barh(ax=ax2,figsize=(50,20))

fig1.tight_layout()
fig2.tight_layout()
fig1.savefig('Top_Emitters.png')
fig2.savefig('Yearly_2_Emitters.png')