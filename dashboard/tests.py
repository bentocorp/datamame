from django.test import TestCase

from Dashboard import Dashboard
import xlrd

#Onfleet data
excel = xlrd.open_workbook("OnFleet_raw.xlsx").sheet_by_name("OnFleet Raw")
onFleetRaw = []
for i in range (1,excel.nrows):
    temp = []
    for j in range(0,24): # need to be auto-calculate
        temp.append(excel.cell_value(i,j))
    onFleetRaw.append(temp)

#Stripe part
excel = xlrd.open_workbook("stripe_raw.xlsx").sheet_by_name("Stripe Raw")
stripeRaw = []
for i in range (1,excel.nrows):
    temp = []
    for j in range(0,44): # need to be auto-calculate
        temp.append(excel.cell_value(i,j))
    stripeRaw.append(temp)

a = Dashboard().dashboard(onFleetRaw,stripeRaw,800,80,1000)
