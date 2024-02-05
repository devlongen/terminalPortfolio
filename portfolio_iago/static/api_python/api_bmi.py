import requests

url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/metric"

querystring = {"weight":"150","height":"1.83"}

headers = {
	"X-RapidAPI-Key": "f5d22b74a5msh72e7f64685d971cp1c73d5jsn48e98adb797f",
	"X-RapidAPI-Host": "body-mass-index-bmi-calculator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())