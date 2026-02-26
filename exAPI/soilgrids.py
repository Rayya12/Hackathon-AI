import requests

def get_soil_data(lat: float, lon: float):
    url = "https://rest.isric.org/soilgrids/v2.0/properties/query"
    params = {
        "lon": lon,
        "lat": lat,
        "property": ["nitrogen", "phh2o"],
        "depth": ["0-5cm", "5-15cm", "15-30cm"],
        "value": "mean"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    layers = data["properties"]["layers"]
    
    # Ambil nilai per kedalaman untuk setiap property
    nitrogen_layer = next(l for l in layers if l["name"] == "nitrogen")
    ph_layer = next(l for l in layers if l["name"] == "phh2o")
    
    nitrogen = [
        depth["values"]["mean"] for depth in nitrogen_layer["depths"]
    ]  # List[float] 3 nilai (0-5, 5-15, 15-30cm)
    
    ph = [
        depth["values"]["mean"] for depth in ph_layer["depths"]
    ]  # List[float] 3 nilai (0-5, 5-15, 15-30cm)
    
    return nitrogen, ph