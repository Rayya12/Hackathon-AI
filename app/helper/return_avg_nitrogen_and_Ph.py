from app.schema.inputSchema import InputData

def return_avg_nitrogen_and_Ph(inputData: InputData):
    
    if (not inputData.soil):
        return {
            "N_kg_per_ha": 50.55,
            "pH": 6.5 
        }
    
    data = inputData.soil
    layers = data["properties"]["layers"]
    
    n_layer = next(l for l in layers if l["name"] == "nitrogen")
    ph_layer = next(l for l in layers if l["name"] == "phh2o")
    
    n_factor = n_layer["unit_measure"]["d_factor"]
    ph_factor = ph_layer["unit_measure"]["d_factor"]
    
    # convert & average 0–30cm (g/kg)
    nitrogen_avg_gkg = (
        sum(d["values"]["mean"] for d in n_layer["depths"])
        / len(n_layer["depths"])
        / n_factor
    )
    
    ph_avg = (
        sum(d["values"]["mean"] for d in ph_layer["depths"])
        / len(ph_layer["depths"])
        / ph_factor
    )
    
    # convert g/kg → kg/ha
    bulk_density = 1.3   # g/cm³ (average soil)
    depth_cm = 30
    conversion_factor = bulk_density * depth_cm * 0.1  # = 3.9
    
    nitrogen_kg_per_ha = nitrogen_avg_gkg * conversion_factor
    
    return {
        "N_kg_per_ha": nitrogen_kg_per_ha,
        "pH": ph_avg
    }