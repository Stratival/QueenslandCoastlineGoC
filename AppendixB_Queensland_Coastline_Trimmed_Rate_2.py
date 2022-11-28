# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:44:51 2021

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

#2. working with new file to plot the avaerage annual rate of erosion or regression between 1988 and 2019 --> amount of erosion = positive value; Progradation = negative erosion value
CstLineRate = pd.read_csv('Queensland_Coastline_ShortTrimmedCSV_Av4.csv', index_col=0, usecols=(0, 2), names=['y_coord', 'rate_time'], header=0,) #names=['fid', 'NetCstBehav_m']
pd.set_option('display.max_columns', None)
CstLineRate.head()
print(CstLineRate)

NetCstBehavRateA = CstLineRate["rate_time"]
max_value = NetCstBehavRateA.max()
min_value = NetCstBehavRateA.min()

print(max_value)
print(min_value)


FIRST = 1
LAST = 4590  # inclusive

# Reference period for the center of the color scale
#FIRST_REFERENCE = 1971
#LAST_REFERENCE = 2000
reference=0
LIM = 2 # meters


NetCstBehavRate = CstLineRate.loc[FIRST:LAST, 'rate_time'].dropna()
#reference = anomaly.loc[FIRST_REFERENCE:LAST_REFERENCE].mean()

cmap = ListedColormap([
    '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef', '#fcbba1', '#fc9272', '#fb6a4a', '#ef3b2c', '#cb181d',
])

#cmap=ListedColormap(['#4292c6','#ef3b2c',])


fig = plt.figure(figsize=(200, 20))

ax = fig.add_axes([0, 0, 1, 1])
ax.set_axis_off()

# create a collection with a rectangle for each year

col = PatchCollection([Rectangle((y, 0), 1, 1)
    for y in range(FIRST, LAST + 1)])

# set data, colormap and color limits

col.set_array(NetCstBehavRate)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)

ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('_CoastalStripesRateFinal.png')
fig.savefig('_CoastalStripesRateFinal.svg')

#legend
x = np.linspace(0, 16, 16)[None, :]
plt.imshow(x, aspect='auto', cmap=cm.vik) # or any other colourmap
plt.axis('off')
plt.show()