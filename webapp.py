import streamlit as st
import plotly.express as px
import pandas

# Load data from a text file
df = pandas.read_csv("data.txt")
# Convert the 'date' column to datetime format
figure = px.line(x=df["date"], y=df["temperature"],
                             labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)