from django.shortcuts import render
from nsepython import *

# Create your views here.
def stockPicker(request):
    stock_picker = tickers_nifty50()
    print(stock_picker)

    #Context The Data
    context = {'stockpicker':stock_picker}
    return render(request,'mainapp/stockpicker.html',context)

def stockTracker(request):
    n = NSELive()
    details = n.stock_quote("HDFC")
    
    print(details)

    # Context The Data
    
    return render(request,'mainapp/stocktracker.html')