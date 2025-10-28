import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
st.header('Análisis de datos de vehículos')

# Crear botón
if st.button('Mostrar histograma'):
    st.write('Creando un gráfico de histograma para los datos seleccionados...')
    
    # Crear histograma con plotly
    fig = px.histogram(car_data, x='odometer', title='Distribución del odómetro')
    
    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)

# Botón para gráfico de dispersión
if st.button('Mostrar gráfico de dispersión'):
    st.write('Creando gráfico de dispersión...')
    fig2 = px.scatter(car_data, x='odometer', y='price',
                      title='Relación entre odómetro y precio')
    st.plotly_chart(fig2)

    