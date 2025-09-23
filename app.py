import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Battery SoH Predictor", page_icon="🔋", layout="centered")

st.image("battery_banner.png", use_column_width=True)

st.title("🔋 Battery State of Health (SoH) Predictor")

st.markdown("""
Welcome to the Battery SoH predictor!  
Fill in the battery parameters below to estimate the State of Health.  
""")

st.divider()

def get_float_input(label, default="0.0"):
    val = st.text_input(label, value=default)
    try:
        fval = float(val)
        valid = True
    except ValueError:
        st.warning(f"Please enter a valid number for {label}")
        valid = False
        fval = None
    return fval, valid

col1, col2 = st.columns(2)
with col1:
    terminal_voltage, valid1 = get_float_input('Terminal Voltage (V)')
    terminal_current, valid2 = get_float_input('Terminal Current (A)')
    temperature, valid3 = get_float_input('Temperature (°C)')
    charge_current, valid4 = get_float_input('Charge Current (A)')
with col2:
    charge_voltage, valid5 = get_float_input('Charge Voltage (V)')
    time, valid6 = get_float_input('Time (s)')
    capacity, valid7 = get_float_input('Capacity (Ah)')
    cycle_str = st.text_input('Cycle Number', value="0")
    try:
        cycle = int(cycle_str)
        valid8 = True
    except ValueError:
        st.warning("Please enter a valid integer for Cycle Number")
        cycle = None
        valid8 = False

st.divider()

all_valid = all([valid1, valid2, valid3, valid4, valid5, valid6, valid7, valid8])

model = joblib.load("random_forest_soh.pkl")

if st.button('Predict SOH', disabled=not all_valid):
    features = np.array([[terminal_voltage, terminal_current, temperature, charge_current,
                          charge_voltage, time, capacity, cycle]])
    predicted_soh = model.predict(features)[0]
    st.metric("🔋 Predicted Battery SoH", f"{predicted_soh:.6f}")
    st.write("""
    **Note:**  
    SOH (State of Health) is an indicator of battery condition compared to its original specifications.
    """)

st.markdown("<br><br>", unsafe_allow_html=True)
