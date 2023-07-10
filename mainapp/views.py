from django.shortcuts import render

# Create your views here.
def stockPicker(request):
    return render(request,'mainapp/stocktracker.html')