import requests
from datetime import datetime, timedelta
import numpy as np

def get_weather_data(lat: float, lon: float):
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(days=30)).strftime("%Y-%m-%d")
    
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "daily": ["temperature_2m_mean", "precipitation_sum"],
        "hourly": ["relative_humidity_2m"],
        "timezone": "auto"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    temperature = data["daily"]["temperature_2m_mean"]   # List[float] 30 nilai
    rainfall = data["daily"]["precipitation_sum"]         # List[float] 30 nilai
    humidity = data["hourly"]["relative_humidity_2m"]     # List[float] 720 nilai
    
    return temperature, humidity, rainfall