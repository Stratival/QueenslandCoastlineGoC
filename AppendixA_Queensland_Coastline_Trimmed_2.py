# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:29:34 2021

@author: valentz
Insipired by https://matplotlib.org/matplotblog/posts/warming-stripes/
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.colors import ListedColormap
import geopandas as gpd
import pandas as pd
from cmcrameri import cm
import numpy as np
from shapely.geometry import box

from scipy.interpolate import make_interp_spline



# Path to geopackage data
gpkg_path = 'D:\Queensland_Coastline\DEACoastlines_gpkg_v1.0.0\DEACoastlines_gpkg_v1.0.0\DEACoastlines_v1.0.0.gpkg'

# Input coords
miny, minx =  -13.26780, 140.82801
maxy, maxx = -17.46528, 141.69620

# Create bounding box and use this to load data using geopandas
bbox = gpd.GeoSeries(box(minx, miny, maxx, maxy), crs='EPSG:4326')
points_gdf = gpd.read_file(gpkg_path, layer='DEACoastlines_ratesofchange_v1.0.0', bbox=bbox)

# Plot
points_gdf.plot()

# Coordinates will be in Australian Albers (`EPSG:3577`) with metre units
# To convert to degrees lat/lon:
#points_gdf = points_gdf.to_crs('EPSG:4326')

# Add x and y coords as new field
points_gdf['x_coord'] = points_gdf.geometry.x
points_gdf['y_coord'] = points_gdf.geometry.y

# Create new index based on y coords, and sort
points_gdf = points_gdf.set_index('y_coord').sort_index(ascending=False)

# Reset index to get incremental ids
points_gdf = points_gdf.reset_index()
points_gdf
points_gdf.to_csv('Queensland_Coastline_ShortTrimmedCSV.csv')


#1. Adding extra column of 2019-1988, don't need to be run once the column was added
#CstLine = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV.csv') #, index_col=0, usecols=(0, 48), header=0) #, index_col=0, usecols=(49), names=['NetCstBehav_m'], header=None,)
#print(CstLine)
#pd.set_option('display.max_columns', None)
#CstLine.head()
#CstLine["NetCstBehav_m"] =  CstLine['dist_2019'] - CstLine['dist_1988']
#CstLine.to_csv("Queensland_Coastline_ShortTrimmedCSV_19882019.csv", index=False)
#print(CstLine)

#NetCstBehav = CstLine["nsm"]
#max_value = NetCstBehav.max()
#min_value = NetCstBehav.min()

#print(max_value)
#print(min_value)

#print(CstLine)

#2. working with new file to plot the overall erosion or regression between 1988 and 2019 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine2 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0, 44), names=['y_coord', 'NSM'], header=0,) #names=['y_coord', 'NetCstBehav_m']
pd.set_option('display.max_columns', None)
CstLine2.head()
print(CstLine2)


FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


NetCstBehav_m2 = CstLine2.loc[FIRST:LAST, 'NSM'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()

#Colourmap when using NSM --> cmap=ListedColormap([#4292c6','##ef3b2c',])
#Colourmap when using dist --> cmap=ListedColormap(['#ef3b2c', '#4292c6',])
cmap=ListedColormap([
    '#4292c6',
    '#ef3b2c',
])
fig = plt.figure(figsize=(200, 20))

ax = fig.add_axes([0, 0, 1, 1])
ax.set_axis_off()

# create a collection with a rectangle for each year

col = PatchCollection([Rectangle((y, 0), 1, 1)
    for y in range(FIRST, LAST + 1)])

# set data, colormap and color limits

col.set_array(NetCstBehav_m2)
col.set_cmap(cmap)
#col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripesFinal.png')
fig.savefig('_CoastalStripesFinal.svg')




from cmcrameri.cm import show_cmaps 
show_cmaps()


