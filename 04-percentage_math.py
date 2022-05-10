# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:27:04 2022

@author: grper
"""

import pandas as pd
import matplotlib.pyplot as plt

loc_keys = {'ARBID':str,'Zip Code':str,'FACID':str,'NAICS Code':str,'Year':str}

emit = pd.read_csv('Stack_Merge3.csv',index_col=["ARBID",'Year'])

# %%
hi_low = emit.sort_values('pct_emission')

highest = hi_low[:20]
highest = highest.reset_index()
highest.set_index((highest['Legal Name'])+" "+(highest['Year'].astype(str)),inplace=True)
high_pct = highest['pct_emission']

fig1,ax1 = plt.subplots(dpi=300)
ax1.set_title('Lowest Percentage of Total Emissions')
high_pct.plot.barh(ax=ax1)

year_pct = emit['pct_emission'].groupby('Year').rank(method='min',ascending=True)
year_order = year_pct.sort_values()

year_graph = emit[(year_pct==1)|(year_pct==2)]
year_graph = year_graph.reset_index()
year_graph.set_index((year_graph['Legal Name'])+" "+(year_graph['Year'].astype(str)),inplace=True)
year_graph = year_graph['pct_emission']
year_graph = year_graph.sort_values()
fig2,ax2 = plt.subplots(dpi=300)
ax2.set_title('Lowest 2 Percentage Emitters Each Year')
year_graph.plot.barh(ax=ax2)

year_graph = emit[(year_pct==10)|(year_pct==11)]
year_graph = year_graph.reset_index()
year_graph.set_index((year_graph['Legal Name'])+" "+(year_graph['Year'].astype(str)),inplace=True)
year_graph = year_graph['pct_emission']
year_graph = year_graph.sort_values()
fig3,ax3 = plt.subplots(dpi=300)
ax3.set_title('Top 2 Emitters Each Year')
year_graph.plot.barh(ax=ax3)

fig1.tight_layout()
fig2.tight_layout()
fig1.savefig('Lowest_pct.png')
fig2.savefig('Lowest_pct_yr.png')