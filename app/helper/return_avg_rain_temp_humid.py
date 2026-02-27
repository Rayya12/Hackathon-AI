from app.schema.inputSchema import InputData
import numpy as np

def return_avg_rain_temp_and_humid(inputData: InputData):
    
    if (not inputData.wather):
        return {
            "temperature": 25.0,
            "humidity": 71.0,
            "rainfall": 103.0
        }
        
    data = inputData.wather
    
    temperature = np.mean(data["daily"]["temperature_2m_mean"])   # List[float] 30 nilai
    rainfall = np.mean(data["daily"]["precipitation_sum"])         # List[float] 30 nilai
    humidity = np.mean(data["hourly"]["relative_humidity_2m"])     # List[float] 720 nilai
    
    
    return {
        "temperature": float(temperature),
        "humidity": float(humidity),
        "rainfall": float(rainfall)
    }