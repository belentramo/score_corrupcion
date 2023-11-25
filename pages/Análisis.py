import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


df=pd.read_excel("data_agrupada.xlsx")

logo = Image.open('logo.png')

st.sidebar.image(logo, width=180)

st.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 40px; font-weight:bold; text-shadow: 2px 2px 4px #000000;">Corruption Likelihood Assessment in the Public Sector</p>', unsafe_allow_html=True)
st.markdown("         ")
st.markdown("         ")

st.sidebar.title("Información")

filtro_año=st.sidebar.selectbox("Años",df["YY"].unique())
df_filtered= df.query('YY == @filtro_año')
filtro_cargo_cluster=st.sidebar.selectbox("Cargo",df_filtered["Cargo"].unique())
df_filtered= df_filtered.query('Cargo == @filtro_cargo_cluster')
filtro_organismo_cluster=st.sidebar.selectbox("Organismo",df_filtered["Organismo"].unique())
df_filtered= df_filtered.query('Organismo == @filtro_organismo_cluster')
filtro_organismo_detalle=st.sidebar.selectbox("Organismo Detalle",df_filtered["Nombre_del_Organismo"].unique())
df_filtered= df_filtered.query('Nombre_del_Organismo == @filtro_organismo_detalle')

#st.dataframe(df_filtered)

score_exp = df_filtered['score']
variacion=df_filtered['variacion_yy_ant']

#hist_data = np.histogram(score_exp, bins=20)

#bar = go.Bar(x=hist_data[1], y=hist_data[0], width=np.diff(hist_data[1]), name='Histograma')

#line = go.Scatter(x=hist_data[1], y=hist_data[0], mode='lines', name='Distribución')

#fig = go.Figure(data=[bar, line])

promedio_score_exp=score_exp.mean()
n_funcionarios=len(score_exp)
numero_adicional = 50  # Aquí puedes reemplazarlo con el valor de tu columna

velocimetro = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = promedio_score_exp,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Score Promedio"},
    #delta = {'reference': numero_adicional},
    gauge = {
        'axis': {'range': [None, 1000]},
        'bar': {'color': "green" if promedio_score_exp < 500 else "yellow" if promedio_score_exp < 600 else "red"},
        'steps': [
            {'range': [0, 500], 'color': 'lightgray'},
            {'range': [500, 1000], 'color': 'gray'}
        ],
    }
))

st.plotly_chart(velocimetro)

    #fig.update_layout(
        #title={
            #'text': "Histograma de score_exp",
            #'y':0.9,
            #'x':0.5,
            #'xanchor': 'center',
            #'yanchor': 'top'},
        #xaxis_title="Puntaje Score",
        #yaxis_title="Frecuencia",
        #plot_bgcolor='rgba(0,0,0,0)',
        #bargap=0.2,
    #)

    #st.plotly_chart(fig)

# promedio_score_exp=score_exp.mean()
# n_funcionarios=len(score_exp)

# st.markdown(
#         """
#         <style>
#         [data-testid="stMetricValue"] {
#             font-size: 100px;
#         }
#         </style>
#         """,
#     unsafe_allow_html=True,
# )

# st.metric("Funcionarios", n_funcionarios, "-8%")


##### BURBUJAS


aux = df.query('YY == @filtro_año').groupby(['Cargo', 'Organismo']).agg(score = ('score', 'mean')).reset_index()
aux['org_cargo'] = aux.Organismo + ' - ' + aux.Cargo
aux['numero_cat'] = list(range(1,17))
aux2 = aux[['org_cargo','numero_cat','score']]

aux2 = aux2.sort_values(['score'], ascending=False).reset_index()
indices_ordenados = aux2['score'].sort_values(ascending=False).index
aux2['colores'] = np.where(aux2.score < 500, 'green', 'red')

fig, ax = plt.subplots(figsize=(8, 6))

# Graficar el gráfico de burbujas con colores personalizados
ax.scatter(aux2.loc[indices_ordenados, 'numero_cat'], aux2.loc[indices_ordenados, 'org_cargo'],
                      s=aux2.loc[indices_ordenados, 'score']*10, alpha=0.5, c=aux2.colores)

# Agregar etiquetas a cada burbuja
for i, txt in enumerate(aux2.loc[indices_ordenados, 'score']):
    ax.annotate(f'{txt:.2f}', (aux2.loc[indices_ordenados, 'numero_cat'].iloc[i], aux2.loc[indices_ordenados, 'org_cargo'].iloc[i]),
                 textcoords="offset points", xytext=(0, 5), ha='center')

# Añadir etiquetas y título
ax.set_xlabel('Número de categoría')
ax.set_ylabel('Categoría')
ax.set_title('Gráfico de Burbujas Organismo - Cargo y SCORE promedio')

st.pyplot(fig)

