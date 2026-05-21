import streamlit as st 
import pandas as pd
import requests
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Urban Environmental Analytics",
    layout="wide"
)

# Titlepytho
st.title("Urban Environmental Analytics Platform")
st.subheader("Monthly PM2.5 Trends in Mumbai")

# Fetch average PM2.5
avg_response = requests.get("http://127.0.0.1:8000/average-pm25")
avg_pm25 = avg_response.json()["average_pm25"]

# Display KPI
st.metric("Average PM2.5", f"{avg_pm25:.2f}")

# Fetch monthly trends
response = requests.get("http://127.0.0.1:8000/monthly-trends")
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)
df["month"] = pd.to_datetime(df["month"])

# Plot line chart
fig = px.line(
    df,
    x="month",
    y="avg_pm25",
    title="Monthly Average PM2.5"
)

st.plotly_chart(fig, use_container_width=True)

# Show raw data
with st.expander("View Data"):
    st.dataframe(df)