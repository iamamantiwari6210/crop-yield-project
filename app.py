import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Crop Yield Dashboard", layout="wide")

st.title("🌾 Crop Yield Prediction Dashboard")

# Sidebar inputs
st.sidebar.header("Input Parameters")

rainfall = st.sidebar.slider("Rainfall (mm)", 0, 500, 100)
temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 25)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 60)

# Dummy prediction (replace later)
yield_prediction = (rainfall * 0.3) + (temperature * 0.5) + (humidity * 0.2)

st.subheader("📊 Predicted Crop Yield")
st.success(f"Estimated Yield: {yield_prediction:.2f} tons/hectare")

# Sample chart
data = pd.DataFrame({
    "Rainfall": np.random.randint(50, 300, 50),
    "Yield": np.random.randint(1, 10, 50)
})

st.line_chart(data)
st.dataframe(data)
