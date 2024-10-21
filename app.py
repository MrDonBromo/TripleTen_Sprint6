import pandas as pd
import plotly.express as px
import streamlit as st

st.header("TripleTen Sprint 6: Vehicles Sales Data")
car_data = pd.read_csv('https://raw.githubusercontent.com/MrDonBromo/TripleTen_Sprint6/refs/heads/main/vehicles_us.csv')
hist_button = st.button('Crear histograma')
disp_button = st.button('Crear dispersion')


if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data,x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    st.write('Creación de un gráfico de dispersión')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig,use_container_width=True)
