import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from vega_datasets import data

# Configura el título de la página i favicon
st.set_page_config(page_title="Shooting Distances", page_icon="arrow.png", layout="wide")
st.title('🏹Shooting Distances')

df = pd.read_excel("DatasetJugadoresAsobal.xlsx")
df1 = pd.read_excel("DatasetJugadoresAsobal2324.xlsx")

st.subheader("📌Consulta los datos sobre lanzamientos intentados, anotados y el porcentaje correspondiente a cada jugador, según la distancia del lanzamiento, filtrando por equipo.")

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

#Grafic 6m
chart = alt.Chart(filtered_data11).encode(
    x='L6G',
    y=alt.Y("Jugador").sort('-x'),
    text='L6G',
    tooltip=['Jugador', 'Equipo', 'L6G', 'L6S', 'L6%']
)

plotfinal6M = chart.mark_bar() + chart.mark_text(align='left', dx=2)

#Grafic 9m
chart1 = alt.Chart(filtered_data11).encode(
    x='L9G',
    y=alt.Y("Jugador").sort('-x'),
    text='L9G',
    tooltip=['Jugador', 'Equipo', 'L9G', 'L9S', 'L9%']
)

plotfinal9M = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

#Grafic 7m
chart2 = alt.Chart(filtered_data11).encode(
    x='L7G',
    y=alt.Y("Jugador").sort('-x'),
    text='L7G',
    tooltip=['Jugador', 'Equipo', 'L7G', 'L7S', 'L7%']
)

plotfinal7M = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

#SHOTS TRIED
#Grafic 6mShots
chart = alt.Chart(filtered_data11).encode(
    x='L6S',
    y=alt.Y("Jugador").sort('-x'),
    text='L6S',
    tooltip=['Jugador', 'Equipo', 'L6G', 'L6S', 'L6%']
)

plotfinal6S = chart.mark_bar() + chart.mark_text(align='left', dx=2)

#Grafic 9mShots
chart1 = alt.Chart(filtered_data11).encode(
    x='L9S',
    y=alt.Y("Jugador").sort('-x'),
    text='L9S',
    tooltip=['Jugador', 'Equipo', 'L9G', 'L9S', 'L9%']
)

plotfinal9S = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

#Grafic 7mShots
chart2 = alt.Chart(filtered_data11).encode(
    x='L7S',
    y=alt.Y("Jugador").sort('-x'),
    text='L7S',
    tooltip=['Jugador', 'Equipo', 'L7G', 'L7S', 'L7%']
)

plotfinal7S = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

#SHOTS %
#Grafic 6m%
chart = alt.Chart(filtered_data11).encode(
    x='L6%',
    y=alt.Y("Jugador").sort('-x'),
    text='L6%',
    tooltip=['Jugador', 'Equipo', 'L6G', 'L6S', 'L6%']
)

plotfinal6p = chart.mark_bar() + chart.mark_text(align='left', dx=2)

#Grafic 9mShots
chart1 = alt.Chart(filtered_data11).encode(
    x='L9%',
    y=alt.Y("Jugador").sort('-x'),
    text='L9%',
    tooltip=['Jugador', 'Equipo', 'L9G', 'L9S', 'L9%']
)

plotfinal9p = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

#Grafic 7mShots
chart2 = alt.Chart(filtered_data11).encode(
    x='L7%',
    y=alt.Y("Jugador").sort('-x'),
    text='L7%',
    tooltip=['Jugador', 'Equipo', 'L7G', 'L7S', 'L7%']
)

plotfinal7p = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

#SHOTS CONTRAATAC
#gols
chart = alt.Chart(filtered_data11).encode(
    x='LCOG',
    y=alt.Y("Jugador").sort('-x'),
    text='LCOG',
    tooltip=['Jugador', 'Equipo', 'LCOG', 'LCOS', 'LCO%']
)

plotfinalLCOG = chart.mark_bar(color='orange') + chart.mark_text(align='left', dx=2)

#intents
chart1 = alt.Chart(filtered_data11).encode(
    x='LCOS',
    y=alt.Y("Jugador").sort('-x'),
    text='LCOS',
    tooltip=['Jugador', 'Equipo', 'LCOG', 'LCOS', 'LCO%']
)

plotfinalLCOS = chart1.mark_bar(color='orange') + chart1.mark_text(align='left', dx=2)

#percentatge

chart2 = alt.Chart(filtered_data11).encode(
    x='LCO%',
    y=alt.Y("Jugador").sort('-x'),
    text='LCO%',
    tooltip=['Jugador', 'Equipo', 'LCOG', 'LCOS', 'LCO%']
)

plotfinalLCOP = chart2.mark_bar(color='orange') + chart2.mark_text(align='left', dx=2)

tab1, tab4, tab7, tab2, tab5, tab8, tab3, tab6, tab9, tab10, tab11, tab12 = st.tabs(["L6G","L6S", "L6%", "L9G", "L9S", "L9%", "L7G", "L7S", "L7%", "LCOG", "LCOS", "LCO%"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(plotfinal6M, use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(plotfinal9M, use_container_width=True)
with tab3:
    st.altair_chart(plotfinal7M, use_container_width=True)
with tab4:
    st.altair_chart(plotfinal6S, use_container_width=True)
with tab5:
    st.altair_chart(plotfinal9S, use_container_width=True)
with tab6:
    st.altair_chart(plotfinal7S, use_container_width=True)
with tab7:
    st.altair_chart(plotfinal6p, use_container_width=True)
with tab8:
    st.altair_chart(plotfinal9p, use_container_width=True)
with tab9:
    st.altair_chart(plotfinal7p, use_container_width=True)
with tab10:
    st.altair_chart(plotfinalLCOG, use_container_width=True)
with tab11:
    st.altair_chart(plotfinalLCOS, use_container_width=True)
with tab12:
    st.altair_chart(plotfinalLCOP, use_container_width=True)

st.caption("🔎Fuente: Asobal")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**LxG** = Goles marcados según distancia")
expander.write("**LxS** = Número total de lanzamientos intentados según distancia")
expander.write("**Lx%** = Porcentaje de acierto en el lanzamiento según distancia")

st.divider()

st.subheader('📌Consulta todos los goleadores según **posición**:')

col1, col2 = st.columns(2)
 
with col1:

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

####-------------------------  PROVA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

with col2:

    st.markdown('Filtrado de datos según **lanzamientos intentados y su distancia**:')
    # Obtener los valores únicos de las variables L
    variables_L = ['L6', 'L7', 'L9', 'LCO']

    # Widget para seleccionar el tipo de gráfico
    selected_chart_type = st.radio('Seleccionar distancia de lanzamiento:', variables_L)

    # Añadir un slider solo para el tipo de gráfico seleccionado
    min_L = filtered_data22[f'{selected_chart_type}S'].min()
    max_L = filtered_data22[f'{selected_chart_type}S'].max()
    selected_L = st.slider(f'Seleccionar rango de lanzamientos intentados desde {selected_chart_type}S:', min_L, max_L, (min_L, max_L))

    # Filtrar los datos según el rango seleccionado en el slider
    filtered_data_L = filtered_data22[(filtered_data22[f'{selected_chart_type}S'] >= selected_L[0]) & (filtered_data22[f'{selected_chart_type}S'] <= selected_L[1])]

#####----------------------------


#Gràfics:

#Grafic 6m
chart = alt.Chart(filtered_data_L).encode(
    x='L6G',
    y=alt.Y("Jugador").sort('-x'),
    text='L6G',
    tooltip=['Jugador', 'Equipo', 'L6G', 'L6S', 'L6%']
)

plotfinal6M = chart.mark_bar() + chart.mark_text(align='left', dx=2)

#Grafic 9m
chart1 = alt.Chart(filtered_data_L).encode(
    x='L9G',
    y=alt.Y("Jugador").sort('-x'),
    text='L9G',
    tooltip=['Jugador', 'Equipo', 'L9G', 'L9S', 'L9%']
)

plotfinal9M = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

#Grafic 7m
chart2 = alt.Chart(filtered_data_L).encode(
    x='L7G',
    y=alt.Y("Jugador").sort('-x'),
    text='L7G',
    tooltip=['Jugador', 'Equipo', 'L7G', 'L7S', 'L7%']
)

plotfinal7M = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

#SHOTS TRIED
#Grafic 6mShots
chart = alt.Chart(filtered_data_L).encode(
    x='L6S',
    y=alt.Y("Jugador").sort('-x'),
    text='L6S',
    tooltip=['Jugador', 'Equipo', 'L6G', 'L6S', 'L6%']
)

plotfinal6S = chart.mark_bar() + chart.mark_text(align='left', dx=2)

#Grafic 9mShots
chart1 = alt.Chart(filtered_data_L).encode(
    x='L9S',
    y=alt.Y("Jugador").sort('-x'),
    text='L9S',
    tooltip=['Jugador', 'Equipo', 'L9G', 'L9S', 'L9%']
)

plotfinal9S = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

#Grafic 7mShots
chart2 = alt.Chart(filtered_data_L).encode(
    x='L7S',
    y=alt.Y("Jugador").sort('-x'),
    text='L7S',
    tooltip=['Jugador', 'Equipo', 'L7G', 'L7S', 'L7%']
)

plotfinal7S = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

#SHOTS %
#Grafic 6m%
chart = alt.Chart(filtered_data_L).encode(
    x='L6%',
    y=alt.Y("Jugador").sort('-x'),
    text='L6%',
    tooltip=['Jugador', 'Equipo', 'L6G', 'L6S', 'L6%']
)

plotfinal6p = chart.mark_bar() + chart.mark_text(align='left', dx=2)

#Grafic 9mShots
chart1 = alt.Chart(filtered_data_L).encode(
    x='L9%',
    y=alt.Y("Jugador").sort('-x'),
    text='L9%',
    tooltip=['Jugador', 'Equipo', 'L9G', 'L9S', 'L9%']
)

plotfinal9p = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

#Grafic 7mShots
chart2 = alt.Chart(filtered_data_L).encode(
    x='L7%',
    y=alt.Y("Jugador").sort('-x'),
    text='L7%',
    tooltip=['Jugador', 'Equipo', 'L7G', 'L7S', 'L7%']
)

plotfinal7p = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

#SHOTS CONTRAATAC
#gols
chart = alt.Chart(filtered_data_L).encode(
    x='LCOG',
    y=alt.Y("Jugador").sort('-x'),
    text='LCOG',
    tooltip=['Jugador', 'Equipo', 'LCOG', 'LCOS', 'LCO%']
)

plotfinalLCOG = chart.mark_bar(color='orange') + chart.mark_text(align='left', dx=2)

#intents
chart1 = alt.Chart(filtered_data_L).encode(
    x='LCOS',
    y=alt.Y("Jugador").sort('-x'),
    text='LCOS',
    tooltip=['Jugador', 'Equipo', 'LCOG', 'LCOS', 'LCO%']
)

plotfinalLCOS = chart1.mark_bar(color='orange') + chart1.mark_text(align='left', dx=2)

#percentatge

chart2 = alt.Chart(filtered_data_L).encode(
    x='LCO%',
    y=alt.Y("Jugador").sort('-x'),
    text='LCO%',
    tooltip=['Jugador', 'Equipo', 'LCOG', 'LCOS', 'LCO%']
)

plotfinalLCOP = chart2.mark_bar(color='orange') + chart2.mark_text(align='left', dx=2)

tab1, tab4, tab7, tab2, tab5, tab8, tab3, tab6, tab9, tab10, tab11, tab12 = st.tabs(["L6G","L6S", "L6%", "L9G", "L9S", "L9%", "L7G", "L7S", "L7%", "LCOG", "LCOS", "LCO%"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(plotfinal6M, use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(plotfinal9M, use_container_width=True)
with tab3:
    st.altair_chart(plotfinal7M, use_container_width=True)
with tab4:
    st.altair_chart(plotfinal6S, use_container_width=True)
with tab5:
    st.altair_chart(plotfinal9S, use_container_width=True)
with tab6:
    st.altair_chart(plotfinal7S, use_container_width=True)
with tab7:
    st.altair_chart(plotfinal6p, use_container_width=True)
with tab8:
    st.altair_chart(plotfinal9p, use_container_width=True)
with tab9:
    st.altair_chart(plotfinal7p, use_container_width=True)
with tab10:
    st.altair_chart(plotfinalLCOG, use_container_width=True)
with tab11:
    st.altair_chart(plotfinalLCOS, use_container_width=True)
with tab12:
    st.altair_chart(plotfinalLCOP, use_container_width=True)

#----------------
st.caption("🔎Fuente: Asobal")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**LxG** = Goles marcados según distancia")
expander.write("**LxS** = Número total de lanzamientos intentados según distancia")
expander.write("**Lx%** = Porcentaje de acierto en el lanzamiento según distancia")


#-------------------------------------

st.divider()

dfequipos = pd.read_excel("DatasetEquiposAsobal2324.xlsx")
dfequipos1 = pd.read_excel("DatasetEquiposAsobal2223.xlsx")

st.subheader("📌Consulta los datos sobre el porcentaje de acierto en el lanzamiento de equipo, según la distancia de cada uno.")

# Obtener una lista de temporadas únicas de ambos DataFrames
temporadas3 = pd.concat([dfequipos['Temporada'], dfequipos1['Temporada']]).unique()

# Crear el select box para la temporada
selected_temporada3 = st.selectbox('Escoge una temporada:', temporadas3, key="selectbox3")

# Filtrar los datos según la temporada seleccionada desde ambos DataFrames
filtered_data3 = pd.concat([dfequipos[dfequipos['Temporada'] == selected_temporada3], dfequipos1[dfequipos1['Temporada'] == selected_temporada3]]).round(2)

#Grafic 6m
chart = alt.Chart(filtered_data3).encode(
    x='L6PTeam',
    y=alt.Y("Equipo").sort('-x'),
    text='L6PTeam',
    tooltip=['Equipo', 'L6GTeam', 'L6STeam', 'L6PTeam']
)

plotfinal6Per = chart.mark_bar() + chart.mark_text(align='left', dx=2)

#Grafic 9m
chart1 = alt.Chart(filtered_data3).encode(
    x='L9PTeam',
    y=alt.Y("Equipo").sort('-x'),
    text='L9PTeam',
    tooltip=['Equipo', 'L9GTeam', 'L9STeam', 'L9PTeam']
)

plotfinal9Per = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

#Grafic 7m
chart2 = alt.Chart(filtered_data3).encode(
    x='L7PTeam',
    y=alt.Y("Equipo").sort('-x'),
    text='L7PTeam',
    tooltip=['Equipo', 'L7GTeam', 'L7STeam', 'L7PTeam']
)

plotfinal7Per = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

#Grafic Contra
chart3 = alt.Chart(filtered_data3).encode(
    x='LCPTeam',
    y=alt.Y("Equipo").sort('-x'),
    text='LCPTeam',
    tooltip=['Equipo', 'LCGTeam', 'LCSTeam', 'LCPTeam']
)

plotfinalCPer = chart3.mark_bar(color='orange') + chart3.mark_text(align='left', dx=2)

tab21, tab22, tab23, tab24 = st.tabs(["L6PTeam","L9PTeam", "L7PTeam", "LCPTeam"])
with tab21:
    st.altair_chart(plotfinal6Per, use_container_width=True)
with tab22:
    st.altair_chart(plotfinal9Per, use_container_width=True)
with tab23:
    st.altair_chart(plotfinal7Per, use_container_width=True)
with tab24:
    st.altair_chart(plotfinalCPer, use_container_width=True)

st.caption("🔎Fuente: Asobal")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**LxPTeam** = Porcentaje de acierto en el lanzamiento del equipo según distancia: 6 = 6 metros, 9 = 9 metros, 7 = 7 metros/penalti y C = Contraataque.")
