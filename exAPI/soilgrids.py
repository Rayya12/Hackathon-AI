import requests

lat, lon = 52.0, 5.0  # your location

url = "https://rest.isric.org/soilgrids/v2.0/properties/query"
params = {
    "lon": lon,
    "lat": lat,
    "property": ["clay", "sand", "silt", "phh2o", "soc", "bdod", "cfvo", "nitrogen"],
    "depth": ["0-5cm", "5-15cm"],
    "value": ["mean", "uncertainty"]
}

response = requests.get(url, params=params)
data = response.json()
print(data)