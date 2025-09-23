import streamlit as st
import joblib
import numpy as np

# Set page config for overall look and icon
st.set_page_config(page_title="Battery SoH Predictor", page_icon="🔋", layout="centered")

# Add a battery image banner (place 'battery_banner.png' in your repo root)
st.image("battery_banner.png", use_column_width=True)

st.title("🔋 Battery State of Health (SoH) Predictor")

st.markdown("""
Welcome to the Battery SoH predictor!  
Fill in the battery parameters below to estimate the State of Health.  
""")

st.divider()

# Group input fields in columns for a neat look
col1, col2 = st.columns(2)
with col1:
    terminal_voltage = st.number_input('🔌 Terminal Voltage (V)', min_value=None)  # allow negative decimals
    terminal_current = st.number_input('⚡ Terminal Current (A)', min_value=None)  # allow negative decimals
    temperature = st.number_input('🌡️ Temperature (°C)', min_value=None)           # allow negative decimals
    charge_current = st.number_input('🔋 Charge Current (A)', min_value=None)      # allow negative decimals if possible
with col2:
    charge_voltage = st.number_input('🔌 Charge Voltage (V)', min_value=None)      # allow negative decimals if possible
    time = st.number_input('⏰ Time (s)', min_value=0.0)
    capacity = st.number_input('🔋 Capacity (Ah)', min_value=0.0)
    cycle
