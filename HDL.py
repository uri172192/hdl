import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="HDL", page_icon="favicon-32x32.png", layout="wide")


def main_page():

    import streamlit as st
    import pandas as pd
    import numpy as np
    from PIL import Image

    #-----------------------------------------------

    image = Image.open('HDL-blanc.png')
    st.image(image) 


    st.subheader('📌Descripción HDL')
    st.write('📢**Handball Data Lab** se presenta como una aplicación destinada al desarrollo y democratización del análisis de datos en balonmano. La finalidad es ayudar a los usarios a **disfrutar, comprender y compartir los datos sobre el balonmano**.')
        
    st.divider()
    st.subheader("📌Contenidos HDL")
    st.write("🏐**Scorers**: visualiza los goleadores según equipo y posición")
    st.write("🏹**Shooting Distances**: explora los máximos anotadores según la distancia del lanzamiento")
    st.write("🎯**Players Shooting Performance**: escoge 2 jugadores y compara su rendimiento en el lanzamiento")
    st.write("📋**Efficiency Snapshot Asobal**: conoce como han rendido los equipos durante la temporada")
    st.write("🕵️**Shooting Similiraty**: descubre los jugadores similares entre si según su eficacia en el lanzamiento")
    st.write("🗂️**Data Consulting**: consulta los datos de los que disponemos sobre cada equipo en materia de lanzamientos")
    st.divider()

def page2():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import altair as alt
    from vega_datasets import data
    import matplotlib.colors as mcolors


    # Configura el título de la página i favicon
    st.title('🏐Scorers')
    st.header('🎯Goleadores Asobal')
    st.subheader('📌Consulta todos los goleadores según **equipo**:')

    df = pd.read_excel("DatasetJugadoresAsobal.xlsx")
    df1 = pd.read_excel("DataJugadoresAsobal2324.xlsx")


    # Obtener una lista de temporadas únicas de ambos DataFrames
    temporadas = pd.concat([df1['Temporada'], df['Temporada']]).unique()

    # Crear el select box para la temporada
    selected_temporada1 = st.selectbox('Escoge una temporada:', temporadas, key="selectbox1")

    # Filtrar los datos según la temporada seleccionada desde ambos DataFrames
    filtered_data1 = df[df['Temporada'] == selected_temporada1].append(df1[df1['Temporada'] == selected_temporada1])

    # Obtener una lista de equipos únicos para la temporada seleccionada
    equipos_temporada = filtered_data1['Equipo'].unique()

    # Crear el select box para el equipo
    selected_equipo = st.selectbox('Escoge un equipo:', equipos_temporada)

    # Filtrar los datos nuevamente para mostrar solo el equipo seleccionado
    filtered_data11 = filtered_data1[filtered_data1['Equipo'] == selected_equipo]

    # Generar colores únicos para cada equipo (combina múltiples escalas de colores)
    team_colors1 = dict(zip(equipos_temporada[:8], mcolors.TABLEAU_COLORS.values()))
    team_colors2 = dict(zip(equipos_temporada[8:16], mcolors.XKCD_COLORS.values()))
    team_colors = {**team_colors1, **team_colors2}

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
    filtered_data2 = df[df['Temporada'] == selected_temporada2].append(df1[df1['Temporada'] == selected_temporada2])

    # Obtener una lista de equipos únicos para la temporada seleccionada
    equipos_temporada2 = filtered_data2['Equipo'].unique()

    # Obtener una lista de posiciones únicos para la temporada seleccionada
    pos_temporada = filtered_data2['Posicion'].unique()

    # Crear el select box para la posicion
    selected_pos = st.selectbox('Escoge una posicion:', pos_temporada)

    # Filtrar los datos nuevamente para mostrar solo  seleccionado
    filtered_data22 = filtered_data2[filtered_data2['Posicion'] == selected_pos]

    # Generar colores únicos para cada equipo (combina múltiples escalas de colores)
    team_colors1 = dict(zip(equipos_temporada2[:8], mcolors.TABLEAU_COLORS.values()))
    team_colors2 = dict(zip(equipos_temporada2[8:16], mcolors.XKCD_COLORS.values()))
    team_colors = {**team_colors1, **team_colors2}

    ## Graph
    graph = alt.Chart(filtered_data22).encode(
        x='ToG',
        y=alt.Y("Jugador").sort('-x'),
        text='ToG',
        tooltip=['Jugador', 'Posicion', 'Equipo', 'ToG', 'ToS', 'To%'],
        color=alt.Color("Equipo", scale=alt.Scale(domain=list(team_colors.keys()), range=list(team_colors.values())))
    )
    plotfinalpos = graph.mark_bar() + graph.mark_text(align='left', dx=2)
    st.altair_chart(plotfinalpos, use_container_width=True)

    st.caption("🔎Fuente: Asobal")
    expander = st.expander(" ➕ **LEGEND**")
    expander.write("**ToG** = Total Goles Marcados")
    expander.write("**ToS** = Total Lanzamientos Intentados")
    expander.write("**To%** = Porcentaje de acierto en el lanzamiento")

def page3():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import altair as alt
    from vega_datasets import data

    # Configura el título de la página i favicon
    st.title('🏹Shooting Distances')

    df = pd.read_excel("DatasetJugadoresAsobal.xlsx")
    df1 = pd.read_excel("DataJugadoresAsobal2324.xlsx")

    st.subheader("📌Consulta los datos sobre lanzamientos intentados, anotados y el porcentaje correspondiente a cada jugador, según la distancia del lanzamiento, filtrando por equipo.")

    # Obtener una lista de temporadas únicas de ambos DataFrames
    temporadas = pd.concat([df1['Temporada'], df['Temporada']]).unique()

    # Crear el select box para la temporada
    selected_temporada1 = st.selectbox('Escoge una temporada:', temporadas, key="selectbox1")

    # Filtrar los datos según la temporada seleccionada desde ambos DataFrames
    filtered_data1 = df[df['Temporada'] == selected_temporada1].append(df1[df1['Temporada'] == selected_temporada1])

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

    #Intents
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
        filtered_data2 = df[df['Temporada'] == selected_temporada2].append(df1[df1['Temporada'] == selected_temporada2])

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

    dfequipos = pd.read_excel("DatasetEquiposAsobal.xlsx")


    st.subheader("📌Consulta los datos sobre el porcentaje de acierto en el lanzamiento de equipo, según la distancia de cada uno.")

    #Grafic 6m
    chart = alt.Chart(dfequipos).encode(
        x='L6PTeam',
        y=alt.Y("Equipo").sort('-x'),
        text='L6PTeam',
        tooltip=['Equipo', 'L6GTeam', 'L6STeam', 'L6PTeam']
    )

    plotfinal6Per = chart.mark_bar() + chart.mark_text(align='left', dx=2)

    #Grafic 9m
    chart1 = alt.Chart(dfequipos).encode(
        x='L9PTeam',
        y=alt.Y("Equipo").sort('-x'),
        text='L9PTeam',
        tooltip=['Equipo', 'L9GTeam', 'L9STeam', 'L9PTeam']
    )

    plotfinal9Per = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

    #Grafic 7m
    chart2 = alt.Chart(dfequipos).encode(
        x='L7PTeam',
        y=alt.Y("Equipo").sort('-x'),
        text='L7PTeam',
        tooltip=['Equipo', 'L7GTeam', 'L7STeam', 'L7PTeam']
    )

    plotfinal7Per = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

    #Grafic Contra
    chart3 = alt.Chart(dfequipos).encode(
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


def page4():
    
    import pandas as pd
    import streamlit as st
    import plotly.graph_objects as go

    # Cargar el DataFrame desde el archivo Excel
    df = pd.read_excel("DatasetJugadoresAsobal.xlsx")
    df1 = pd.read_excel("DataJugadoresAsobal2324.xlsx")


    # Título de la página
    st.title('🎯Players Shooting Performance')

    # Título de la sección
    st.header('📌Comparador de Jugadores')

    # Obtener una lista de temporadas únicas de ambos DataFrames
    temporadas = pd.concat([df1['Temporada'], df['Temporada']]).unique()

    # Crear el select box para la temporada
    selected_temporada1 = st.selectbox('Escoge una temporada:', temporadas, key="selectbox1")

    # Filtrar los datos según la temporada seleccionada desde ambos DataFrames
    filtered_data1 = df[df['Temporada'] == selected_temporada1].append(df1[df1['Temporada'] == selected_temporada1])

    # Generar una clave única para el widget multiselect
    player_selection_key = "player_selection"
    selected_players = st.multiselect('Selecciona dos jugadores:', filtered_data1['Jugador'], default=['Dika Mem', 'Antonio García'], key=player_selection_key)

    # Validación para asegurarse de que se seleccionen exactamente dos jugadores
    if len(selected_players) == 2:
        # Filtrar los datos según los jugadores seleccionados
        filtered_data = filtered_data1[filtered_data1['Jugador'].isin(selected_players)]

        # Crear el gráfico de radar
        categories = ['L6G', 'L6S', 'L7G', 'L7S', 'L9G', 'L9S', 'LCOG', 'LCOS']

        fig = go.Figure()

        # Lista de colores personalizados para cada jugador
        colors = ['blue', 'green']

        for i, player in enumerate(selected_players):
            values = filtered_data[filtered_data['Jugador'] == player][categories].values[0]
            values = values.tolist()
            values.append(values[0])  # Agregar el primer valor al final para cerrar el polígono

            # Cambiar colores para cada jugador
            line_color = colors[i]  # Color de la línea
            fill_color = f'rgba(0, 0, 255, 0.2)'  # Color del área rellena con transparencia

            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories + [categories[0]],
                fill='toself',
                name=player,
                line=dict(color=line_color, width=2),
                fillcolor=fill_color
            ))

        # Ajustar el tamaño del gráfico directamente desde Plotly
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 180],
                    tickvals=[50, 100, 150],
                    ticktext=["50", "100", "150"],
                    ticks="outside",
                ),
            ),
            showlegend=True,
            title='Lanzamientos Marcados/Intentados según Distancias',
            width=800,  # Ajusta el ancho del gráfico
            height=600  # Ajusta la altura del gráfico
        )

        st.plotly_chart(fig)
    else:
        st.warning('Selecciona exactamente dos jugadores para poder comparar.')

    # ... Código previo ...

    # Crear una tabla con los valores de cada variable por cada jugador
    table_data = []
    for player in selected_players:
        values = filtered_data[filtered_data['Jugador'] == player][categories].values[0]
        table_data.append([player] + values.tolist())

    # Crear un DataFrame para la tabla
    table_df = pd.DataFrame(table_data, columns=['Jugador'] + categories)

    # Identificar las celdas con los valores más altos
    high_value_style = 'background-color: lawngreen;'  # Estilo CSS para resaltar las celdas

    for col in categories:
        max_value = table_df[col].max()
        table_df[col] = table_df.apply(
            lambda row: f"{row[col]} ⬆️" if row[col] == max_value else row[col],
            axis=1
        )

    # Mostrar la tabla con estilos CSS
    st.markdown(
        table_df.style.applymap(lambda x: high_value_style if '⬆️' in str(x) else '', subset=pd.IndexSlice[:, categories]).render(),
        unsafe_allow_html=True
    )

    # Resto del código ...

    st.divider()
    st.caption("🔎Fuente: Asobal")
    expander = st.expander(" ➕ **LEGEND**")
    expander.write("**LxG** = Goles marcados según distancia")
    expander.write("**LxS** = Número total de lanzamientos intentados según distancia")

    st.divider()

    # Validación para asegurarse de que se seleccionen exactamente dos jugadores
    if len(selected_players) == 2:
        # Filtrar los datos según los jugadores seleccionados
        filtered_data = filtered_data1[filtered_data1['Jugador'].isin(selected_players)]

        # Crear el gráfico de radar
        categories = ['L6%', 'L7%', 'L9%', 'LCO%']

        fig = go.Figure()

        # Lista de colores personalizados para cada jugador
        colors = ['blue', 'green']

        for i, player in enumerate(selected_players):
            values = filtered_data[filtered_data['Jugador'] == player][categories].values[0]
            values = values.tolist()
            values.append(values[0])  # Agregar el primer valor al final para cerrar el polígono

            # Cambiar colores para cada jugador
            line_color = colors[i]  # Color de la línea
            fill_color = f'rgba(0, 0, 255, 0.2)'  # Color del área rellena con transparencia

            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories + [categories[0]],
                fill='toself',
                name=player,
                line=dict(color=line_color, width=2),
                fillcolor=fill_color
            ))

        # Ajustar el tamaño del gráfico directamente desde Plotly
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1],
                    tickvals=[0, 0.250, 0.500, 0.750],
                    ticktext=["0", "0.250", "0.500", "0.750"],
                    ticks="outside",
                ),
            ),
            showlegend=True,
            title='Porcentajes en el Lanzamiento según Distancias',
            width=800,  # Ajusta el ancho del gráfico
            height=600  # Ajusta la altura del gráfico
        )

        st.plotly_chart(fig)
    else:
        st.warning('Selecciona exactamente dos jugadores para poder comparar.')

    # Crear una tabla con los valores de cada variable por cada jugador
    table_data = []
    for player in selected_players:
        values = filtered_data[filtered_data['Jugador'] == player][categories].values[0]
        table_data.append([player] + values.tolist())

    # Crear un DataFrame para la tabla
    table_df = pd.DataFrame(table_data, columns=['Jugador'] + categories)

    # Formatear los valores con dos decimales
    table_df[categories] = table_df[categories].applymap("{:.2f}".format)

    # Identificar las celdas con los valores más altos
    high_value_style = 'background-color: lawngreen;'  # Estilo CSS para resaltar las celdas

    for col in categories:
        max_value = table_df[col].max()
        table_df[col] = table_df.apply(
            lambda row: f"{row[col]} ⬆️" if row[col] == max_value else row[col],
            axis=1
        )

    # Mostrar la tabla con estilos CSS
    st.markdown(
        table_df.style.applymap(lambda x: high_value_style if '⬆️' in str(x) else '', subset=pd.IndexSlice[:, categories]).render(),
        unsafe_allow_html=True
    )

    st.divider()
    st.caption("🔎Fuente: Asobal")
    expander = st.expander(" ➕ **LEGEND**")
    expander.write("**Lx%** = Porcentaje de acierto en el lanzamiento según distancia")


def page5():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import altair as alt
    from vega_datasets import data

    # Configura el título de la página i favicon
    st.title('🕵️Similitud Jugadores')
    st.subheader('📌Descubre los jugadores más similares entre si respecto a su eficacia en el lanzamiento en la Liga Asobal.')
    #-------------------------------------
    df = pd.read_excel('DatasetJugadoresAsobal.xlsx')
    df1 = pd.read_excel("DataJugadoresAsobal2324.xlsx")
    #-------------------------------------
    #-------------------------------------


    # Librerías

    import pandas as pd
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    import numpy as np

    from matplotlib import pyplot as plt

    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    import warnings
    warnings.filterwarnings(action="ignore")

    #---------------------------------------------------------------------------------------------------------------------------------

    #Temporada Actual:
    #Cambiar orden posicion metricas object:
    st.write('Temporada 23-24')
    df1.insert(1,'Jugador', df1.pop("Jugador"))
    df1.insert(2,'Posicion', df1.pop("Posicion"))

    #Eliminar columnas:
    df1.drop(columns='Nº', inplace=True)
    df1.drop(columns='Equipo', inplace=True)
    df1.drop(columns='Posicion', inplace=True)
    df1.drop(columns='Temporada', inplace=True)


    X, y = df1.iloc[:, 1:len(df1.columns)].values, df1.iloc[:, 0].values

    X_std = StandardScaler().fit_transform(X)

    pca = PCA(n_components = len(df1.columns)-1)
    pca.fit(X_std)
    X_pca = pca.transform(X_std)

    print("Shape x_PCA: ", X_pca.shape)
    expl = pca.explained_variance_ratio_

    for x in range(0, len(df1.columns), 2):
        print("Explained Variance: " + str(x) + " components:", sum(expl[0:x]))

    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('Dimensions')
    plt.ylabel('Explained Variance')
    plt.show()

    N_COMP = 8
    columns = []

    for col in range(1, N_COMP+1, 1):
        columns.append("PCA" + str(col))

    df1_pca_resultado = pd.DataFrame(data=X_pca[:,0:N_COMP], columns=columns, index = y)

    df1_pca_resultado.head()

    corr_matrix = df1_pca_resultado.T.corr(method='pearson')

    ## Conseguir lista de equipos
    Players = df1['Jugador'].unique()

    ## Create the select box
    selected_player = st.selectbox('Escoge jugador:', Players)

    ## Filter the data
    filtered_data = df1[df1['Jugador'] == selected_player]




    def GetSimilarPlayers(Jugador, numPlayers, corr_matrix):

        SimPlayers = pd.DataFrame(columns = ['Jugador', 'Similar Player', 'Correlation Factor'])

        i = 0
        for i in range(0, numPlayers):
            row = corr_matrix.loc[corr_matrix.index == Jugador].squeeze()

            SimPlayers.at[i, 'Jugador'] = Jugador
            SimPlayers.at[i, 'Similar Player'] = row.nlargest(i+2).sort_values(ascending=True).index[0]
            SimPlayers.at[i, 'Correlation Factor'] = row.nlargest(i+2).sort_values(ascending=True)[0]

            i = i+1

        return SimPlayers

    Jugador = 'Faruk Yusuf'
    NumPlayers = 5

    # Check if a player is selected
    if selected_player:
        # Call the function with the selected player
        df_correlatedPlayers1 = GetSimilarPlayers(selected_player, NumPlayers, corr_matrix)

        # Display the resulting DataFrame
        st.write(df_correlatedPlayers1)

    #---------------------------------------------------------------------------------------------------------------------------------

    #Temporada Anterior:
    st.write('Temporada 22-23')
    #Cambiar orden posicion metricas object:
    df.insert(1,'Jugador', df.pop("Jugador"))
    df.insert(2,'Posicion', df.pop("Posicion"))

    #Eliminar columnas:
    df.drop(columns='Nº', inplace=True)
    df.drop(columns='Equipo', inplace=True)
    df.drop(columns='Posicion', inplace=True)
    df.drop(columns='Temporada', inplace=True)


    X, y = df.iloc[:, 1:len(df.columns)].values, df.iloc[:, 0].values

    X_std = StandardScaler().fit_transform(X)

    pca = PCA(n_components = len(df.columns)-1)
    pca.fit(X_std)
    X_pca = pca.transform(X_std)

    print("Shape x_PCA: ", X_pca.shape)
    expl = pca.explained_variance_ratio_

    for x in range(0, len(df.columns), 2):
        print("Explained Variance: " + str(x) + " components:", sum(expl[0:x]))

    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('Dimensions')
    plt.ylabel('Explained Variance')
    plt.show()

    N_COMP = 8
    columns = []

    for col in range(1, N_COMP+1, 1):
        columns.append("PCA" + str(col))

    df_pca_resultado = pd.DataFrame(data=X_pca[:,0:N_COMP], columns=columns, index = y)

    df_pca_resultado.head()

    corr_matrix = df_pca_resultado.T.corr(method='pearson')

    ## Conseguir lista de equipos
    Players = df['Jugador'].unique()

    ## Create the select box
    selected_player = st.selectbox('Escoge jugador:', Players)

    ## Filter the data
    filtered_data = df[df['Jugador'] == selected_player]




    def GetSimilarPlayers(Jugador, numPlayers, corr_matrix):

        SimPlayers = pd.DataFrame(columns = ['Jugador', 'Similar Player', 'Correlation Factor'])

        i = 0
        for i in range(0, numPlayers):
            row = corr_matrix.loc[corr_matrix.index == Jugador].squeeze()

            SimPlayers.at[i, 'Jugador'] = Jugador
            SimPlayers.at[i, 'Similar Player'] = row.nlargest(i+2).sort_values(ascending=True).index[0]
            SimPlayers.at[i, 'Correlation Factor'] = row.nlargest(i+2).sort_values(ascending=True)[0]

            i = i+1

        return SimPlayers

    Jugador = 'Faruk Yusuf'
    NumPlayers = 5

    # Check if a player is selected
    if selected_player:
        # Call the function with the selected player
        df_correlatedPlayers = GetSimilarPlayers(selected_player, NumPlayers, corr_matrix)

        # Display the resulting DataFrame
        st.write(df_correlatedPlayers)

    #df_correlatedPlayers = GetSimilarPlayers(Jugador, NumPlayers, corr_matrix)

    #df_correlatedPlayers


def page6():
    import streamlit as st
    import pandas as pd

    # Configura el título de la página i favicon
    st.title("🗂️Data Consulting")

    st.subheader('📌Players Data')
    st.write('Consulta datos jugadores Asobal:')
    ## Df Load
    df = pd.read_excel("DatasetJugadoresAsobal.xlsx")
    df1 = pd.read_excel("DataJugadoresAsobal2324.xlsx")


    # Obtener una lista de temporadas únicas de ambos DataFrames
    temporadas = pd.concat([df1['Temporada'], df['Temporada']]).unique()

    # Crear el select box para la temporada
    selected_temporada1 = st.selectbox('Escoge una temporada:', temporadas, key="selectbox1")

    # Filtrar los datos según la temporada seleccionada desde ambos DataFrames
    filtered_data1 = df[df['Temporada'] == selected_temporada1].append(df1[df1['Temporada'] == selected_temporada1])

    # Obtener una lista de equipos únicos para la temporada seleccionada
    equipos_temporada = filtered_data1['Equipo'].unique()

    # Crear el select box para el equipo
    selected_equipo = st.selectbox('Escoge un equipo:', equipos_temporada)

    # Filtrar los datos nuevamente para mostrar solo el equipo seleccionado
    filtered_data11 = filtered_data1[filtered_data1['Equipo'] == selected_equipo]

    
    ## Display the filtered data
    st.write(filtered_data11)

    st.caption("🔎Fuente: Asobal")

    #Legend
    expander = st.expander("➕ **LEGEND**")
    expander.write("**Equipo** = Nombre del equipo")
    expander.write("**Nº** = Dorsal del jugador")
    expander.write("**Posicion** = Posición de juego del jugador")
    expander.write("**ToG** = Total Goles Marcados")
    expander.write("**ToS** = Total Lanzamientos Intentados")
    expander.write("**To%** = Porcentaje total de acierto en el lanzamiento")
    expander.write("**L6 (Lanzamientos de 6 metros), L9 (Lanzamientos de 9 metros), L7 (Penaltis), LCO (Lanzamientos de contraataque)** = Siguen el mismo proceso de goles, lanzamientos intentados y porcentaje de acierto según cada distancia o tipo de lanzamiento.")

    st.divider()

    st.subheader('📌Teams Data')
    st.write('Consulta datos equipos Asobal:')
    dfteams = pd.read_excel("DatasetEquiposAsobal.xlsx")
    dfteams1 = pd.read_excel("DatasetEquiposAsobal2324.xlsx")

    # Obtener una lista de temporadas únicas de ambos DataFrames
    temporadas = pd.concat([dfteams1['Temporada'], dfteams['Temporada']]).unique()

    # Crear el select box para la temporada
    selected_temporada1 = st.selectbox('Escoge una temporada:', temporadas, key="selectbox2")

    # Filtrar los datos según la temporada seleccionada desde ambos DataFrames
    filtered_data1 = dfteams[dfteams['Temporada'] == selected_temporada1].append(dfteams1[dfteams1['Temporada'] == selected_temporada1])
    

    def round_table_values(df):
        # Aplica redondeo a 2 decimales para todas las celdas del DataFrame
        rounded_df = filtered_data1.round(2)
        return rounded_df
    df_rounded = round_table_values(filtered_data1)
    st.write(df_rounded)
    st.caption("🔎Fuente: Asobal")

    expander = st.expander(" ➕ **LEGEND**")
    expander.write("**Equipo** = Nombre del equipo")
    expander.write("**PJ** = Partidos Jugados")
    expander.write("**GF** = Goles a favor")
    expander.write("**GC** = Goles en contra")
    expander.write("**Pos** = Número total de posesiones en tota la temporada")
    expander.write("**DefRt** = Defensive Rating, eficiencia defensiva")
    expander.write("**DefRt** = Defensive Rating, eficiencia defensiva")
    expander.write("**OffRt** = Offensive Rating, eficiencia ofensiva")
    expander.write("**NetRt** = Net Rating, diferencia entre eficiencia ofensiva y defensiva")
    expander.write("**Pace** = ritmo de juego, número de posesiones por partido")
    expander.write("**LxGTeam** = Nombre goles anotados por un equipo desde una distancia concreta durante la temproada")
    expander.write("**LxSTeam** = Nombre lanzamientos intentados por un equipo desde una distancia concreta durante la temproada")
    expander.write("**LxPTeam** = Porcentaje de acierto en el lanzamiento de un equipo desde una distancia concreta durante la temproada")




#MENU PAGES PLAYERS
page_names_to_funcs = {
    "🤾‍♂️📊HDL": main_page,
    "🏐Scorers": page2,
    "🏹Shooting Distances": page3,
    "🎯Players Shooting Performance": page4,
    "🕵️Shooting Similarity": page5,
    "🗂️Data Consulting": page6,
}


#------------------------------------------------------------------------------------------------------------------------------
#GOALKEEPERS

def gk():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import altair as alt
    from vega_datasets import data
    import matplotlib.colors as mcolors

    st.title('​🧱​Saves')
    st.header('🥅Porteros Asobal')
    st.subheader('📌Consulta el rendimiento global de los porteros según **equipo**:')

    df = pd.read_excel("asobalgk2324.xlsx")
    ##Conseguir lista de equipos
    Portero = df['Equipo'].unique()

    ## Create the select box
    selected_gk = st.selectbox('Escoge equipo:', Portero)

    ## Filter the data
    filtered_data = df[df['Equipo'] == selected_gk]

    ## Graph
    graph = alt.Chart(filtered_data).encode(
        x='ToP',
        y=alt.Y("Jugador").sort('-x'),
        text='ToP',
        tooltip=['Jugador', 'Equipo', 'ToP', 'ToL', 'To%'],
        color=alt.Color("Equipo")
    )
    plotfinal = graph.mark_bar() + graph.mark_text(align='left', dx=2)
    st.altair_chart(plotfinal, use_container_width=True)

    st.caption("🔎Fuente: Asobal")
    expander = st.expander(" ➕ **LEGEND**")
    expander.write("**ToP** = Total Paradas Realizadas")
    expander.write("**ToL** = Total Lanzamientos Recibidos")
    expander.write("**To%** = Porcentaje de paradas")

def gk1():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import altair as alt
    from vega_datasets import data
    import matplotlib.colors as mcolors


    st.title('​🏹​Saves Distances')
    st.header('🥅Porteros Asobal')
    st.subheader('📌Consulta el rendimiento global de los porteros según distancia del lanzamiento:')

    df = pd.read_excel("asobalgk2324.xlsx")
    ##Conseguir lista de equipos
    Portero = df['Equipo'].unique()

    ## Create the select box
    selected_gk = st.selectbox('Escoge equipo:', Portero)

    ## Filter the data
    filtered_data = df[df['Equipo'] == selected_gk]

    
    #Grafic 6m
    chart = alt.Chart(filtered_data).encode(
        x='L6P',
        y=alt.Y("Jugador").sort('-x'),
        text='L6P',
        tooltip=['Jugador', 'Equipo', 'L6P', 'L6M', 'L6%']
    )

    plotfinal6M = chart.mark_bar() + chart.mark_text(align='left', dx=2)

    #Grafic 6m Shots
    chart = alt.Chart(filtered_data).encode(
        x='L6M',
        y=alt.Y("Jugador").sort('-x'),
        text='L6M',
        tooltip=['Jugador', 'Equipo', 'L6P', 'L6M', 'L6%']
    )

    plotfinal6MS = chart.mark_bar() + chart.mark_text(align='left', dx=2)

    #Grafic 6m %
    chart = alt.Chart(filtered_data).encode(
        x='L6%',
        y=alt.Y("Jugador").sort('-x'),
        text='L6%',
        tooltip=['Jugador', 'Equipo', 'L6P', 'L6M', 'L6%']
    )

    plotfinal6MP = chart.mark_bar() + chart.mark_text(align='left', dx=2)

    #Grafic 9m
    chart1 = alt.Chart(filtered_data).encode(
        x='L9P',
        y=alt.Y("Jugador").sort('-x'),
        text='L9P',
        tooltip=['Jugador', 'Equipo', 'L9P', 'L9M', 'L9%']
    )

    plotfinal9M = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

    #Grafic 9m Shots
    chart1 = alt.Chart(filtered_data).encode(
        x='L9M',
        y=alt.Y("Jugador").sort('-x'),
        text='L9M',
        tooltip=['Jugador', 'Equipo', 'L9P', 'L9M', 'L9%']
    )

    plotfinal9MS = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

    #Grafic 9m %
    chart1 = alt.Chart(filtered_data).encode(
        x='L9%',
        y=alt.Y("Jugador").sort('-x'),
        text='L9%',
        tooltip=['Jugador', 'Equipo', 'L9P', 'L9M', 'L9%']
    )

    plotfinal9MP = chart1.mark_bar(color='firebrick') + chart1.mark_text(align='left', dx=2)

    #Grafic 7m
    chart2 = alt.Chart(filtered_data).encode(
        x='L7P',
        y=alt.Y("Jugador").sort('-x'),
        text='L7P',
        tooltip=['Jugador', 'Equipo', 'L7P', 'L7M', 'L7%']
    )

    plotfinal7M = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

    #Grafic 7m Shots
    chart2 = alt.Chart(filtered_data).encode(
        x='L7M',
        y=alt.Y("Jugador").sort('-x'),
        text='L7M',
        tooltip=['Jugador', 'Equipo', 'L7P', 'L7M', 'L7%']
    )

    plotfinal7MS = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

    #Grafic 7m %
    chart2 = alt.Chart(filtered_data).encode(
        x='L7%',
        y=alt.Y("Jugador").sort('-x'),
        text='L7%',
        tooltip=['Jugador', 'Equipo', 'L7P', 'L7M', 'L7%']
    )

    plotfinal7MP = chart2.mark_bar(color='green') + chart2.mark_text(align='left', dx=2)

    #Grafic Contraatac
    chart = alt.Chart(filtered_data).encode(
        x='LCOP',
        y=alt.Y("Jugador").sort('-x'),
        text='LCOP',
        tooltip=['Jugador', 'Equipo', 'LCOP', 'LCO', 'LCO%']
    )

    plotfinalLCOP = chart.mark_bar(color='orange') + chart.mark_text(align='left', dx=2)

    #Grafic Contraatac Shots
    chart1 = alt.Chart(filtered_data).encode(
        x='LCO',
        y=alt.Y("Jugador").sort('-x'),
        text='LCO',
        tooltip=['Jugador', 'Equipo', 'LCOP', 'LCO', 'LCO%']
    )

    plotfinalLCOS = chart1.mark_bar(color='orange') + chart1.mark_text(align='left', dx=2)

    #Grafic Contraatac %
    chart2 = alt.Chart(filtered_data).encode(
        x='LCO%',
        y=alt.Y("Jugador").sort('-x'),
        text='LCO%',
        tooltip=['Jugador', 'Equipo', 'LCOP', 'LCO', 'LCO%']
    )

    plotfinalLCOPP = chart2.mark_bar(color='orange') + chart2.mark_text(align='left', dx=2)

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(["L6P","L6S", "L6%", "L9P", "L9S", "L9%", "L7P", "L7S", "L7%", "LCOP", "LCOS", "LCO%"])
    with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
        st.altair_chart(plotfinal6M, use_container_width=True)
    with tab2:
    # Use the native Altair theme.
        st.altair_chart(plotfinal6MS, use_container_width=True)
    with tab3:
        st.altair_chart(plotfinal6MP, use_container_width=True)
    with tab4:
        st.altair_chart(plotfinal9M, use_container_width=True)
    with tab5:
        st.altair_chart(plotfinal9MS, use_container_width=True)
    with tab6:
        st.altair_chart(plotfinal9MP, use_container_width=True)
    with tab7:
        st.altair_chart(plotfinal7M, use_container_width=True)
    with tab8:
        st.altair_chart(plotfinal7MS, use_container_width=True)
    with tab9:
        st.altair_chart(plotfinal7MP, use_container_width=True)
    with tab10:
        st.altair_chart(plotfinalLCOP, use_container_width=True)
    with tab11:
        st.altair_chart(plotfinalLCOS, use_container_width=True)
    with tab12:
        st.altair_chart(plotfinalLCOPP, use_container_width=True)

    st.caption("🔎Fuente: Asobal")
    expander = st.expander(" ➕ **LEGEND**")
    expander.write("**LxP** = Paradas realizadas según distancia")
    expander.write("**LxM** = Número total de lanzamientos recibidos según distancia")
    expander.write("**Lx%** = Porcentaje de paradas en el lanzamiento según distancia")

def gk2():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import altair as alt
    from vega_datasets import data
    import matplotlib.colors as mcolors


    st.title('​​🙌​Goalkeepers Saving Performance')
    st.header('🥅Porteros Asobal')
    st.subheader('📌Compara el rendimiento de los porteros de la Liga Asobal:')

    df = pd.read_excel("asobalgk2324.xlsx")

    # Verifica los nombres de los jugadores únicos en la columna 'Jugador'
    jugadores_unicos = df['Jugador'].unique()

    # Generar una clave única para el widget multiselect
    player_selection_key = "player_selection"
    selected_players = st.multiselect('Selecciona dos jugadores:', df['Jugador'], default=['Emil Nielsen', 'Miguel Espinha'], key=player_selection_key)

    # Validación para asegurarse de que se seleccionen exactamente dos jugadores
    if len(selected_players) == 2:
        # Filtrar los datos según los jugadores seleccionados
        filtered_data = df[df['Jugador'].isin(selected_players)]

        # Crear el gráfico de radar
        categories = ['L6P', 'L6M', 'L7P', 'L7M', 'L9P', 'L9M', 'LCOP', 'LCO']

        fig = go.Figure()

        # Lista de colores personalizados para cada jugador
        colors = ['blue', 'green']

        for i, player in enumerate(selected_players):
            values = filtered_data[filtered_data['Jugador'] == player][categories].values[0]
            values = values.tolist()
            values.append(values[0])  # Agregar el primer valor al final para cerrar el polígono

            # Cambiar colores para cada jugador
            line_color = colors[i]  # Color de la línea
            fill_color = f'rgba(0, 0, 255, 0.2)'  # Color del área rellena con transparencia

            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories + [categories[0]],
                fill='toself',
                name=player,
                line=dict(color=line_color, width=2),
                fillcolor=fill_color
            ))

        # Ajustar el tamaño del gráfico directamente desde Plotly
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 180],
                    tickvals=[50, 100, 150],
                    ticktext=["50", "100", "150"],
                    ticks="outside",
                ),
            ),
            showlegend=True,
            title='Lanzamientos Marcados/Intentados según Distancias',
            width=800,  # Ajusta el ancho del gráfico
            height=600  # Ajusta la altura del gráfico
        )

        st.plotly_chart(fig)
    else:
        st.warning('Selecciona exactamente dos jugadores para poder comparar.')


    # Crear una tabla con los valores de cada variable por cada jugador
    table_data = []
    for player in selected_players:
        values = filtered_data[filtered_data['Jugador'] == player][categories].values[0]
        table_data.append([player] + values.tolist())

    # Crear un DataFrame para la tabla
    table_df = pd.DataFrame(table_data, columns=['Jugador'] + categories)

    # Identificar las celdas con los valores más altos
    high_value_style = 'background-color: lawngreen;'  # Estilo CSS para resaltar las celdas

    for col in categories:
        max_value = table_df[col].max()
        table_df[col] = table_df.apply(
            lambda row: f"{row[col]} ⬆️" if row[col] == max_value else row[col],
            axis=1
        )

    # Mostrar la tabla con estilos CSS
    st.markdown(
        table_df.style.applymap(lambda x: high_value_style if '⬆️' in str(x) else '', subset=pd.IndexSlice[:, categories]).render(),
        unsafe_allow_html=True
    )


    st.divider()
    st.caption("🔎Fuente: Asobal")
    expander = st.expander(" ➕ **LEGEND**")
    expander.write("**LxP** = Paradas realizadas según distancia")
    expander.write("**LxM** = Número total de lanzamientos recibidos según distancia")

    st.divider()

    # Validación para asegurarse de que se seleccionen exactamente dos jugadores
    if len(selected_players) == 2:
        # Filtrar los datos según los jugadores seleccionados
        filtered_data = df[df['Jugador'].isin(selected_players)]

        # Crear el gráfico de radar
        categories = ['L6%', 'L7%', 'L9%', 'LCO%']

        fig = go.Figure()

        # Lista de colores personalizados para cada jugador
        colors = ['blue', 'green']

        for i, player in enumerate(selected_players):
            values = filtered_data[filtered_data['Jugador'] == player][categories].values[0]
            values = values.tolist()
            values.append(values[0])  # Agregar el primer valor al final para cerrar el polígono

            # Cambiar colores para cada jugador
            line_color = colors[i]  # Color de la línea
            fill_color = f'rgba(0, 0, 255, 0.2)'  # Color del área rellena con transparencia

            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories + [categories[0]],
                fill='toself',
                name=player,
                line=dict(color=line_color, width=2),
                fillcolor=fill_color
            ))

        # Ajustar el tamaño del gráfico directamente desde Plotly
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1],
                    tickvals=[0, 0.250, 0.500, 0.750],
                    ticktext=["0", "0.250", "0.500", "0.750"],
                    ticks="outside",
                ),
            ),
            showlegend=True,
            title='Porcentajes en el Lanzamiento según Distancias',
            width=800,  # Ajusta el ancho del gráfico
            height=600  # Ajusta la altura del gráfico
        )

        st.plotly_chart(fig)
    else:
        st.warning('Selecciona exactamente dos jugadores para poder comparar.')

    # Crear una tabla con los valores de cada variable por cada jugador
    table_data = []
    for player in selected_players:
        values = filtered_data[filtered_data['Jugador'] == player][categories].values[0]
        table_data.append([player] + values.tolist())

    # Crear un DataFrame para la tabla
    table_df = pd.DataFrame(table_data, columns=['Jugador'] + categories)

    # Formatear los valores con dos decimales
    table_df[categories] = table_df[categories].applymap("{:.2f}".format)

    # Identificar las celdas con los valores más altos
    high_value_style = 'background-color: lawngreen;'  # Estilo CSS para resaltar las celdas

    for col in categories:
        max_value = table_df[col].max()
        table_df[col] = table_df.apply(
            lambda row: f"{row[col]} ⬆️" if row[col] == max_value else row[col],
            axis=1
        )

    # Mostrar la tabla con estilos CSS
    st.markdown(
        table_df.style.applymap(lambda x: high_value_style if '⬆️' in str(x) else '', subset=pd.IndexSlice[:, categories]).render(),
        unsafe_allow_html=True
    )

    st.divider()
    st.caption("🔎Fuente: Asobal")
    expander = st.expander(" ➕ **LEGEND**")
    expander.write("**Lx%** = Porcentaje de paradas según distancia del lanzamiento")

def gk3():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import altair as alt
    from vega_datasets import data
    import matplotlib.colors as mcolors


    st.title('​​🗂️​​Data Consulting')
    st.header('🥅Porteros Asobal')
    st.subheader('📌Goalkeepers Data:')

    df = pd.read_excel("asobalgk2324.xlsx")

    st.write('Consulta datos porteros Asobal:')
    st.write(df)
    
    st.caption("🔎Fuente: Asobal")

    #Legend
    expander = st.expander("➕ **LEGEND**")
    expander.write("**Equipo** = Nombre del equipo")
    expander.write("**Nº** = Dorsal del portero")
    expander.write("**Gol** = Goles anotados")
    expander.write("**Ast** = Asistencias completadas")
    expander.write("**ToG** = Total Goles Marcados")
    expander.write("**ToL** = Total Lanzamientos Intentados")
    expander.write("**To%** = Porcentaje total de acierto en el lanzamiento")
    expander.write("**L6 (Lanzamientos de 6 metros), L9 (Lanzamientos de 9 metros), L7 (Penaltis), LCO (Lanzamientos de contraataque)** = Siguen el mismo proceso de paradas, lanzamientos recibidos y porcentaje de paradas según cada distancia o tipo de lanzamiento.")
    

    st.divider()

    st.write('Consulta los datos según equipos:')
    ## Conseguir lista de equipos
    Equipos = df['Equipo'].unique()

    ## Create the select box
    selected_team = st.selectbox('Escoge equipo:', Equipos)

    ## Filter the data
    filtered_data = df[df['Equipo'] == selected_team]

    st.write(filtered_data)

    st.caption("🔎Fuente: Asobal")

    #Legend
    expander = st.expander("➕ **LEGEND**")
    expander.write("**Equipo** = Nombre del equipo")
    expander.write("**Nº** = Dorsal del portero")
    expander.write("**Gol** = Goles anotados")
    expander.write("**Ast** = Asistencias completadas")
    expander.write("**ToG** = Total Goles Marcados")
    expander.write("**ToL** = Total Lanzamientos Intentados")
    expander.write("**To%** = Porcentaje total de acierto en el lanzamiento")
    expander.write("**L6 (Lanzamientos de 6 metros), L9 (Lanzamientos de 9 metros), L7 (Penaltis), LCO (Lanzamientos de contraataque)** = Siguen el mismo proceso de paradas, lanzamientos recibidos y porcentaje de paradas según cada distancia o tipo de lanzamiento.")
    

#MENU PAGES GOALKEEPERS
page_names_GK = {
    "🧱Saves": gk,
    "🏹​​Saves Distances": gk1,
    "🙌​Goalkeepers Saving Performance": gk2,
    "🗂️​Data Consulting":gk3,
}

#------------------------------------------------------------------------------------------------------------------------------

# Sidebar
image = Image.open('HDL-blanc.png')

# Modificar la dimensión de la imagen
image = image.resize((220, 220))  # Ajusta el tamaño como desees

# Colocar la imagen en la barra lateral
st.sidebar.image(image)

# Selección del menú
menu_selection = st.sidebar.selectbox("Selecciona un menú:", ["Asobal Players", "Asobal GK"])

# Define un diccionario que mapea las opciones del menú a las funciones correspondientes
menu_options = {
    "Asobal Players": page_names_to_funcs,
    "Asobal GK": page_names_GK
}

# Verifica si la opción del menú seleccionada está en el diccionario
if menu_selection in menu_options:
    selected_page = st.sidebar.selectbox("Selecciona una página:", menu_options[menu_selection].keys())
    menu_options[menu_selection][selected_page]()
else:
    # Manejar el caso cuando la opción del menú no está en el diccionario
    st.sidebar.warning("Opción de menú no válida")



