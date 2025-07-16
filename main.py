from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.models import load_model

app = FastAPI()
model = load_model("diabetes_prediction.h5")

class PatientData(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

@app.get("/")
def root():
    return {"message": "Diabetes prediction API is live."}

@app.post("/predict")
def predict(data: PatientData):
    input_array = np.array([[
        data.Pregnancies, data.Glucose, data.BloodPressure, data.SkinThickness,
        data.Insulin, data.BMI, data.DiabetesPedigreeFunction, data.Age
    ]])
    prediction = model.predict(input_array)[0][0]
    result = "Likely Diabetic" if prediction > 0.5 else "Likely Not Diabetic"
    return {"probability": float(prediction), "result": result}
