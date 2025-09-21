import streamlit as st
import joblib
import numpy as np

st.title("Battery State of Health Prediction")

model = joblib.load("random_forest_soh.pkl")

# User inputs
terminal_voltage = st.number_input('Terminal Voltage')
terminal_current = st.number_input('Terminal Current')
temperature = st.number_input('Temperature')
charge_current = st.number_input('Charge Current')
charge_voltage = st.number_input('Charge Voltage')
time = st.number_input('Time')
capacity = st.number_input('Capacity')
cycle = st.number_input('Cycle')

if st.button('Predict SOH'):
    features = np.array([[terminal_voltage, terminal_current, temperature, charge_current, charge_voltage, time, capacity, cycle]])
    prediction = model.predict(features)[0]
    st.write(f"Predicted State of Health: {predicted_soh}")

