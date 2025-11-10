import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Predictive Maintenance for EVs", page_icon="🧠", layout="wide")

st.title("🧠 Predictive Maintenance for Electric Vehicles")
st.write("Predict potential component failure using EV sensor data analytics.")

model = joblib.load("maintenance_model.pkl")
data = pd.read_csv("maintenance_data.csv")

# Sidebar input
st.sidebar.header("Sensor Inputs")
motor_temp = st.sidebar.slider("Motor Temperature (°C)", 30, 120, 70)
controller_temp = st.sidebar.slider("Controller Temperature (°C)", 25, 100, 55)
battery_voltage = st.sidebar.slider("Battery Voltage (V)", 3.0, 4.5, 3.8)
vibration = st.sidebar.slider("Vibration Level (g)", 0.1, 1.2, 0.4)

# Predict
input_df = pd.DataFrame([[motor_temp, controller_temp, battery_voltage, vibration]],
                        columns=["motor_temp", "controller_temp", "battery_voltage", "vibration"])

prediction = model.predict(input_df)[0]

if prediction == 1:
    st.error("⚠️ High Risk: Potential component failure detected. Maintenance required.")
else:
    st.success("✅ System Healthy: No immediate risk detected.")

# Visualization
st.subheader("📊 Sensor Data Analysis")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x="failure", y="motor_temp", ax=ax, palette="coolwarm")
    ax.set_title("Motor Temperature vs Failure")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x="failure", y="vibration", ax=ax, palette="viridis")
    ax.set_title("Vibration Level vs Failure")
    st.pyplot(fig)
