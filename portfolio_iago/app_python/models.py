from django.db import models

# Create your models here.
import requests
def receber_dados(request):
	peso_usuario = request.POST.get('peso_user')
	altura_usuario = request.POST.get('altura_user')
def calculo_imc(pesoUsuario,alturaUsuario):
	url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/metric"
	querystring = {
    	"weight": pesoUsuario,
    	"height": alturaUsuario
}

	headers = {
	"X-RapidAPI-Key": "f5d22b74a5msh72e7f64685d971cp1c73d5jsn48e98adb797f",
	"X-RapidAPI-Host": "body-mass-index-bmi-calculator.p.rapidapi.com"
}

	response = requests.get(url, headers=headers, params=querystring)
	return response
