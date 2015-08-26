from Dashboard import Dashboard
from BaseFunction import BaseFunction
import datetime
import xlrd
from bokeh.charts import Bar, output_file, show
from bokeh.io import output_file, show, vplot
import sys

excel = xlrd.open_workbook("orders_raw.xlsx")
excel = excel.sheet_by_name("orders_raw.csv")
ordersRaw = []
for i in range (1,excel.nrows):
    temp = []
    for j in range(0,13): # need to be auto-calculate
        temp.append(excel.cell_value(i,j))
    ordersRaw.append(temp)

######################################################
orderDict = {}
for i in range(0,len(ordersRaw)):
    temp = ordersRaw[i][1]
    if not temp in orderDict:
        orderDict[temp] = 1
    else:
        orderDict[temp] = orderDict[temp] + 1

myDict = {}
keys = list(orderDict.keys())
for i in range(0,len(keys)):
    temp = orderDict[keys[i]]
    if not temp in myDict:
        myDict[temp] = 1
    else:
        myDict[temp] = myDict[temp] + 1

temp = []
name = []
keys = list(myDict.keys())
for i in range(0,len(keys)):
    temp.append(float("{0:.4f}".format(myDict[keys[i]]/float(39.87))))
    name.append(str(keys[i]))

# prepare some data
data = {"y": temp}

# output to static HTML file
output_file("bar.html")

# create a new line chat with a title and axis labels
p1 = Bar(data, cat=name, title="Bar example",
        xlabel='# orders per user', ylabel='# of people', width=1000, height=400)
######################################################
moneyDict = {}
for i in range(0,len(ordersRaw)):
    temp = ordersRaw[i][1]
    if not temp in moneyDict:
        date = datetime.datetime.today()-datetime.datetime.utcfromtimestamp((ordersRaw[i][4] - 25569) * 86400.0)
        moneyDict[temp] = [date.days,ordersRaw[i][12]]
    else:
        moneyDict[temp][1] = moneyDict[temp][1] + ordersRaw[i][12]

moneyDateDict = {}
keys = list(moneyDict.keys())
for i in range(0,len(keys)):
    temp = moneyDict[keys[i]][0]
    if not temp in moneyDateDict:
        moneyDateDict[temp] = [moneyDict[keys[i]][1],1]
    else:
        moneyDateDict[temp][0] = moneyDateDict[temp][0] + moneyDict[keys[i]][1]
        moneyDateDict[temp][1] = moneyDateDict[temp][1] + 1

temp = []
name = []
keys = list(moneyDateDict.keys())
for i in range(0,len(keys)):
    temp.append(moneyDateDict[keys[i]][0]/moneyDateDict[keys[i]][1])
    name.append(str(keys[i]))

# prepare some data
data2 = {"y": temp}

# create a new line chat with a title and axis labels
p2 = Bar(data2, cat=name, title="Average money spend",
        xlabel='# of day from today', ylabel='# of money', width=1000, height=500)

######################################################
##weekPivot = Dashboard().readWeekPivot()
for i in range(0,len(ordersRaw)):
    ordersRaw[i].append(datetime.datetime.utcfromtimestamp((ordersRaw[i][4] - 25569.1) * 86400.0))
##ordersDict = BaseFunction().getDict(ordersRaw,weekPivot,13)
##tempDict = {}
##keys = BaseFunction().sortKey(ordersDict)
##for i in range(0,len(keys)):
##    for j in range(0,len(ordersDict[keys[i])):
##        if not keys[i] in tempDict:
##            tempDict[i] = []
##        else:
##            tempDict[temp] = tempDict[temp] + 1
######################################################
freqDict = {}
for i in range(0,len(ordersRaw)):
    temp = ordersRaw[i][1]
    if not temp in freqDict:
        freqDict[temp] = [ordersRaw[i][13]]
    else:
        freqDict[temp].append(ordersRaw[i][13])
        
diff12 = {}
diff23 = {}
diff34 = {}
diff45 = {}
diff56 = {}
keys = list(freqDict.keys())
for i in range(0,len(keys)):
    #between 1 and 2
    if len(freqDict[keys[i]]) > 1:
        temp = (freqDict[keys[i]][1]-freqDict[keys[i]][0]+datetime.timedelta(0,18000)).days
        if not temp in diff12:
            diff12[temp] = 1
        else:
            diff12[temp] = diff12[temp]+1
    # between 2 and 3
    if len(freqDict[keys[i]]) > 2:
        temp = (freqDict[keys[i]][2]-freqDict[keys[i]][1]+datetime.timedelta(0,18000)).days
        if not temp in diff23:
            diff23[temp] = 1
        else:
            diff23[temp] = diff23[temp]+1
    #between 3 and 4
    if len(freqDict[keys[i]]) > 3:
        temp = (freqDict[keys[i]][3]-freqDict[keys[i]][2]+datetime.timedelta(0,18000)).days
        if not temp in diff34:
            diff34[temp] = 1
        else:
            diff34[temp] = diff34[temp]+1
    #between 4 and 5
    if len(freqDict[keys[i]]) > 4:
        temp = (freqDict[keys[i]][4]-freqDict[keys[i]][3]+datetime.timedelta(0,18000)).days
        if not temp in diff45:
            diff45[temp] = 1
        else:
            diff45[temp] = diff45[temp]+1
    #between 5 and 6
    if len(freqDict[keys[i]]) > 5:
        temp = (freqDict[keys[i]][5]-freqDict[keys[i]][4]+datetime.timedelta(0,18000)).days
        if not temp in diff56:
            diff56[temp] = 1
        else:
            diff56[temp] = diff56[temp]+1

#diff12 graph
temp = []
name = []
keys = list(diff12.keys())
for i in range(0,len(keys)):
    temp.append(diff12[keys[i]])
    name.append(str(keys[i]))
    
data3 = {"y": temp}

p3 = Bar(data3, cat=name, title="Order frequency between first and second order",
        xlabel='# of day between 1 and 2 orders', ylabel='# of order', width=1000, height=500)

#diff23 graph
temp = []
name = []
keys = list(diff23.keys())
for i in range(0,len(keys)):
    temp.append(diff23[keys[i]])
    name.append(str(keys[i]))

data4 = {"y": temp}

p4 = Bar(data4, cat=name, title="Order frequency between second and third order",
        xlabel='# of day between 2 and 3 orders', ylabel='# of order', width=1000, height=500)

#diff34 graph
temp = []
name = []
keys = list(diff34.keys())
for i in range(0,len(keys)):
    temp.append(diff34[keys[i]])
    name.append(str(keys[i]))

data5 = {"y": temp}

p5 = Bar(data5, cat=name, title="Order frequency between third and forth order",
        xlabel='# of day between 3 and 4 orders', ylabel='# of order', width=1000, height=500)

#diff45 graph
temp = []
name = []
keys = list(diff45.keys())
for i in range(0,len(keys)):
    temp.append(diff45[keys[i]])
    name.append(str(keys[i]))

data6 = {"y": temp}

p6 = Bar(data6, cat=name, title="Order frequency between forth and fifth order",
        xlabel='# of day between 4 and 5 orders', ylabel='# of order', width=1000, height=500)

#diff56 graph
temp = []
name = []
keys = list(diff56.keys())
for i in range(0,len(keys)):
    temp.append(diff56[keys[i]])
    name.append(str(keys[i]))

data7 = {"y": temp}

p7 = Bar(data7, cat=name, title="Order frequency between fifth and sixth order",
        xlabel='# of day between 5 and 6 orders', ylabel='# of order', width=1000, height=500)


plot = vplot(p1,p2,p3,p4,p5,p6,p7)
show(plot)

def makeDiffGraph(dictionary,num1,num2):
    temp = []
    name = []
    keys = list(dictionary.keys())
    for i in range(0,len(keys)):
        temp.append(dictionary[keys[i]])
        name.append(str(keys[i]))

    data7 = {"y": temp}

    p7 = Bar(data7, cat=name, title="Order frequency between fifth and sixth order",
            xlabel='# of day between 5 and 6 orders', ylabel='# of order', width=1000, height=500)




