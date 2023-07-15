from django.shortcuts import render
from yahoo_fin.stock_info import *

# Create your views here.
def stockPicker(request):
    stock_picker = tickers_nifty50()
    print(stock_picker)

    #Context The Data
    context = {'stockpicker':stock_picker}
    return render(request,'mainapp/stockpicker.html',context)

def stockTracker(request):
    return render(request,'mainapp/stocktracker.html')