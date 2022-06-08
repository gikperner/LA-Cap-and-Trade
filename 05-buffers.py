# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 13:22:00 2022

@author: grper
"""

import geopandas as gpd
# import matplotlib.pyplot as plt

years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
radius = [200,400,600,800,1000,1200,1400,1600,3200]

for cur in years:   
    layer = gpd.read_file(filename='yearly_data.gpkg',layer=cur+' emissions')
    layer_buf1 = layer.buffer(1600)
    layer_buf1 = layer_buf1.to_crs(layer.crs)
    layer_buf2 = layer.buffer(8000)
    layer_buf2 = layer_buf2.to_crs(layer.crs)  
    layer_buf1.to_file('yearly_data.gpkg',layer=cur+' 1600m buffer',index=False)
    layer_buf2.to_file('yearly_data.gpkg',layer=cur+' 8000m buffer',index=False)

# layer['buffer_1600'] = layer_buf1

# doing some stuff
# ej = gpd.read_file(filename='yearly_data.gpkg',layer="Enviroscreen_LA")
# slice16 = layer.sjoin(ej,how='left',predicate='intersects')

# slice16.to_file(filename='test.gpkg')
# layer = gpd.read_file(filename='yearly_data.gpkg',layer='2011 emissions')
# ring_layer = gpd.GeoDataFrame()
# geo_list = []
# last_buf = None
# for r in radius:
#      this_buf  = layer.buffer(r)
#      if len(geo_list) == 0:
#          geo_list.append(this_buf[0])
#      else:
#          change = this_buf.difference(last_buf)
#          geo_list.append(change[0])
#      last_buf = this_buf
# ring_layer['geometry'] = geo_list
# ring_layer = ring_layer.set_crs(layer.crs)
# ring_layer.to_file('yearly_data.gpkg',layer='2011 buffer',index=False)


# for cur in years:
    # layer = gpd.read_file(filename='yearly_data.gpkg',layer=cur+' emissions')
    # ring_layer = gpd.GeoDataFrame()
    # ring_layer['radius'] = radius
    # geo_list = []
    # last_buf = None
    # print(f'{cur} layer read')
    # for r in radius:
    #     this_buf  = layer.buffer(r)
    #     if len(geo_list) == 0:
    #         geo_list.append(this_buf[0])
    #     else:
    #         change = this_buf.difference(last_buf)
    #         geo_list.append(change[0])
    #     last_buf = this_buf
    # ring_layer['geometry'] = geo_list
    # ring_layer = ring_layer.set_crs(layer.crs)
    # print(f'{cur} buffers made')
    # ring_layer.to_file('yearly_data.gpkg',layer=cur+' buffer',index=False)
    # print(f'{cur} buffers saved')