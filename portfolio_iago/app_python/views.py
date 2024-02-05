
from django.shortcuts import render
from django.shortcuts import redirect

# conexoes com diretorios
def portfolio(request):
    return render(request,'home/index.html')
def jogo_da_velha(request):
    return render(request,'python/jogo_da_velha.html')
def calculadora_imc(request):
    return render(request,'python/calculadora_imc.html')
def jogo_de_advinhar(request):
    return render(request,'python/jogo_de_advinhar.html')

# transacao de diretorios
def help_python(request):
    tratativa_dados = request.POST.get('texto_codigo') 
    if tratativa_dados == '.help':
        return render(request, 'python/help_python.html')
    elif tratativa_dados == '.cd jogo_da_velha':
        return render(request,'python/jogo_da_velha.html')
    elif tratativa_dados == '.cd calculadora_imc':
        return render(request,'python/calculadora_imc.html')
    elif tratativa_dados == '.cd jogo_de_advinhar':
        return render(request,'python/jogo_de_advinhar.html')
    elif tratativa_dados == '.linkedin':
        return redirect('https://www.linkedin.com/in/iagolongen/')
    elif tratativa_dados == '.wpp':
        return redirect('https://wa.me/5547988071571')
    elif tratativa_dados == '.github':
        return redirect('https://github.com/devlongen')
    else:
        return render(request,'home/index.html')

"""    
import requests
from js_diferente import diferente
url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/metric"
querystring = {pesoUsuario,alturaUsuario}

headers = {
	"X-RapidAPI-Key": "f5d22b74a5msh72e7f64685d971cp1c73d5jsn48e98adb797f",
	"X-RapidAPI-Host": "body-mass-index-bmi-calculator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
"""
