# -*- coding: utf-8 -*-
from django.test import TestCase

import gmplot
import xlrd
import os
from BaseFunction import BaseFunction
import HeatMap
import datetime
from HeatMapGPS import HeatMapGPS

##onFleetRaw = HeatMapGPS().readExcel()
##for i in range(0,len(onFleetRaw)):
##    onFleetRaw[i].append(datetime.datetime.utcfromtimestamp((onFleetRaw[i][10] - 25569) * 86400.0))
##myDict = HeatMap.createDictByHour(onFleetRaw,24)
##location = []
##kk=7
##for i in range (0,len(myDict[kk])):
##    if myDict[kk][i][24].weekday() == 4:
##        location.append(myDict[kk][i][6])
##lats = []
##lngs = []
##for i in range(0,len(location)):
##    com = location[i].index(",")
##    temp = float(location[i][(com+1):])
##    lats.append(float("{0:.6f}".format(temp)))
##    temp = float(location[i][0:com])
##    lngs.append(float("{0:.6f}".format(temp)))
##
###draw map
##gmap = gmplot.GoogleMapPlotter(37.778, -122.412, 16)
##gmap.heatmap(lats, lngs,radius=25,opacity=0.8)
##
##BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
##gmap.draw(os.path.join(BASE_DIR, 'templates/Friday21.html'))
from bokeh.charts import Line, output_file, show

# prepare some data
data = {"a": [1, 2, 3, 4, 5], "b": [2, 3, 4, 5, 6], "c": [6, 7, 1, 3, 5],
        "d": [3, 5, 9, 2, 3], "y": [6, 4, 7, 1, 2], "z": [1, 5, 12, 4, 2]}

# output to static HTML file
output_file("lines.html", title="line plot example")

# create a new line chat with a title and axis labels
p = Line(data, title="simple line example", xlabel='x', ylabel='values', width=400, height=400)

# show the results
show(p)
