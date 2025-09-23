import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Battery SoH Predictor", page_icon="🔋", layout="centered")

# Banner image
st.image("battery_banner.png", use_column_width=True)

st.title("🔋 Battery State of Health (SoH) Predictor")

st.markdown("""
Enter the battery parameters below exactly as shown in your dataset for accurate predictions.
""")

st.divider()

col1, col2 = st.columns(2)
with col1:
    terminal_voltage = st.number_input(
        'Terminal Voltage (V)', format="%.6f"
    )
    terminal_current = st.number_input(
        'Terminal Current (A)', format="%.6f"
    )
    temperature = st.number_input(
        'Temperature (°C)', format="%.5f"
    )
    charge_current = st.number_input(
        'Charge Current (A)', format="%.5f"
    )

with col2:
    charge_voltage = st.number_input(
        'Charge Voltage (V)', format="%.4f"
    )
    time = st.number_input(
        'Time (s)', format="%.3f"
    )
    capacity = st.number_input(
        'Capacity (Ah)', format="%.6f"
    )
    cycle = st.number_input(
        'Cycle Number', format="%d", step=1
    )

st.divider()

model = joblib.load("random_forest_soh.pkl")

if st.button('Predict SOH'):
    features = np.array([
        [terminal_voltage, terminal_current, temperature, charge_current, charge_voltage, time, capacity, cycle]
    ])
    predicted_soh = model.predict(features)[0]
    st.metric("🔋 Predicted Battery SoH", f"{predicted_soh:.6f}")

    st.write("""
    **Note:**  
    SOH (State of Health) is an indicator of battery condition compared to its original specifications.
    """)

st.markdown("<br><br>", unsafe_allow_html=True)
