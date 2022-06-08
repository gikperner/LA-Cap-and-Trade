# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:03:54 2022

@author: grper
"""

import pandas as pd
import geopandas as gpd
import os

# %% File reads
filename = 'yearly_data.gpkg'

loc_keys = {'ARBID':str,'Zip Code':str,'FACID':str,'NAICS Code':str,'Year':str}
emit = pd.read_csv('geo_merged.csv',index_col="ARBID",dtype=loc_keys)

ca_map = gpd.read_file('Input_data/calenviroscreen40shpf2021shp.zip')

la_map = ca_map.query('County=="Los Angeles"')

# %%
years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
drop_col = ['Latitude','Longitude']
if os.path.exists(filename):
    os.remove(filename)

la_map.to_file(filename,layer='Enviroscreen_LA',index=False)
emit.reset_index(inplace=True)

all_geo = gpd.GeoDataFrame(data=emit,geometry=gpd.points_from_xy(emit.Longitude,emit.Latitude))
all_geo.drop(columns=drop_col,inplace=True)
all_geo = all_geo.set_crs("EPSG:4326")
all_geo = all_geo.to_crs(la_map.crs)
all_geo.to_file(filename,layer="All Year Data")

for cur in years:
    data = emit.query('Year == @cur')
    # how to create GeoDataFrame from 
    # https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html
    geo = gpd.GeoDataFrame(data=data,geometry=gpd.points_from_xy(data.Longitude,data.Latitude))
    geo.drop(columns=drop_col,inplace=True)
    geo = geo.set_crs("EPSG:4326")
    geo = geo.to_crs(la_map.crs)
    geo.to_file(filename,layer=cur+' emissions',index=False)