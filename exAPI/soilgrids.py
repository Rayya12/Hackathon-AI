import requests

def get_soil_features(lat: float, lon: float):
    url = "https://rest.isric.org/soilgrids/v2.0/properties/query"
    params = {
        "lon": lon,
        "lat": lat,
        "property": ["nitrogen", "phh2o"],
        "depth": ["0-5cm", "5-15cm", "15-30cm"],
        "value": ["mean"]
    }
    
    data = requests.get(url, params=params).json()
    
    
    return data
    
    


# contoh pakai
features = get_soil_features(-6.837985,107.674170)
print(features)