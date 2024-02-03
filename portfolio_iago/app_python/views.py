
from django.shortcuts import render

def portfolio(request):
    return render(request,'home/index.html')
def help_python(request):
    return render(request,'python/help_python.html')
