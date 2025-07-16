# 🧠 Diabetes Prediction AI with FastAPI

This project is an AI-based application that predicts the likelihood of diabetes in a patient based on health metrics like Glucose, BMI, Insulin, Age, etc. It uses a TensorFlow deep learning model and is served using FastAPI for API access.

## 🚀 Features

- ✅ Predicts diabetes using 8 health features  
- 🧪 Trained using TensorFlow/Keras on PIMA Indians Diabetes dataset  
- ⚙️ FastAPI backend to serve model as a REST API  
- 🔬 Includes data preprocessing (handling missing/zero values)  
- 📈 Performance evaluated using accuracy, confusion matrix, F1-score  
- 🔒 Easily extendable with frontend or mobile integration  

## 📁 Project Structure
diabetes_prediction_ai/
├── app.py # Optional Streamlit frontend (if used)
├── main.py # FastAPI app for serving the model
├── diabetes_model.h5 # Trained TensorFlow model
├── requirements.txt # All Python dependencies
├── README.md # This file
└── venv/ # Python virtual environment (optional)

## 📊 Dataset

*Source:* PIMA Indians Diabetes Dataset  
*Link:* https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv

*Columns Used:*
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
- Outcome (0 = No diabetes, 1 = Diabetes)

## ⚙️ How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/diabetes_prediction_ai.git
cd diabetes_prediction_ai
