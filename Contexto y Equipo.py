import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Carga las imágenes
imagen1 = Image.open('vale.jpg')
imagen2 = Image.open('belen.jpg')
imagen3 = Image.open('franco.jpg')
imagen4 = Image.open('cata.jpg')

logo = Image.open('logo.png')

st.sidebar.image(logo, width=180)

# Agrega un título de contexto y una reseña pequeña
st.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 40px; font-weight:bold; text-shadow: 2px 2px 4px #000000;">Contexto</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify;">En la actualidad, la corrupción sigue siendo un desafío significativo a nivel global. A medida que se avanza la digitalización, los métodos de corrupción también evolucionan adoptando nuevas formas lo que hace más difícil su detección.</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify;">El objetivo principal es generar un Indicador de Propensión a la Corrupción que le asigna un puntaje score a cada funcionario público</p>', unsafe_allow_html=True)
st.markdown("         ")
st.markdown("         ")

# Agrega el título "Quienes Somos"
st.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 40px; font-weight:bold; text-shadow: 2px 2px 4px #000000;">Quienes Somos</p>', unsafe_allow_html=True)
st.markdown("         ")
st.markdown("         ")

col1, col2, col3, col4 = st.columns(4)

# integrantes

linkedin_url1 = "https://www.linkedin.com/in/valentina-pino-728031140/"
linkedin_url2 = "https://www.linkedin.com/in/bel%C3%A9n-tramolao-mardones-616a58137/"
linkedin_url3 = "https://www.linkedin.com/in/franco-alberto-gonz%C3%A1lez-b1870a22b/"
linkedin_url4 = "https://www.linkedin.com/in/catalina-montero-c%C3%A1ceres-24696b287/"

col1.image(imagen1, width=160)
col1.markdown("Valentina Pino")
col1.write('Analista de Inteligencia Financiera, UAF')

col2.image(imagen2, width=150)
col2.markdown("Belén Tramolao")
col2.write('Analista de Riesgo de Crédito, KPMG')

col3.image(imagen3, width=106)
col3.markdown("Franco González")
col3.write('Estudiante de Ing. Matemática, UTFSM')

col4.image(imagen4, width=113)
col4.markdown("Catalina Montero")
col4.write('Estudiante de Ing. Estadística, USACH')
