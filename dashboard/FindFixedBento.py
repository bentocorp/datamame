from Dashboard import Dashboard
from BaseFunction import BaseFunction
import xlsxwriter
import datetime

weekPivot = Dashboard().readWeekPivot()
orderDetailsRaw = Dashboard().readOrderDetailsRaw()
temp = []
for i in range(0,len(orderDetailsRaw)):
    if orderDetailsRaw[i][2].hour > 16:
        temp.append(orderDetailsRaw[i])
orderDetailsRaw = temp
myDict = BaseFunction().getDictByDay(orderDetailsRaw,weekPivot,3)
key = BaseFunction().sortKey(myDict)

best = []
for i in range(0,len(key)):
    dishID = BaseFunction().getColumn(myDict[key[i]],7)
    if len(dishID) > 50:
        bestCount = 0
        for j in range(0,len(dishID)/5):
            count = 0
            temp = dishID[(j*5):((j+1)*5)]
            for k in range(0,len(dishID)/5):
                if set(dishID[(k*5):((k+1)*5)]) == set(temp):
                    count = count+1
            if bestCount < count:
                record = temp
                bestCount = count
        best = best + record
        best = best + ["{0:.4f}".format(bestCount/float(len(dishID)/5))]

import csv

ofile  = open('ttest.csv', "wb")
writer = csv.writer(ofile)

for i in range(0,len(best)/6):
    temp = best[(i*6):((i+1)*6)]
    writer.writerow(temp)

ofile.close()
