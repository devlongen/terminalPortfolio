import requests

url = "https://fitness-calculator.p.rapidapi.com/bmi"

querystring = {"age":"25","weight":"65","height":"180"}

headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())