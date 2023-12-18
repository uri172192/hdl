import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title="Players Shooting Performance", page_icon="punteria.png", layout="wide")

# Cargar el DataFrame desde el archivo Excel
df = pd.read_excel("DatasetJugadoresAsobal2223.xlsx")
df1 = pd.read_excel("DatasetJugadoresAsobal2324.xlsx")


# Título de la página
st.title('🎯Players Shooting Performance')

# Título de la sección
st.subheader('📌Compara el rendimiento de los de jugadores de la Liga Asobal')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    imageasobal = Image.open('apple-touch-icon.png')
    st.image(imageasobal)

# Obtener una lista de temporadas únicas de ambos DataFrames
temporadas = pd.concat([df1['Temporada'], df['Temporada']]).unique()

# Crear el select box para la temporada
selected_temporada1 = st.selectbox('Escoge una temporada:', temporadas, key="selectbox1")

# Filtrar los datos según la temporada seleccionada desde ambos DataFrames
filtered_data1 = pd.concat([df[df['Temporada'] == selected_temporada1], df1[df1['Temporada'] == selected_temporada1]])


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
if isinstance(table_df, pd.DataFrame):
    # Aplicar estilos al DataFrame
    styled_table = table_df.style.applymap(lambda x: high_value_style if '⬆️' in str(x) else '', subset=pd.IndexSlice[:, categories])
    # Renderizar el DataFrame estilizado usando st.write
    st.write(styled_table)
else:
    st.error("table_df no es un DataFrame válido.")


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
if isinstance(table_df, pd.DataFrame):
    # Aplicar estilos al DataFrame
    styled_table = table_df.style.applymap(lambda x: high_value_style if '⬆️' in str(x) else '', subset=pd.IndexSlice[:, categories])
    # Renderizar el DataFrame estilizado usando st.write
    st.write(styled_table)
else:
    st.error("table_df no es un DataFrame válido.")

st.divider()
st.caption("🔎Fuente: Asobal")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**Lx%** = Porcentaje de acierto en el lanzamiento según distancia")
