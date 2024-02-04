
from django.shortcuts import render
from django.shortcuts import redirect

def portfolio(request):
    return render(request,'home/index.html')
def help_python(request):
    tratativa_dados = request.POST.get('texto_codigo') 
    if tratativa_dados == '.help':
        return render(request, 'python/help_python.html')
    elif tratativa_dados == '.linkedin':
        return redirect('https://www.linkedin.com/in/iagolongen/')
    elif tratativa_dados == '.wpp':
        return redirect('https://wa.me/5547988071571')
    else:
        return render(request,'home/index.html')