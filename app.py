import streamlit as st
import requests

st.title("🧠 Diabetes Prediction App")
st.write("Enter Patient Info to predict diabetes risk.")

data = {
    "Pregnancies": st.number_input("Pregnancies", min_value=0.0, step=1.0),
    "Glucose": st.number_input("Glucose", min_value=0.0),
    "BloodPressure": st.number_input("Blood Pressure", min_value=0.0),
    "SkinThickness": st.number_input("Skin Thickness", min_value=0.0),
    "Insulin": st.number_input("Insulin", min_value=0.0),
    "BMI": st.number_input("BMI", min_value=0.0),
    "DiabetesPedigreeFunction": st.number_input("Diabetes Pedigree Function", min_value=0.0),
    "Age": st.number_input("Age", min_value=0.0, step=1.0)
}

if st.button("Predict"):
    try:
        res = requests.post("http://localhost:8000/predict", json=data)
        output = res.json()
        st.success(f"{output['result']} (Confidence: {output['probability']:.2f})")
    except:
        st.error("Prediction failed. Make sure FastAPI server is running properly.")
