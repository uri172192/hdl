import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from vega_datasets import data
import matplotlib.colors as mcolors
from PIL import Image

# Configura el título de la página i favicon
st.set_page_config(page_title="Scorers", page_icon="ball.png", layout="wide")

st.title('🏐Scorers')
st.header('🎯Goleadores Asobal')
st.subheader('📌Consulta todos los goleadores según **equipo**:')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    imageasobal = Image.open('apple-touch-icon.png')
    st.image(imageasobal)

df = pd.read_excel("DatasetJugadoresAsobal.xlsx")
df1 = pd.read_excel("DatasetJugadoresAsobal2324.xlsx")

# Obtener una lista de temporadas únicas de ambos DataFrames
temporadas = pd.concat([df1['Temporada'], df['Temporada']]).unique()

# Crear el select box para la temporada
selected_temporada1 = st.selectbox('Escoge una temporada:', temporadas, key="selectbox1")

# Filtrar los datos según la temporada seleccionada desde ambos DataFrames
filtered_data1 = pd.concat([df[df['Temporada'] == selected_temporada1], df1[df1['Temporada'] == selected_temporada1]])

# Obtener una lista de equipos únicos para la temporada seleccionada
equipos_temporada = filtered_data1['Equipo'].unique()

# Crear el select box para el equipo
selected_equipo = st.selectbox('Escoge un equipo:', equipos_temporada)

# Filtrar los datos nuevamente para mostrar solo el equipo seleccionado
filtered_data11 = filtered_data1[filtered_data1['Equipo'] == selected_equipo]

# Crear un diccionario de colores personalizados para cada equipo
custom_team_colors = {
    'Barça': 'darkred',
    'Granollers': 'royalblue',
    'Cuenca': 'sienna',
    'Torrelavega': 'orange',
    'Bidasoa': 'olive',
    'Logroño': 'tomato',
    'Ademar': 'lightcoral',
    'Puente Genil': 'mediumspringgreen',
    'Anaitasuna': 'forestgreen',
    'Benidorm': 'cornflowerblue',
    'Huesca': 'red',
    'Sinfin': 'black',
    'Valladolid': 'mediumblue',
    'Cangas': 'navy',
    'Puerto Sagunto': 'firebrick',
    'Nava': 'bisque',
    'Cisne': 'silver',
    'Guadalajara': 'purple',
    # Agrega más equipos y colores según sea necesario
}

# Asigna los colores personalizados a los equipos
team_colors = {equipo: custom_team_colors.get(equipo, 'magenta') for equipo in equipos_temporada}

# Crear el gráfico
graph = alt.Chart(filtered_data11).encode(
    x='ToG',
    y=alt.Y("Jugador").sort('-x'),
    text='ToG',
    tooltip=['Jugador', 'Equipo', 'ToG', 'ToS', 'To%'],
    color=alt.Color("Equipo", scale=alt.Scale(domain=list(team_colors.keys()), range=list(team_colors.values())))
)
plotfinal = graph.mark_bar() + graph.mark_text(align='left', dx=2)

# Mostrar el gráfico en Streamlit
st.altair_chart(plotfinal, use_container_width=True)

st.caption("🔎Fuente: Asobal")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**ToG** = Total Goles Marcados")
expander.write("**ToS** = Total Lanzamientos Intentados")
expander.write("**To%** = Porcentaje de acierto en el lanzamiento")

st.divider()

st.subheader('📌Consulta todos los goleadores según **posición**:')

# Crear el filtro de temporada para el segundo gráfico en el cuerpo principal
selected_temporada2 = st.selectbox('Escoge una temporada:', temporadas, key="selectbox2")

# Filtrar los datos según la temporada seleccionada desde ambos DataFrames
filtered_data2 = pd.concat([df[df['Temporada'] == selected_temporada2], df1[df1['Temporada'] == selected_temporada2]])

# Obtener una lista de equipos únicos para la temporada seleccionada
equipos_temporada2 = filtered_data2['Equipo'].unique()

# Obtener una lista de posiciones únicos para la temporada seleccionada
pos_temporada = filtered_data2['Posicion'].unique()

# Crear el select box para la posicion
selected_pos = st.selectbox('Escoge una posicion:', pos_temporada)

# Filtrar los datos nuevamente para mostrar solo  seleccionado
filtered_data22 = filtered_data2[filtered_data2['Posicion'] == selected_pos]

# Crear un diccionario de colores personalizados para cada equipo
custom_team_colors = {
    'Barça': 'darkred',
    'Granollers': 'royalblue',
    'Cuenca': 'sienna',
    'Torrelavega': 'orange',
    'Bidasoa': 'olive',
    'Logroño': 'tomato',
    'Ademar': 'lightcoral',
    'Puente Genil': 'mediumspringgreen',
    'Anaitasuna': 'forestgreen',
    'Benidorm': 'cornflowerblue',
    'Huesca': 'red',
    'Sinfin': 'black',
    'Valladolid': 'mediumblue',
    'Cangas': 'navy',
    'Puerto Sagunto': 'firebrick',
    'Nava': 'bisque',
    'Cisne': 'silver',
    'Guadalajara': 'purple',
    # Agrega más equipos y colores según sea necesario
}

# Asigna los colores personalizados a los equipos
team_colors = {equipo: custom_team_colors.get(equipo, 'magenta') for equipo in equipos_temporada2}

# Crear el gráfico
graph = alt.Chart(filtered_data22).encode(
    x='ToG',
    y=alt.Y("Jugador").sort('-x'),
    text='ToG',
    tooltip=['Jugador', 'Posicion','Equipo', 'ToG', 'ToS', 'To%'],
    color=alt.Color("Equipo", scale=alt.Scale(domain=list(team_colors.keys()), range=list(team_colors.values())))
)
plotfinalpos = graph.mark_bar() + graph.mark_text(align='left', dx=2)

# Mostrar el gráfico en Streamlit
st.altair_chart(plotfinalpos, use_container_width=True)

st.caption("🔎Fuente: Asobal")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**ToG** = Total Goles Marcados")
expander.write("**ToS** = Total Lanzamientos Intentados")
expander.write("**To%** = Porcentaje de acierto en el lanzamiento")
