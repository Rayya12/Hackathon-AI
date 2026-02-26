from fastapi import FastAPI
import joblib
from app.schema.inputSchema import InputData
from app.schema.outputSchema import OutputData
import numpy as np
import pandas as pd


app = FastAPI()

# Model Name
MODEL_NAME = "model/best_model.pkl"
Label_ENCODER = "model/label_encoder.pkl"

def load_model_and_encoder():
    return joblib.load(MODEL_NAME), joblib.load(Label_ENCODER) 

model,encoder = load_model_and_encoder()

@app.post("/predict", response_model=OutputData)
def predict(inputData: InputData):
    
    
    input = {
        "N": [np.mean(inputData.nitrogen)],
        "temperature": [np.mean(inputData.temperature)],
        "humidity": [np.mean(inputData.humidity)],
        "ph": [np.mean(inputData.ph)],
        "rainfall": [np.mean(inputData.rainfall)]
    }
    
    input_df = pd.DataFrame(input)
    
    # Get predicted class index and decode it
    prediction = model.predict(input_df)
    predicted_class = encoder.inverse_transform(prediction)[0]
    
    # Get probability of the predicted class
    proba = model.predict_proba(input_df)
    predicted_proba = float(np.max(proba))  # highest probability
    
    proba_sorted = np.sort(proba[0])[::-1][:3]
    indices = np.argsort(proba[0])[::-1][:3]

    top3 = {encoder.inverse_transform([i])[0]: round(v, 4) for i, v in zip(indices, proba_sorted)}
    
    
    return OutputData(
        prediction_class=predicted_class,
        probability=predicted_proba,
        top3=top3
    )   
    
    
    
    




