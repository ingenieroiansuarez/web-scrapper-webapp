import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("temperatures.db")
cursor = connection.cursor()
cursor.execute("SELECT date FROM temperatures")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temperature FROM temperatures")
temperatures = cursor.fetchall()
temperatures = [item[0] for item in temperatures]


figure = px.line(x=date, y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)