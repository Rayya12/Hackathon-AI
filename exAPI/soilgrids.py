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
    
    
    layers = data["properties"]["layers"]
    
    n_layer = next(l for l in layers if l["name"] == "nitrogen")
    ph_layer = next(l for l in layers if l["name"] == "phh2o")
    
    n_factor = n_layer["unit_measure"]["d_factor"]
    ph_factor = ph_layer["unit_measure"]["d_factor"]
    
    # convert & average 0–30cm
    nitrogen_avg_gkg = sum(d["values"]["mean"] for d in n_layer["depths"]) / len(n_layer["depths"]) / n_factor
    ph_avg = sum(d["values"]["mean"] for d in ph_layer["depths"]) / len(ph_layer["depths"]) / ph_factor
    
    # optional: convert nitrogen to percent
    nitrogen_percent = nitrogen_avg_gkg / 10
    
    return {
        "N_g_per_kg": nitrogen_avg_gkg,
        "N_percent": nitrogen_percent,
        "pH": ph_avg
    }
    
    


# contoh pakai
features = get_soil_features(-6.837985,107.674170)
print(features)