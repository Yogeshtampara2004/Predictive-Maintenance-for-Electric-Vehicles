import pandas as pd
import numpy as np

np.random.seed(42)
n = 400

motor_temp = np.random.normal(70, 15, n).clip(30, 120)
controller_temp = np.random.normal(55, 10, n).clip(25, 100)
battery_voltage = np.random.normal(3.8, 0.2, n).clip(3.2, 4.3)
vibration = np.random.normal(0.4, 0.15, n).clip(0.1, 1.2)

# Failure logic
failure_prob = (motor_temp > 90) | (controller_temp > 75) | (vibration > 0.7) | (battery_voltage < 3.5)
failure = np.where(failure_prob, 1, 0)

df = pd.DataFrame({
    "motor_temp": motor_temp,
    "controller_temp": controller_temp,
    "battery_voltage": battery_voltage,
    "vibration": vibration,
    "failure": failure
})

df.to_csv("maintenance_data.csv", index=False)
print("✅ maintenance_data.csv generated successfully!")
