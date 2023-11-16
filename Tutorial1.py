import streamlit as st
import pandas as pd


df=pd.read_excel("Base_score.xlsx")

st.title("Prueba Score")
filtro=st.sidebar.selectbox("Región",df["Region"].unique())

st.dataframe(df[df["Region"]==filtro])