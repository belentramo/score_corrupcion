import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_excel("Base_score.xlsx")
print(df.info())

st.title("Prueba Score")
filtro_region=st.sidebar.selectbox("Región",df["Region"].unique())
filtro_organismo=st.sidebar.selectbox("Organismo",df["Organismo"].unique())
#df_filtered=df[df["Region"]==filtro_region] & df[df["Organismo"]==filtro_organismo]
df_filtered = df.query('Region == @filtro_region and Organismo == @filtro_organismo')

#df_filtered=df[df["Organismo"]==filtro_organismo]
st.dataframe(df_filtered)

# Crear un histograma con Plotly Express
fig = px.histogram(df_filtered, x='score_pred', nbins=20, title='Histograma de score_pred')# Mostrar el histograma

st.plotly_chart(fig)