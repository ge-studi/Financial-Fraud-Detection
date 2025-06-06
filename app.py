# app.py
import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("best_model.pkl")  # Pipeline includes scaling

st.title("Fraud Detection System")

# Input fields
step = st.number_input("Step", min_value=0)
transaction_type = st.selectbox("Transaction Type", options=["CASH_OUT", "TRANSFER", "CASH_IN", "DEBIT", "PAYMENT"])
type_encoded = {"CASH_OUT": 0, "TRANSFER": 1, "CASH_IN": 2, "DEBIT": 3, "PAYMENT": 4}[transaction_type]
amount = st.number_input("Transaction Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0)

if st.button("Predict Fraud"):
    input_data = pd.DataFrame([[step, type_encoded, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]],
                              columns=['step', 'type_encoded', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest'])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("This transaction is likely FRAUDULENT!")
    else:
        st.success("This transaction appears to be legitimate.")
