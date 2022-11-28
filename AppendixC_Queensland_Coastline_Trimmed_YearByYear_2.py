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


#legend
#x = np.linspace(0, 16, 16)[None, :]
#plt.imshow(x, aspect='auto', cmap=cm.vik) # or any other colourmap
#plt.axis('off')
#plt.show()



#from cmcrameri.cm import show_cmaps 
#show_cmaps()

#0 selecting queensland coastline
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



#2. working with new file to plot the yearly erosion or regression between 1988 and 1989 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine8889 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,8, 9), names=['y_coord', 'dist_1988', 'dist_1989'], header=0,)
pd.set_option('display.max_columns', None)
CstLine8889.head()
print(CstLine8889)

CstLine8889["dist_1988-dist_1989"] =  CstLine8889['dist_1988'] - CstLine8889['dist_1989']
print(CstLine8889)



FIRST = 1
LAST = 4590


reference=0
LIM = 20 # meters


CstLine8889Plot = CstLine8889.loc[FIRST:LAST, 'dist_1988-dist_1989'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine8889Plot)


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

col.set_array(CstLine8889Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_8889.png')
fig.savefig('_CoastalStripes_8889.svg')


#3. working with new file to plot the yearly erosion or regression between 1989 and 1990 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine8990 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,9, 10), names=['y_coord', 'dist_1989', 'dist_1990'], header=0,)
pd.set_option('display.max_columns', None)
CstLine8889.head()
print(CstLine8990)

CstLine8990["dist_1989-dist_1990"] =  CstLine8990['dist_1989'] - CstLine8990['dist_1990']
print(CstLine8990)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine8990Plot = CstLine8990.loc[FIRST:LAST, 'dist_1989-dist_1990'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine8990Plot)

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

col.set_array(CstLine8990Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_8990.png')
fig.savefig('_CoastalStripes_8990.svg')


#4. working with new file to plot the yearly erosion or regression between 1990 and 1991 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine9091 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,10, 11), names=['y_coord', 'dist_1990', 'dist_1991'], header=0,)
pd.set_option('display.max_columns', None)
CstLine9091.head()
print(CstLine9091)

CstLine9091["dist_1990-dist_1991"] =  CstLine9091['dist_1990'] - CstLine9091['dist_1991']
print(CstLine9091)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine9091Plot = CstLine9091.loc[FIRST:LAST, 'dist_1990-dist_1991'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine9091Plot)

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

col.set_array(CstLine9091Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_9091.png')
fig.savefig('_CoastalStripes_9091.svg')


#5. working with new file to plot the yearly erosion or regression between 1991 and 1992 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine9192 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,11, 12), names=['y_coord', 'dist_1991', 'dist_1992'], header=0,)
pd.set_option('display.max_columns', None)
CstLine9192.head()
print(CstLine9192)

CstLine9192["dist_1991-dist_1992"] =  CstLine9192['dist_1991'] - CstLine9192['dist_1992']
print(CstLine9192)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine9192Plot = CstLine9192.loc[FIRST:LAST, 'dist_1991-dist_1992'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine9192Plot)

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

col.set_array(CstLine9192Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_9192.png')
fig.savefig('_CoastalStripes_9192.svg')


#6. working with new file to plot the yearly erosion or regression between 1992 and 1993 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine9293 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,12, 13), names=['y_coord', 'dist_1992', 'dist_1993'], header=0,)
pd.set_option('display.max_columns', None)
CstLine9293.head()
print(CstLine9293)

CstLine9293["dist_1992-dist_1993"] =  CstLine9293['dist_1992'] - CstLine9293['dist_1993']
print(CstLine9293)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine9293Plot = CstLine9293.loc[FIRST:LAST, 'dist_1992-dist_1993'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine9293Plot)

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

col.set_array(CstLine9293Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_9293.png')
fig.savefig('_CoastalStripes_9293.svg')


#7. working with new file to plot the yearly erosion or regression between 1993 and 1994 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine9394 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,13, 14), names=['y_coord', 'dist_1993', 'dist_1994'], header=0,)
pd.set_option('display.max_columns', None)
CstLine9394.head()
print(CstLine9394)

CstLine9394["dist_1993-dist_1994"] =  CstLine9394['dist_1993'] - CstLine9394['dist_1994']
print(CstLine9394)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine9394Plot = CstLine9394.loc[FIRST:LAST, 'dist_1993-dist_1994'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine9394Plot)

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

col.set_array(CstLine9394Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_9394.png')
fig.savefig('_CoastalStripes_9394.svg')


#8. working with new file to plot the yearly erosion or regression between 1994 and 1995 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine9495 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,14, 15), names=['y_coord', 'dist_1994', 'dist_1995'], header=0,)
pd.set_option('display.max_columns', None)
CstLine9495.head()
print(CstLine9495)

CstLine9495["dist_1994-dist_1995"] =  CstLine9495['dist_1994'] - CstLine9495['dist_1995']
print(CstLine9495)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine9495Plot = CstLine9495.loc[FIRST:LAST, 'dist_1994-dist_1995'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine9495Plot)

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

col.set_array(CstLine9495Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_9495.png')
fig.savefig('_CoastalStripes_9495.svg')


#9. working with new file to plot the yearly erosion or regression between 1995 and 1996 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine9596 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,15, 16), names=['y_coord', 'dist_1995', 'dist_1996'], header=0,)
pd.set_option('display.max_columns', None)
CstLine9596.head()
print(CstLine9596)

CstLine9596["dist_1995-dist_1996"] =  CstLine9596['dist_1995'] - CstLine9596['dist_1996']
print(CstLine9596)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine9596Plot = CstLine9596.loc[FIRST:LAST, 'dist_1995-dist_1996'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine9596Plot)

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

col.set_array(CstLine9596Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_9596.png')
fig.savefig('_CoastalStripes_9596.svg')



#10. working with new file to plot the yearly erosion or regression between 1996 and 1997 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine9697 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,16, 17), names=['y_coord', 'dist_1996', 'dist_1997'], header=0,)
pd.set_option('display.max_columns', None)
CstLine9697.head()
print(CstLine9697)

CstLine9697["dist_1996-dist_1997"] =  CstLine9697['dist_1996'] - CstLine9697['dist_1997']
print(CstLine9697)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine9697Plot = CstLine9697.loc[FIRST:LAST, 'dist_1996-dist_1997'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine9697Plot)

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

col.set_array(CstLine9697Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_9697.png')
fig.savefig('_CoastalStripes_9697.svg')


#11. working with new file to plot the yearly erosion or regression between 1997 and 1998 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine9798 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,17, 18), names=['y_coord', 'dist_1997', 'dist_1998'], header=0,)
pd.set_option('display.max_columns', None)
CstLine9798.head()
print(CstLine9798)

CstLine9798["dist_1997-dist_1998"] =  CstLine9798['dist_1997'] - CstLine9798['dist_1998']
print(CstLine9798)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine9798Plot = CstLine9798.loc[FIRST:LAST, 'dist_1997-dist_1998'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine9798Plot)

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

col.set_array(CstLine9798Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_9798.png')
fig.savefig('_CoastalStripes_9798.svg')


#12. working with new file to plot the yearly erosion or regression between 1998 and 1999 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine9899 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,18, 19), names=['y_coord', 'dist_1998', 'dist_1999'], header=0,)
pd.set_option('display.max_columns', None)
CstLine9899.head()
print(CstLine9899)

CstLine9899["dist_1998-dist_1999"] =  CstLine9899['dist_1998'] - CstLine9899['dist_1999']
print(CstLine9899)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine9899Plot = CstLine9899.loc[FIRST:LAST, 'dist_1998-dist_1999'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine9899Plot)

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

col.set_array(CstLine9899Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_9899.png')
fig.savefig('_CoastalStripes_9899.svg')


#13. working with new file to plot the yearly erosion or regression between 1999 and 2000 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine9900 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,19, 20), names=['y_coord', 'dist_1999', 'dist_2000'], header=0,)
pd.set_option('display.max_columns', None)
CstLine9900.head()
print(CstLine9900)

CstLine9900["dist_1999-dist_2000"] =  CstLine9900['dist_1999'] - CstLine9900['dist_2000']
print(CstLine9900)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine9900Plot = CstLine9900.loc[FIRST:LAST, 'dist_1999-dist_2000'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine9900Plot)

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

col.set_array(CstLine9900Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_9900.png')
fig.savefig('_CoastalStripes_9900.svg')


#14. working with new file to plot the yearly erosion or regression between 2000 and 2001 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine0001 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,20, 21), names=['y_coord', 'dist_2000', 'dist_2001'], header=0,)
pd.set_option('display.max_columns', None)
CstLine0001.head()
print(CstLine0001)

CstLine0001["dist_2000-dist_2001"] =  CstLine0001['dist_2000'] - CstLine0001['dist_2001']
print(CstLine0001)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine0001Plot = CstLine0001.loc[FIRST:LAST, 'dist_2000-dist_2001'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine0001Plot)

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

col.set_array(CstLine0001Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_0001.png')
fig.savefig('_CoastalStripes_0001.svg')


#15. working with new file to plot the yearly erosion or regression between 2001 and 2002 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine0102 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,21, 22), names=['y_coord', 'dist_2001', 'dist_2002'], header=0,)
pd.set_option('display.max_columns', None)
CstLine0102.head()
print(CstLine0102)

CstLine0102["dist_2001-dist_2002"] =  CstLine0102['dist_2001'] - CstLine0102['dist_2002']
print(CstLine0102)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine0102Plot = CstLine0102.loc[FIRST:LAST, 'dist_2001-dist_2002'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine0102Plot)

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

col.set_array(CstLine0102Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_0102.png')
fig.savefig('_CoastalStripes_0102.svg')


#16. working with new file to plot the yearly erosion or regression between 2002 and 2003 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine0203 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,22, 23), names=['y_coord', 'dist_2002', 'dist_2003'], header=0,)
pd.set_option('display.max_columns', None)
CstLine0203.head()
print(CstLine0203)

CstLine0203["dist_2002-dist_2003"] =  CstLine0203['dist_2002'] - CstLine0203['dist_2003']
print(CstLine0203)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine0203Plot = CstLine0203.loc[FIRST:LAST, 'dist_2002-dist_2003'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine0203Plot)

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

col.set_array(CstLine0203Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_0203.png')
fig.savefig('_CoastalStripes_0203.svg')


#17. working with new file to plot the yearly erosion or regression between 2003 and 2004 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine0304 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,23, 24), names=['y_coord', 'dist_2003', 'dist_2004'], header=0,)
pd.set_option('display.max_columns', None)
CstLine0304.head()
print(CstLine0304)

CstLine0304["dist_2003-dist_2004"] =  CstLine0304['dist_2003'] - CstLine0304['dist_2004']
print(CstLine0203)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine0304Plot = CstLine0304.loc[FIRST:LAST, 'dist_2003-dist_2004'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine0304Plot)

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

col.set_array(CstLine0304Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_0304.png')
fig.savefig('_CoastalStripes_0304.svg')


#18. working with new file to plot the yearly erosion or regression between 2004 and 2005 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine0405 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,24, 25), names=['y_coord', 'dist_2004', 'dist_2005'], header=0,)
pd.set_option('display.max_columns', None)
CstLine0405.head()
print(CstLine0405)

CstLine0405["dist_2004-dist_2005"] =  CstLine0405['dist_2004'] - CstLine0405['dist_2005']
print(CstLine0405)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine0405Plot = CstLine0405.loc[FIRST:LAST, 'dist_2004-dist_2005'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine0405Plot)

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

col.set_array(CstLine0405Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_0405.png')
fig.savefig('_CoastalStripes_0405.svg')


#19. working with new file to plot the yearly erosion or regression between 2005 and 2006 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine0506 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,25, 26), names=['y_coord', 'dist_2005', 'dist_2006'], header=0,)
pd.set_option('display.max_columns', None)
CstLine0506.head()
print(CstLine0506)

CstLine0506["dist_2005-dist_2006"] =  CstLine0506['dist_2005'] - CstLine0506['dist_2006']
print(CstLine0506)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine0506Plot = CstLine0506.loc[FIRST:LAST, 'dist_2005-dist_2006'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine0506Plot)

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

col.set_array(CstLine0506Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_0506.png')
fig.savefig('_CoastalStripes_0506.svg')


#20. working with new file to plot the yearly erosion or regression between 2006 and 2007 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine0607 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,26, 27), names=['y_coord', 'dist_2006', 'dist_2007'], header=0,)
pd.set_option('display.max_columns', None)
CstLine0607.head()
print(CstLine0607)

CstLine0607["dist_2006-dist_2007"] =  CstLine0607['dist_2006'] - CstLine0607['dist_2007']
print(CstLine0607)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine0607Plot = CstLine0607.loc[FIRST:LAST, 'dist_2006-dist_2007'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine0607Plot)

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

col.set_array(CstLine0607Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_0607.png')
fig.savefig('_CoastalStripes_0607.svg')


#21. working with new file to plot the yearly erosion or regression between 2007 and 2008 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine0708 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,27, 28), names=['y_coord', 'dist_2007', 'dist_2008'], header=0,)
pd.set_option('display.max_columns', None)
CstLine0708.head()
print(CstLine0708)

CstLine0708["dist_2007-dist_2008"] =  CstLine0708['dist_2007'] - CstLine0708['dist_2008']
print(CstLine0708)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine0708Plot = CstLine0708.loc[FIRST:LAST, 'dist_2007-dist_2008'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine0708Plot)

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

col.set_array(CstLine0708Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_0708.png')
fig.savefig('_CoastalStripes_0708.svg')


#22. working with new file to plot the yearly erosion or regression between 2008 and 2009 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine0809 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV.csv', index_col=0, usecols=(0,28, 29), names=['y_coord', 'dist_2008', 'dist_2009'], header=0,)
pd.set_option('display.max_columns', None)
CstLine0809.head()
print(CstLine0809)

CstLine0809["dist_2008-dist_2009"] =  CstLine0809['dist_2008'] - CstLine0809['dist_2009']
print(CstLine0809)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine0809Plot = CstLine0809.loc[FIRST:LAST, 'dist_2008-dist_2009'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine0809Plot)

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

col.set_array(CstLine0809Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_0809.png')
fig.savefig('_CoastalStripes_0809.svg')


#23. working with new file to plot the yearly erosion or regression between 2009 and 2010 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine0910 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,29, 30), names=['y_coord', 'dist_2009', 'dist_2010'], header=0,)
pd.set_option('display.max_columns', None)
CstLine0910.head()
print(CstLine0910)

CstLine0910["dist_2009-dist_2010"] =  CstLine0910['dist_2009'] - CstLine0910['dist_2010']
print(CstLine0910)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine0910Plot = CstLine0910.loc[FIRST:LAST, 'dist_2009-dist_2010'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine0910Plot)

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

col.set_array(CstLine0910Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_0910.png')
fig.savefig('_CoastalStripes_0910.svg')


#24. working with new file to plot the yearly erosion or regression between 2010 and 2011 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine1011 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,30, 31), names=['y_coord', 'dist_2010', 'dist_2011'], header=0,)
pd.set_option('display.max_columns', None)
CstLine1011.head()
print(CstLine1011)

CstLine1011["dist_2010-dist_2011"] =  CstLine1011['dist_2010'] - CstLine1011['dist_2011']
print(CstLine1011)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine1011Plot = CstLine1011.loc[FIRST:LAST, 'dist_2010-dist_2011'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine1011Plot)

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

col.set_array(CstLine1011Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_1011.png')
fig.savefig('_CoastalStripes_1011.svg')


#25. working with new file to plot the yearly erosion or regression between 2011 and 2012 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine1112 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,31, 32), names=['y_coord', 'dist_2011', 'dist_2012'], header=0,)
pd.set_option('display.max_columns', None)
CstLine1112.head()
print(CstLine1112)

CstLine1112["dist_2011-dist_2012"] =  CstLine1112['dist_2011'] - CstLine1112['dist_2012']
print(CstLine1112)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine1112Plot = CstLine1112.loc[FIRST:LAST, 'dist_2011-dist_2012'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine1112Plot)

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

col.set_array(CstLine1112Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_1112.png')
fig.savefig('_CoastalStripes_1112.svg')


#26. working with new file to plot the yearly erosion or regression between 2012 and 2013 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine1213 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,32, 33), names=['y_coord', 'dist_2012', 'dist_2013'], header=0,)
pd.set_option('display.max_columns', None)
CstLine1213.head()
print(CstLine1213)

CstLine1213["dist_2012-dist_2013"] =  CstLine1213['dist_2012'] - CstLine1213['dist_2013']
print(CstLine1213)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine1213Plot = CstLine1213.loc[FIRST:LAST, 'dist_2012-dist_2013'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine1213Plot)

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

col.set_array(CstLine1213Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_1213.png')
fig.savefig('_CoastalStripes_1213.svg')


#27. working with new file to plot the yearly erosion or regression between 2013 and 2014 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine1314 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,33, 34), names=['y_coord', 'dist_2013', 'dist_2014'], header=0,)
pd.set_option('display.max_columns', None)
CstLine1314.head()
print(CstLine1314)

CstLine1314["dist_2013-dist_2014"] =  CstLine1314['dist_2013'] - CstLine1314['dist_2014']
print(CstLine1314)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine1314Plot = CstLine1314.loc[FIRST:LAST, 'dist_2013-dist_2014'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine1314Plot)

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

col.set_array(CstLine1314Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_1314.png')
fig.savefig('_CoastalStripes_1314.svg')


#28. working with new file to plot the yearly erosion or regression between 2014 and 2015 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine1415 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,34, 35), names=['y_coord', 'dist_2014', 'dist_2015'], header=0,)
pd.set_option('display.max_columns', None)
CstLine1415.head()
print(CstLine1415)

CstLine1415["dist_2014-dist_2015"] =  CstLine1415['dist_2014'] - CstLine1415['dist_2015']
print(CstLine1415)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine1415Plot = CstLine1415.loc[FIRST:LAST, 'dist_2014-dist_2015'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine1415Plot)

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

col.set_array(CstLine1415Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_1415.png')
fig.savefig('_CoastalStripes_1415.svg')


#29. working with new file to plot the yearly erosion or regression between 2015 and 2016 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine1516 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,35, 36), names=['y_coord', 'dist_2015', 'dist_2016'], header=0,)
pd.set_option('display.max_columns', None)
CstLine1516.head()
print(CstLine1516)

CstLine1516["dist_2015-dist_2016"] =  CstLine1516['dist_2015'] - CstLine1516['dist_2016']
print(CstLine1516)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine1516Plot = CstLine1516.loc[FIRST:LAST, 'dist_2015-dist_2016'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine1516Plot)

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

col.set_array(CstLine1516Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_1516.png')
fig.savefig('_CoastalStripes_1516.svg')


#30. working with new file to plot the yearly erosion or regression between 2016 and 2017 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine1617 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,36, 37), names=['y_coord', 'dist_2016', 'dist_2017'], header=0,)
pd.set_option('display.max_columns', None)
CstLine1617.head()
print(CstLine1617)

CstLine1617["dist_2016-dist_2017"] =  CstLine1617['dist_2016'] - CstLine1617['dist_2017']
print(CstLine1617)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine1617Plot = CstLine1617.loc[FIRST:LAST, 'dist_2016-dist_2017'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine1617Plot)

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

col.set_array(CstLine1617Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_1617.png')
fig.savefig('_CoastalStripes_1617.svg')


#31. working with new file to plot the yearly erosion or regression between 2017 and 2018 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine1718 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,37, 38), names=['y_coord', 'dist_2017', 'dist_2018'], header=0,)
pd.set_option('display.max_columns', None)
CstLine1718.head()
print(CstLine1718)

CstLine1718["dist_2017-dist_2018"] =  CstLine1718['dist_2017'] - CstLine1718['dist_2018']
print(CstLine1718)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine1718Plot = CstLine1718.loc[FIRST:LAST, 'dist_2017-dist_2018'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine1718Plot)

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

col.set_array(CstLine1718Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_1718.png')
fig.savefig('_CoastalStripes_1718.svg')


#32. working with new file to plot the yearly erosion or regression between 2018 and 2019 --> amount of erosion = positive value; Progradation = negative erosion value
CstLine1819 = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0,38, 39), names=['y_coord', 'dist_2018', 'dist_2019'], header=0,)
pd.set_option('display.max_columns', None)
CstLine1819.head()
print(CstLine1819)

CstLine1819["dist_2018-dist_2019"] =  CstLine1819['dist_2018'] - CstLine1819['dist_2019']
print(CstLine1819)



FIRST = 1
LAST = 4590

reference=0
LIM = 20 # meters


CstLine1819Plot = CstLine1819.loc[FIRST:LAST, 'dist_2018-dist_2019'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()
print(CstLine1819Plot)

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

col.set_array(CstLine1819Plot)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripes_1819.png')
fig.savefig('_CoastalStripes_1819.svg')