#Basic Stat analysis to get column we need output
import datetime
from BaseFunction import BaseFunction

class BaseStat:
    #should be a self save constant number

    #get number of bento lunch/dinner
    def getBentoNum(self,orderDetailsRaw,ordersRaw,weekPivot):
        #Get all key to prepare
        myDict = BaseFunction().getDict(orderDetailsRaw,weekPivot,3)
        allKey = BaseFunction().sortKey(myDict)
        
        #create 2 lists
        bentoLunch = [0] * len(allKey)
        bentoDinner = [0] * len(allKey)
        status = BaseFunction().getStatus(orderDetailsRaw,ordersRaw)
        pkOrder = BaseFunction().getColumn(orderDetailsRaw,1)
        meal = BaseFunction().getMeal(BaseFunction().getColumn(orderDetailsRaw,2))
        #first loop scan different key
        for i in range(0,len(allKey)):
            #second loop scan every value in one key
            for j in range(0,len(myDict[allKey[i]])):
                temp = myDict[allKey[i]][j]
                if status[pkOrder.index(temp[1])] == "Delivered":
                    if meal[pkOrder.index(temp[1])] == "lunch":
                        bentoLunch[i] += 1
                    else:
                        bentoDinner[i] += 1
            bentoLunch[i] = bentoLunch[i]/5
            bentoDinner[i] =bentoDinner[i]/5
        return(bentoLunch,bentoDinner)

    #get number of orders
    def getOrdersNum(self,ordersRaw,weekPivot):
        myDict = BaseFunction().getDict(ordersRaw,weekPivot,4)
        allKey = BaseFunction().sortKey(myDict)
        orders = [0] * len(allKey)
        #first loop scan different key
        for i in range(0,len(allKey)):
            #second loop scan every value in one key
            for j in range(0,len(myDict[allKey[i]])):
                temp = myDict[allKey[i]][j]
                if temp[9] == "Delivered":
                     orders[i] += 1
        return(orders)

    #get unique customers number
    def getUniqueCostumerNum(self,ordersRaw,weekPivot):
        pkOrder = BaseFunction().getColumn(ordersRaw,0)
        uniqueID = []
        myDict = BaseFunction().getDict(ordersRaw,weekPivot,4)
        allKey = BaseFunction().sortKey(myDict)
        uniqueNum = [0] * len(allKey)
        #first loop scan different key
        for i in range(0,len(allKey)):
            #second loop scan every value in one key
            for j in range(0,len(myDict[allKey[i]])):
                temp = myDict[allKey[i]][j]
                if temp[9] == "Delivered":
                     if temp[1] not in set(uniqueID):
                         uniqueNum[i] += 1
                         uniqueID.append(temp[1])
        return(uniqueNum)

    #get 14/28 days repeat prob
    def getDaysRepaet(self,ordersRaw,weekPivot):
        myDict = BaseFunction().getDict(ordersRaw,weekPivot,4)
        allKey = BaseFunction().sortKey(myDict)
        fourDaysRepaet = [0] * len(allKey)
        eightDaysRepaet = [0] * len(allKey)
        #first loop scan different key
        for i in range(2,len(allKey)):
            #create 14 days recode id and get more than 1 number
            temp14 = BaseFunction().getColumn(myDict[allKey[i-1]],1)
            temp14 = temp14 + BaseFunction().getColumn(myDict[allKey[i-2]],1)
            for j in range(0,len(set(temp14))):
                if temp14.count(list(set(temp14))[j]) > 1:
                    fourDaysRepaet[i] += 1
            #create 28 days recode id
            if i > 3:
                temp28 = BaseFunction().getColumn(myDict[allKey[i-1]],1)
                temp28 = temp28 + BaseFunction().getColumn(myDict[allKey[i-2]],1)
                temp28 = temp28 + BaseFunction().getColumn(myDict[allKey[i-3]],1)
                temp28 = temp28 + BaseFunction().getColumn(myDict[allKey[i-4]],1)
                for j in range(0,len(set(temp28))):
                    if temp28.count(list(set(temp28))[j]) > 1:
                        eightDaysRepaet[i] += 1
            fourDaysRepaet[i] = fourDaysRepaet[i]*100/len(set(temp14))
            if i > 3:
                eightDaysRepaet[i] = eightDaysRepaet[i]*100/len(set(temp28))
        return(fourDaysRepaet,eightDaysRepaet)

    #get mean delivery time
    def getMeanDeliveryTime(self,onFleetRaw,weekPivot):
        #change the style of time column
        for i in range(0,len(onFleetRaw)):
            onFleetRaw[i].append(datetime.datetime.utcfromtimestamp((onFleetRaw[i][10] - 25569) * 86400.0))
        myDict = BaseFunction().getDict(onFleetRaw,weekPivot,24)
        allKey = BaseFunction().sortKey(myDict)
        meanDeliveryTime = [0] * len(allKey)
        #first loop scan different key
        for i in range(0,len(allKey)):
            #second loop scan every value in one key
            for j in range(0,len(myDict[allKey[i]])):
                temp = myDict[allKey[i]][j]
                if (temp[10] != '') & (temp[12] != ''): #delete NaN
                    if (temp[12]-temp[10])*86400/60 < 60: #delete crazy number
                        meanDeliveryTime[i] = meanDeliveryTime[i] + (temp[12]-temp[10])*86400/60
            meanDeliveryTime[i] = meanDeliveryTime[i]/len(myDict[allKey[i]])
        return(meanDeliveryTime)

    #get stripe report
    def getStripe(self,stripeRaw,weekPivot):
        for i in range(0,len(stripeRaw)):
            stripeRaw[i].append(datetime.datetime.utcfromtimestamp((stripeRaw[i][2] - 25569) * 86400.0))
        myDict = BaseFunction().getDict(stripeRaw,weekPivot,44)
        allKey = BaseFunction().sortKey(myDict)
        stripeGross = [0] * len(allKey)
        stripeRefund = [0] * len(allKey)
        #first loop scan different key
        for i in range(0,len(allKey)):
        #second loop scan every value in one key
            for j in range(0,len(myDict[allKey[i]])):
                temp = myDict[allKey[i]][j]
                if (temp[12] != "Failed"):
                    stripeGross[i] += temp[3]
                    stripeRefund[i] += temp[4]
        return([stripeGross,stripeRefund])

    #get NPS lunch/dinner/total
    def getNPS(self,NPSRaw,ordersRaw,weekPivot):
        NPSRaw = NPSRaw[260:]
        for  i in range(0,len(NPSRaw)):
            pkOrder = BaseFunction().getColumn(ordersRaw,0)
            NPSRaw[i].append(ordersRaw[pkOrder.index(NPSRaw[i][0])][4])
        myDict = BaseFunction().getDict(NPSRaw,weekPivot,5)
        allKey = BaseFunction().sortKey(myDict)
        NPSLunch = [10] * len(allKey)
        NPSDinner = [10] * len(allKey)
        NPSTotal = [10] * len(allKey)
        #first loop scan different key
        for i in range(0,len(allKey)):
            lunchCount = 0
            dinnerCount = 0
            #second loop scan every value in one key
            for j in range(0,len(myDict[allKey[i]])):
                temp = myDict[allKey[i]][j]
                if temp[4] != None:
                    if temp[5].hour < 15:
                        NPSLunch[i] = NPSLunch[i] + BaseFunction().getScore(temp[4])
                        lunchCount += 1
                    else:
                        NPSDinner[i] = NPSDinner[i] + BaseFunction().getScore(temp[4])
                        dinnerCount += 1
                    NPSTotal[i] = NPSTotal[i] + BaseFunction().getScore(temp[4])
            NPSLunch[i] = (NPSLunch[i]-10)*100/lunchCount
            NPSDinner[i] = (NPSDinner[i]-10)*100/dinnerCount
            NPSTotal[i] = (NPSTotal[i]-10)*100/(lunchCount+dinnerCount)
        return(NPSLunch,NPSDinner,NPSTotal)

    #get increasing rate
    def getIncreasingRate(self,column):
        increasingRate = [0] * len(column)
        for i in range(1,len(column)):
            if column[i-1] != 0:
                increasingRate[i] = column[i]*100/column[i-1]-100
        return increasingRate
        
            








