#draw the heatmap on GOOGLE Map
import gmplot
import xlrd
import os
from BaseFunction import BaseFunction
import HeatMap
import datetime

class HeatMapGPS:
    def readExcel(self):
        #read excel
        excel = xlrd.open_workbook("/Users/chongzhou/Documents/bentonow/dashboard/mysite/dashboard/OnFleet_raw.xlsx").sheet_by_name("OnFleet Raw")
        onFleetRaw = []
        for i in range (1,excel.nrows):
            temp = []
            for j in range(0,24): # need to be auto-calculate
                temp.append(excel.cell_value(i,j))
            onFleetRaw.append(temp)
        return(onFleetRaw)

    def drawMap(self):
        #onFleetRaw = onFleetRaw[4727:]
        onFleetRaw = self.readExcel()
        for i in range(0,len(onFleetRaw)):
            onFleetRaw[i].append(datetime.datetime.utcfromtimestamp((onFleetRaw[i][10] - 25569) * 86400.0))
        myDict = HeatMap.createDictByHour(onFleetRaw,24)
        key = HeatMap.timeDiff(datetime.datetime.now())
        location=[]
        if (key >= 0) & (key <=17):
            location = BaseFunction().getColumn(myDict[key],6)
        lats = []
        lngs = []
        for i in range(0,len(location)):
            com = location[i].index(",")
            temp = float(location[i][(com+1):])
            lats.append(float("{0:.6f}".format(temp)))
            temp = float(location[i][0:com])
            lngs.append(float("{0:.6f}".format(temp)))
            
        #draw map
        gmap = gmplot.GoogleMapPlotter(37.778, -122.412, 16)
        gmap.heatmap(lats, lngs,radius=25,opacity=0.8)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        gmap.draw(os.path.join(BASE_DIR, 'templates/mymap.html'))
