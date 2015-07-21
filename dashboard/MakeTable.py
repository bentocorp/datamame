from BaseFunction import BaseFunction
from BaseStat import BaseStat

class MakeTable:
#make each column of table and put into one [[]]
#the order is by excel
    def makeTable(self,orderDetailsRaw,ordersRaw,onFleetRaw,stripeRaw,NPSRaw,weekPivot,d,c,cr):
        #independent data!! write into database future
        download = [0,0,758,467,449,392,700,690,642,634,562,567,561,539,839,532,828,740,468,537,float(d)]
        bentoCatering = [0,0,0,0,11,0,11,30,30,30,30,30,85,38,27,137,35,82,42,30,float(c)]
        menu = []
        #pull from code
        myDict = BaseFunction().getDict(ordersRaw,weekPivot,4)
        allKey = BaseFunction().sortKey(myDict) #get all Key first column
        temp = BaseStat().getBentoNum(orderDetailsRaw,ordersRaw,weekPivot)
        bentoLunch = temp[0] #bento_lunch
        bentoDinner = temp[1] # bento_dinner
        ordersNum = BaseStat().getOrdersNum(ordersRaw,weekPivot) #orders
        newCostumerNum = BaseStat().getUniqueCostumerNum(ordersRaw,weekPivot) #unique cost
        temp = BaseStat().getDaysRepaet(ordersRaw,weekPivot)
        fourDaysRepaet = temp[0] #14day repeat
        eightDaysRepeat = temp[1] #28day repeat
        meanDeliveryTime = BaseStat().getMeanDeliveryTime(onFleetRaw,weekPivot) #delivery time
        temp = BaseStat().getStripe(stripeRaw,weekPivot)
        stripeGross = temp[0] #stripe gross
        stripeGross[len(stripeGross)-1] = stripeGross[len(stripeGross)-1] + float(cr) #add manual chagne future!
        stripeRefund = temp[1] #stripe refund
        temp = BaseStat().getNPS(NPSRaw,ordersRaw,weekPivot)
        NPSLunch = temp[0] #nps lunch
        NPSDinner = temp[1] #nps dinner
        NPSTotal = temp[2] #nps total

        #calculation
        bentoTotal = [0] * len(bentoLunch)
        repeatCostumerNum = [0] * len(newCostumerNum)
        bentoPerOrder = [0] * len(ordersNum)
        stripeNet = [0] * len(stripeGross)
        AverageOrderValue = [0] * len(ordersNum)
        for i in range(0,len(bentoLunch)):
            bentoTotal[i] = bentoLunch[i] + bentoDinner[i] + bentoCatering[i] #bento total
            repeatCostumerNum[i] = ordersNum[i] - newCostumerNum[i]  #repeat customers
            bentoPerOrder[i] = ordersNum[i]/bentoTotal[i] #bento per order
            stripeNet[i] = stripeGross[i] - stripeRefund[i] #stripe net
            AverageOrderValue[i] = stripeNet[i]/ordersNum[i] #average order
            
        #increasing rate past
        bentoLunchRate = BaseStat().getIncreasingRate(bentoLunch) #lunch rate
        bentoDinnerRate = BaseStat().getIncreasingRate(bentoDinner) #dinner rate
        bentoCateringRate = BaseStat().getIncreasingRate(bentoCatering) #catering rate
        bentoTotalRate = BaseStat().getIncreasingRate(bentoTotal) #total rate
        stripeRate = BaseStat().getIncreasingRate(stripeNet) #stripe rate

        #Make a list
        return (allKey,menu,NPSLunch,NPSDinner,NPSTotal,meanDeliveryTime,download,ordersNum,
                    bentoLunch,bentoLunchRate,bentoDinner,bentoDinnerRate,bentoCatering,
                    bentoCateringRate,bentoTotal,bentoTotalRate,newCostumerNum,repeatCostumerNum,
                    fourDaysRepaet,eightDaysRepeat,bentoPerOrder,stripeGross,stripeRefund,stripeNet,
                    stripeRate,AverageOrderValue)

    
    
    
    
