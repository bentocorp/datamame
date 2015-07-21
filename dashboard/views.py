from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

import io
from xlsxwriter.workbook import Workbook
import xlrd
import xlwt
from Dashboard import Dashboard
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    """docstring for index"""
    return render(request, 'register.html', {'title': 'test page'})

def upload(request):
    if request.method == 'POST':
        onFleet = request.FILES['onfleet']
        stripe = request.FILES['stripe']
        download = request.POST['download']
        catering = request.POST['catering']
        cateringRevenue = request.POST['cateringRevenue']
        dashboard = Dashboard().dashboard(onFleet,stripe,download,catering,cateringRevenue)

        output = io.BytesIO()
        workbook = Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()
        worksheet = writeExcel(worksheet,dashboard)
            
        workbook.close()
        output.seek(0)
        response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = "attachment; filename=result.xlsx"
    return response
    #return render_to_response('upload.html', {'a':new},content_type='xls')

def writeExcel(worksheet,dashboard):
    for i in range(0,len(dashboard)):
        for j in range(0,len(dashboard[i])):
            temp = dashboard[i]
            if len(temp) !=0:
                worksheet.write(len(temp)-j+1, i, temp[len(temp)-j-1])
    return(worksheet)

##    
##def handle_uploaded_file(g,h):
##    g = xlrd.open_workbook(file_contents=g.read())
##    h =  xlrd.open_workbook(file_contents=h.read())
##    a = h.sheet_by_name("nps.csv")
##    a = a.cell_value(1,4)
##    return a
