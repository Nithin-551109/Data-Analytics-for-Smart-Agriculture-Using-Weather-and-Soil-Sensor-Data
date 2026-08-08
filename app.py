import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Data Analytics for Smart Agriculture")
st.write("Weather and Soil Sensor Data Analysis")

data = pd.read_csv("agriculture_data.csv")

st.subheader("Agricultural Sensor Data")
st.dataframe(data)

st.subheader("Soil Moisture Analysis")
fig, ax = plt.subplots()
ax.plot(data["Soil_Moisture"])
ax.set_xlabel("Reading")
ax.set_ylabel("Soil Moisture (%)")
st.pyplot(fig)

st.subheader("Temperature Analysis")
fig, ax = plt.subplots()
ax.plot(data["Temperature"])
ax.set_xlabel("Reading")
ax.set_ylabel("Temperature (°C)")
st.pyplot(fig)

avg_moisture = data["Soil_Moisture"].mean()

if avg_moisture < 40:
    st.warning("Soil moisture is low. Irrigation may be required.")
else:
    st.success("Soil moisture is sufficient.")