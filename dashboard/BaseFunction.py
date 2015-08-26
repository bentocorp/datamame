#Basic function for all excels futural analysis
import datetime

class BaseFunction:
    
    #return whole column you need
    #data is a matrix
    def getColumn(self,data,colNum):
        date = []
        for i in range(0,len(data)):
            date.append(data[i][colNum])
        return(date)

    #return week
    #data and weekPivot is matrics
    def getWeek(self,data,weekPivot,colNum):
        week = []
        week.append(datetime.datetime(data[0][colNum].year,data[0][colNum].month,data[0][colNum].day))
        for i in range(1,len(data)):
            temp = data[i][colNum]
            last = data[i-1][colNum]
            #if the order is same as last one, write last one
            if (temp.month == last.month) & (temp.day == last.day) & (temp.year == last.year):
                week.append(week[i-1])
            else:
                #go over week pivot excel to find one
                for j in range(0,len(weekPivot)):
                    last = weekPivot[j][0]
                    if (temp.month == last.month) & (temp.day == last.day) & (temp.year == last.year):
                        last = weekPivot[j][1]
                        week.append(datetime.datetime(last.year,last.month,last.day))
        return(week)

    #return meal
    def getMeal(self,data):
        meal = []
        for i in range(0,len(data)):
            if data[i].hour < 15:
                meal.append("lunch")
            else:
                meal.append("dinner")
        return(meal)

    #return status for orderDetailRaw only
    def getStatus(self,data,dataO):
        status = []
        index = self.getColumn(dataO,0)
        statusO = self.getColumn(dataO,9)
        for i in range(0,len(data)):
            temp = index.index(data[i][1])
            status.append(statusO[temp])
        return(status)
    
    #make a dictionary, key is unique week, set is data
    #To do: need to be optimize the algorithm
    def getDict(self,data,weekPivot,colNum):
        myDict = {}
        temp = datetime.datetime(data[0][colNum].year,data[0][colNum].month,data[0][colNum].day)
        myDict[temp] = [data[0]]
        for i in range(1,len(data)):
            temp = datetime.datetime(data[i][colNum].year,data[i][colNum].month,data[i][colNum].day)
            for j in range(0,len(weekPivot)):
                last = weekPivot[j][0]
                if (temp.month == last.month) & (temp.day == last.day) & (temp.year == last.year):
                    last = weekPivot[j][1]
                    last = datetime.datetime(last.year,last.month,last.day)
                    #if no key, create.
                    if not last in myDict:
                        myDict[last] = [data[i]]
                    else:
                        myDict[last].append(data[i])
                    break
        return(myDict)

    #sort key in dict
    def sortKey(self,myDict):
        allKey = []
        for key in myDict:
            allKey.append(key)
        allKey = sorted(allKey)
        return (allKey)

    #get NPS score
    def getScore(self,score):
        if score > 8:
            return (1)
        elif score < 7:
            return (-1)
        else:
            return 0

    def getDictByDay(self,data,weekPivot,colNum):
        myDict = {}
        temp = datetime.datetime(data[0][colNum].year,data[0][colNum].month,data[0][colNum].day)
        myDict[temp] = [data[0]]
        for i in range(1,len(data)):
            temp = datetime.datetime(data[i][colNum].year,data[i][colNum].month,data[i][colNum].day)
            for j in range(0,len(weekPivot)):
                last = weekPivot[j][0]
                if (temp.month == last.month) & (temp.day == last.day) & (temp.year == last.year):
                    #if no key, create.
                    if not last in myDict:
                        myDict[last] = [data[i]]
                    else:
                        myDict[last].append(data[i])
                    break
        return(myDict)

    def getMain(self,data):
        main = []
        for i in range(0,len(data)):
            if  i%5 == 0:
                main.append(data[i])
        return(main)
    
    def getSide(self,data):
        side = []
        for i in range(0,len(data)):
            if  i%5 != 0:
                side.append(data[i])
        return(side)

    #find 4 of 6 best
    def getBestSide(self,ID,count):
        best = []
        for i in range(0,4):
            best.append(ID[count.index(max(count))])
            ID.remove(ID[count.index(max(count))])
            count.remove(max(count))
        return(best)
    
            
            
                                        
                                             
                                             


    
