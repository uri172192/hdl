import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from math import pi
import plotly.graph_objects as go

st.set_page_config(page_title="GK EHF DATA", page_icon="favicon-32x32.png", layout="wide")


#st.markdown("<h1 style='text-align: center;'>Goalkeeper EHF Champions League Data -- Group Phase</h1>", unsafe_allow_html=True)
st.title("🥅 Goalkeeper EHF Champions League Data 🤾🏿‍♂️")
left_co, cent_co, right_co = st.columns(3)
with left_co:
    st.subheader("📋 Group Phase 23/24 📋")
with cent_co:
    image = Image.open('logohdl.png')
    st.image(image)

df = pd.read_excel("dfgkgp.xlsx")

# Crear el expander
expander = st.expander("➕ **EHF GK TEAMS DATA CONSULTORY** 🥅🤾🏿‍♂")

# Dentro del expander, agregar el código para seleccionar un jugador
with expander:
    gkteam = st.selectbox('Select your team:',
                        (df['Team']),
                        index=None,
                        placeholder="Select EHF team...")
    #st.write('EHF Team selected:', gkteam)

    # Filtrar el DataFrame según el equipo seleccionado
    equipo_df = df[df['Team'] == gkteam]

    # Mostrar el DataFrame filtrado si se seleccionó un equipo
    if not equipo_df.empty:
        #st.write(f'GK Data EHF Team Selected: {gkteam}:')
        #st.write(equipo_df)
        # Redondear los valores a 2 decimales
        equipo_df_rounded = equipo_df.round(2)
        
        st.write(equipo_df_rounded)
    
    else:
        st.warning('Please, select an EHF team.')



# Crear el expander
expander = st.expander("➕ **EHF GK INDIVIDUAL DATA CONSULTORY** 🥅🤾🏻‍♂️")

# Dentro del expander, agregar el código para seleccionar un jugador
with expander:
    gk = st.selectbox('Select EHF GK:', 
                      (df['Name']), 
                      index=None, 
                      placeholder='Type GK name...')
    gk_selected = df[df['Name'] == gk]

    if not gk_selected.empty:
        #st.write(f'GK Data EHF Team {gk}:')
        #st.write(gk_selected)
        # Redondear los valores a 2 decimales
        gk_selected_rounded = gk_selected.round(2)
        
        #st.write(f'GK Data EHF Team {gk}:')
        st.write(gk_selected_rounded)
    else:
        st.warning('Please, write a GK Name.')

 
# Mostrar el DataFrame completo + Search Bar:
# Redondear los valores a 2 decimales
df_rounded = df.round(2)
st.write('🗃️**EHF 23/24 Group Phase GK Data:**', df_rounded)


image = Image.open('logohdl.png')

st.caption("🔎Source: EHF")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**SA%** = Saves %")
expander.write("**GC** = Goals Conceded")
expander.write("**NºMSA** = Number of Saves made by X distance")
expander.write("**NºMSO** = Number of Shots received by X distance")
expander.write("**WSA** = Number of saves made from wing shots")
expander.write("**WSO** = Number of wing shots received")


#with right_co:
    #image1 = Image.open('ehflogo.png')
    #st.image(image1)


# Generar una clave única para el widget multiselect
player_selection_key = "player_selection"
selected_players = st.multiselect('Selecciona dos porteros:', df['Name'],max_selections=2, key=player_selection_key, placeholder="Choose your Goalkeepers")
    
# Validación para asegurarse de que se seleccionen exactamente dos jugadores
if len(selected_players) == 2:
    
    # Filtrar los datos según los jugadores seleccionados
    gk_selected = df[df['Name'].isin(selected_players)]
    
    # Crear el gráfico de radar
    categories = ['Saves', '7MSA', '6MSA', '9MSA', 'WSA']
    
    fig = go.Figure()
    
    # Lista de colores personalizados para cada jugador
    colors = ['blue', 'red']
    
    for i, player in enumerate(selected_players):
        values =   gk_selected = df[df['Name'] == player][categories].values[0]
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
            title='Saves Made + Saves Made by Shoot Distances',
            width=800,  # Ajusta el ancho del gráfico
            height=600  # Ajusta la altura del gráfico
    )
    
    st.plotly_chart(fig)
else:
    st.warning('Selecciona exactamente dos jugadores para poder comparar.')
    
    # ... Código previo ...

# Definir las categorías para el gráfico de radar
categories = ['Saves', '7MSA', '6MSA', '9MSA', 'WSA']

# Crear una tabla con los valores de cada variable por cada jugador
table_data = []
for player in selected_players:
    values = df[df['Name'] == player][categories].values[0]
    table_data.append([player] + values.tolist())
    
# Crear un DataFrame para la tabla
table_df = pd.DataFrame(table_data, columns=['Name'] + categories)
    
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
st.caption("🔎 Source: EHF")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**NºMSA** = Saves made by X distance")
