#draw heat map
import MySQLdb
import datetime
from Dashboard import Dashboard
from BaseFunction import BaseFunction
from bokeh.charts import HeatMap, output_file, show
from bokeh.palettes import RdYlGn6
import pandas as pd

## calculate the 30 mins difference
def timeDiff(time):
    if time.hour == 10:
        return 0
    elif (time.hour == 11) & (time.minute < 30):
        return 1
    elif (time.hour == 11) & (time.minute >= 30):
        return 2
    elif (time.hour == 12) & (time.minute < 30):
        return 3
    elif (time.hour == 12) & (time.minute >= 30):
        return 4
    elif (time.hour == 13) & (time.minute < 30):
        return 5
    elif (time.hour == 13) & (time.minute >= 30):
        return 6
    elif time.hour == 16:
        return 7
    elif (time.hour == 17) & (time.minute < 30):
        return 8
    elif (time.hour == 17) & (time.minute >= 30):
        return 9
    elif (time.hour == 18) & (time.minute < 30):
        return 10
    elif (time.hour == 18) & (time.minute >= 30):
        return 11
    elif (time.hour == 19) & (time.minute < 30):
        return 12
    elif (time.hour == 19) & (time.minute >= 30):
        return 13
    elif (time.hour == 20) & (time.minute < 30):
        return 14
    elif (time.hour == 20) & (time.minute >= 30):
        return 15
    elif (time.hour == 21) & (time.minute < 30):
        return 16
    elif (time.hour == 21) & (time.minute >= 30):
        return 17
    
#create a dictionary
#key is the 30 mins time period. value is the ordersRaw whole data
def createDictByHour(ordersRaw,column):
    myDict = {}
    timeColumn = BaseFunction().getColumn(ordersRaw,column)
    for i in range(0,len(ordersRaw)):
        temp = timeDiff(timeColumn[i])
        if not temp in myDict:
            myDict[temp] = [ordersRaw[i]]
        else:
            myDict[temp].append(ordersRaw[i])
    return(myDict)

##ordersRaw = Dashboard().readOrdersRaw()
##ordersRaw = ordersRaw[4189:]
##myDict = createDictByHour(ordersRaw,4)
##del myDict[None]
##allKey = BaseFunction().sortKey(myDict)
##zipcode = BaseFunction().getColumn(ordersRaw,8)
##uniqueZip = list(set(zipcode))
##
##heatmap = {}
##for i in range(0,len(allKey)):
##    zipTime = [0] *len(uniqueZip)
##    for j in range(0,len(myDict[allKey[i]])):
##        temp = myDict[allKey[i]][j]
##        zipTime[uniqueZip.index(temp[8])] = zipTime[uniqueZip.index(temp[8])] +1
##    heatmap[allKey[i]] = zipTime
##
##for i in range(0,len(allKey)):
##    for j in range(0,len(heatmap[allKey[i]])):
##        heatmap[allKey[i]][j] = float("{0:.2f}".format(heatmap[allKey[i]][j]*100/sum(heatmap[allKey[i]])))
##    
##output_file('DinnerHeatmap.html')
##df = pd.DataFrame(
##        dict(
##            A16 = heatmap[7],
##            A17 = heatmap[8],
##            A1730 = heatmap[9],
##            A18 = heatmap[10],
##            A1830 = heatmap[11],
##            A19 = heatmap[12],
##            A1930 = heatmap[13],
##            A20 = heatmap[14],
##            A2030 = heatmap[15],
##            A21 = heatmap[16],
##            A2130 = heatmap[17]
##        ),
##        index=uniqueZip
##    )
##p = HeatMap(df,title='dinner heatmap',palette=RdYlGn6)
##show(p)
##
##output_file('LunchHeatmap.html')
##df = pd.DataFrame(
##        dict(
##            A10 = heatmap[0],
##            A11 = heatmap[1],
##            A1130 = heatmap[2],
##            A12 = heatmap[3],
##            A1230 = heatmap[4],
##            A13 = heatmap[5],
##            A1330 = heatmap[6],
##        ),
##        index=uniqueZip
##    )
##p = HeatMap(df,title='lunch heatmap',palette=RdYlGn6)
##show(p)





