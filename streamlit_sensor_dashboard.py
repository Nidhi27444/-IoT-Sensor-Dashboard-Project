
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("cleaned_sensor_data.csv", parse_dates=["timestamp"])

st.title("IoT Sensor Dashboard")

# Filters
st.sidebar.header("Filter Sensor Data")
temp_range = st.sidebar.slider("Temperature (°C)", float(df.temperature_C.min()), float(df.temperature_C.max()), (float(df.temperature_C.min()), float(df.temperature_C.max())))
pressure_range = st.sidebar.slider("Pressure (kPa)", float(df.pressure_kPa.min()), float(df.pressure_kPa.max()), (float(df.pressure_kPa.min()), float(df.pressure_kPa.max())))

filtered_df = df[
    (df.temperature_C >= temp_range[0]) & (df.temperature_C <= temp_range[1]) &
    (df.pressure_kPa >= pressure_range[0]) & (df.pressure_kPa <= pressure_range[1])
]

# Display stats
st.subheader("Filtered Data Overview")
st.write(filtered_df.describe())

# Line charts
st.subheader("Temperature Over Time")
fig_temp = px.line(filtered_df, x="timestamp", y="temperature_C", title="Temperature (°C)")
st.plotly_chart(fig_temp)

st.subheader("Pressure Over Time")
fig_press = px.line(filtered_df, x="timestamp", y="pressure_kPa", title="Pressure (kPa)")
st.plotly_chart(fig_press)

st.subheader("Humidity Over Time")
fig_hum = px.line(filtered_df, x="timestamp", y="humidity_percent", title="Humidity (%)")
st.plotly_chart(fig_hum)

st.subheader("Air Quality Index Over Time")
fig_aqi = px.line(filtered_df, x="timestamp", y="air_quality_index", title="Air Quality Index")
st.plotly_chart(fig_aqi)
