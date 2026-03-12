# =========================================================
# Loan Prediction Streamlit App
# =========================================================

import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Loan Prediction App")

# Input fields
Gender = st.selectbox("Gender", ["Male","Female"])
Married = st.selectbox("Married", ["Yes","No"])
Dependents = st.selectbox("Dependents", ["0","1","2","3+"])
Education = st.selectbox("Education", ["Graduate","Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes","No"])
ApplicantIncome = st.number_input("Applicant Income")
CoapplicantIncome = st.number_input("Coapplicant Income")
LoanAmount = st.number_input("Loan Amount")
Loan_Amount_Term = st.number_input("Loan Term")
Credit_History = st.selectbox("Credit History", [1.0, 0.0])
Property_Area = st.selectbox("Property Area", ["Urban","Semiurban","Rural"])

st.write("Fill the details and click predict.")

Gender = 1 if Gender == "Male" else 0
Married = 1 if Married == "Yes" else 0

Dependents_map = {"0":0, "1":1, "2":2, "3+":3}
Dependents = Dependents_map[Dependents]

Education = 0 if Education == "Graduate" else 1
Self_Employed = 1 if Self_Employed == "Yes" else 0

Property_Area_map = {"Urban":2, "Semiurban":1, "Rural":0}
Property_Area = Property_Area_map[Property_Area]
input_data = pd.DataFrame([[
    Gender,
    Married,
    Dependents,
    Education,
    Self_Employed,
    ApplicantIncome,
    CoapplicantIncome,
    LoanAmount,
    Loan_Amount_Term,
    Credit_History,
    Property_Area
]])
input_scaled = scaler.transform(input_data)
if st.button("Predict"):

    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")