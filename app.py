import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model
model = joblib.load("rf_model.pkl")

# App title
st.title("🧠 AI Kit – Cost Savings Estimator")
st.write("Predict monthly savings based on weather, production & resource usage.")

# Sidebar input
st.sidebar.header("🛠 Input Parameters")

weather_score = st.sidebar.slider("Weather Score (0: bad - 1: perfect)", 0.0, 1.0, 0.85)
qt_jeans_kg = st.sidebar.number_input("Quantity of jeans produced (kg)", min_value=10000, max_value=100000, value=58000)
qt_water_to_use_liters = st.sidebar.number_input("Water to be used (liters)", min_value=1000000, max_value=10000000, value=7000000)
qt_electricity_to_use_kWh = st.sidebar.number_input("Electricity to be used (kWh)", min_value=10000, max_value=200000, value=98000)

# Predict
input_data = pd.DataFrame([{
    "weather_score": weather_score,
    "qt_jeans_kg": qt_jeans_kg,
    "qt_water_to_use_liters": qt_water_to_use_liters,
    "qt_electricity_to_use_kWh": qt_electricity_to_use_kWh
}])

if st.button("Predict Savings 💰"):
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Estimated Monthly Cost Saved: **{prediction:.2f} TND**")

# Footer
st.markdown("---")
st.caption("Built with ❤️ for sustainable textile industries in Tunisia.")
