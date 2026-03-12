🌱 Crop Recommendation System

A machine learning model that predicts the most suitable crop based on environmental and soil conditions.

This system integrates:

🌦 Weather data from Open-Meteo API
🧪 Soil data from SoilGrids API
🌳 Tree-based ML model (Random Forest / Gradient Boosting)

📌 Overview

The model predicts crop suitability using:

Soil Nitrogen (0–30 cm depth average)
Temperature (30-day average)
Humidity (30-day average)
Soil pH (0–30 cm depth average)
Rainfall (30-day total)

The model was trained on structured environmental data and expects the same input format during inference.

🧾 Required Input Features
The model expects 5 numerical features in the following exact order:
[
    N,
    temperature,
    humidity,
    ph,
    rainfall
]

Feature	Description	Source
N	Soil Nitrogen average at depth 0–30 cm	SoilGrids
temperature	Average temperature (°C) over the last 30 days	Open-Meteo
humidity	Average relative humidity (%) over the last 30 days	Open-Meteo
ph	Soil pH average at depth 0–30 cm	SoilGrids
rainfall	Total rainfall (mm) over the last 30 days	Open-Meteo


⚠ Feature order must match training order.

🌦 Weather Data Collection (Open-Meteo)
Use the Open-Meteo archive API to retrieve historical daily data.

Recommended variables:
temperature_2m_mean
relative_humidity_2m_mean
precipitation_sum

Then compute:
30-day average temperature
30-day average humidity
30-day total rainfall


🧪 Soil Data Collection (SoilGrids)

Query soil properties at depth:
0–5 cm
5–15 cm
15–30 cm

Then compute the average across 0–30 cm.
Recommended layers:
phh2o → soil pH
nitrogen → nitrogen content


📦 Model Information

Model type: Tree-based ensemble
Robust to outliers
Handles nonlinear relationships
No feature scaling required


📊 Model Interpretability

The model was analyzed using:
Feature importance
SHAP (SHapley Additive Explanations)

Key findings:
Rainfall and humidity strongly influence predictions
Nitrogen content plays a major role
Temperature and pH contribute moderately

📌 Assumptions

Weather data represents the average of the last 30 days
Soil data represents the mean value from depth 0–30 cm

All units must match training data:
Temperature → °C
Rainfall → mm
Humidity → %
pH → standard scale
Nitrogen → SoilGrids unit

🛠 Tech Stack

Python
Scikit-learn
LightGBM / XGBoost
Optuna
SHAP
Open-Meteo API
SoilGrids API

# 🚀 HOW TO RUN

## Prerequisites
- [Git](https://git-scm.com/)
- [Anaconda](https://www.anaconda.com/) atau [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/Rayya12/Hackathon-AI.git
   cd HACKATHON-AI
   ```

2. **Create the conda environment**
   ```bash
   conda create -n venv-name python=3.x # use the version you like
   ```

3. **Activate the environment**
   ```bash
   conda activate nama_env
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Activate the project
Open `main.ipynb` Using Jupyter Notebook or VS Code, use kernell `venv-name` That you have created. If you want to use the main.py file, In Vscode press ctrl shift p and select the interpreter/environtment that you have created. In terminal, type python/python3 main.py to activate.

