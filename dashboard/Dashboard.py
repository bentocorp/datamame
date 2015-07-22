##The basic data analysing for dashboard

import MySQLdb
import xlrd
import datetime
import xlwt
from BaseFunction import BaseFunction
from BaseStat import BaseStat
from MakeTable import MakeTable
import database

class Dashboard:
    #import  weekPivot
    def readWeekPivot(self):
        excel = xlrd.open_workbook("/Users/chongzhou/Documents/bentonow/dashboard/mysite/dashboard/week_pivot.xlsx").sheet_by_name("Week Pivot")
        weekPivot = []
        for i in range (1,excel.nrows):
            temp = datetime.datetime.utcfromtimestamp((excel.cell_value(i,0) - 25569) * 86400.0)
            temp1 = datetime.datetime.utcfromtimestamp((excel.cell_value(i,1) - 25569) * 86400.0)
            weekPivot.append([temp,temp1])
        return(weekPivot)

    #sql part
    #import orders Raw data from MySql serve
    def readOrdersRaw(self):
        cnx = database.bento
        cursor = cnx.cursor()
        cursor.execute("SELECT o.pk_Order, o.fk_User as 'Customer Id', concat(u.firstname, ' ', "
                                "u.lastname) as 'Customer Name', u.email, o.created_at as order_created_at,"
                        "o.street, o.city, o.state, o.zip, os.`status`, o.tax, o.tip, o.amount as 'Total' "
                                "from `Order` o left join OrderStatus os on (o.pk_Order = os.fk_Order)"
                                "left join User u on (o.fk_User = u.pk_User) ORDER BY order_created_at ASC;")
        ordersRaw=[]
        for row in cursor:
            ordersRaw.append(row)
        cursor.close()
        return(ordersRaw)

    #orderDetailsRaw data
    def readOrderDetailsRaw(self):
        cnx = database.bento
        cursor = cnx.cursor()
        cursor.execute("call bento.Report_OrderDetails();")
        orderDetailsRaw=[]
        for row in cursor:
            orderDetailsRaw.append(row)
        return(orderDetailsRaw)

    #NPS data
    def readNPSRaw(self):
        cnx = database.survey
        cursor = cnx.cursor()
        sql = "SELECT DISTINCT m.order_id, m.created_on, m.email, ms.comment AS meal_comment,ms.rating AS nps FROM dish_survey ds, dish d, meal_survey ms, meal m WHERE ds.meal_id = m.id AND m.id = ms.meal_id AND ds.dish_id = d.id ORDER BY m.created_on;"
        cursor.execute(sql)
        tempNPS = []
        for row in cursor:
            tempNPS.append(row)
        NPSRaw = []
        for i in range (0,len(tempNPS)):
            temp = []
            for j in range(0,5): # need to be auto-calculate
                temp.append(tempNPS[i][j])
            NPSRaw.append(temp)
        return(NPSRaw)

    #onfleet data
    def readOnFleet(self,onfleet):
        excel = xlrd.open_workbook(file_contents=onfleet.read())
        excel = excel.sheet_by_name("OnFleet Raw")
        onFleetRaw = []
        for i in range (1,excel.nrows):
            temp = []
            for j in range(0,24): # need to be auto-calculate
                temp.append(excel.cell_value(i,j))
            onFleetRaw.append(temp)
        return(onFleetRaw)

    #stripe data
    def readStripe(self,stripe):
        excel = xlrd.open_workbook(file_contents=stripe.read())
        excel = excel.sheet_by_name("Stripe Raw")
        stripeRaw = []
        for i in range (1,excel.nrows):
            temp = []
            for j in range(0,44): # need to be auto-calculate
                temp.append(excel.cell_value(i,j))
            stripeRaw.append(temp)
        return(stripeRaw)

    #make dashborad
    #only method can be called by other script in total analysis
    def dashboard(self,onFleetRaw,stripeRaw,download,catering,cateringRevenue):
        weekPivot = self.readWeekPivot()
        orderDetailsRaw = self.readOrderDetailsRaw()
        ordersRaw = self.readOrdersRaw()
        NPSRaw = self.readNPSRaw()
        onFleetRaw = self.readOnFleet(onFleetRaw)
        stripeRaw = self.readStripe(stripeRaw)
        dashboard = MakeTable().makeTable(orderDetailsRaw,ordersRaw,onFleetRaw,stripeRaw,NPSRaw,weekPivot,
                                  download,catering,cateringRevenue)
        return(dashboard)


        










