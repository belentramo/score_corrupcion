import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from PIL import Image

logo = Image.open('logo.png')

st.sidebar.image(logo, width=200)

# Abre la imagen del favicon
#favicon = Image.open('favicon.ico')

# Configura la página para usar la imagen como favicon
#st.set_page_config(page_icon=favicon)

df=pd.read_excel("Base_score.xlsx")
print(df.info())

#st.title("Corruption Likelihood Assessment in the Public Sector")
#st.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 26px;">Corruption Likelihood Assessment in the Public Sector</p>', unsafe_allow_html=True)
st.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 30px; font-weight:bold;">Corruption Likelihood Assessment in the Public Sector</p>', unsafe_allow_html=True)
# Agregar un espacio vacío
st.markdown("\n\n\n\n\n\n\n")

st.sidebar.title("Información")

filtro_region=st.sidebar.selectbox("Región",df["Region"].unique())
filtro_organismo=st.sidebar.selectbox("Organismo",df["Organismo"].unique())
df_filtered = df.query('Region == @filtro_region and Organismo == @filtro_organismo')

st.dataframe(df_filtered)

data = df_filtered['score_pred']

hist_data = np.histogram(data, bins=20)

bar = go.Bar(x=hist_data[1], y=hist_data[0], width=np.diff(hist_data[1]), name='Histograma')

line = go.Scatter(x=hist_data[1], y=hist_data[0], mode='lines', name='Distribución')

fig = go.Figure(data=[bar, line])

fig.update_layout(
    title={
        'text': "Histograma de score_pred",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title="Puntaje Score",
    yaxis_title="Frecuencia",
    plot_bgcolor='rgba(0,0,0,0)',
    bargap=0.2,
)

st.plotly_chart(fig)