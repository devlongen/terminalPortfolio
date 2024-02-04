
from django.shortcuts import render
from django.http import HttpResponse

def portfolio(request):
    return render(request,'home/index.html')
def help_python(request):
    tratativa_dados = request.POST.get('texto_codigo') 
    if tratativa_dados == ".help":
        return render(request, 'python/help_python.html')
    else:
        return render(request,'home/index.html')