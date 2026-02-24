import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m,precipitation,windspeed_10m",
    "forecast_days": 7
}

response = requests.get(url, params=params)
data = response.json()
print(data)