import streamlit as st
import pandas as pd
from PIL import Image
from soccerplots.radar_chart import Radar

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



## parameter names
params = ['xAssists', 'Key Passes', 'Crosses Into Box', 'Cross Competion', 'Deep Completions', 
          'Progressive Passes', 'Prog. Passes Accuracy%', 'Dribbles', 'Progressive Runs', 
          'PADJ Interceptions', 'Succ. Def Actions', 'Def Duel Win%']

## range values
ranges = [(0.0, 0.15), (0.0, 0.67), (0.06, 0.63), (19.51, 50.0), (0.35, 1.61), (6.45, 11.94), (62.94, 79.46), (0.43, 4.08), (0.6, 2.33), (5.01, 7.2), (9.02, 12.48),
          (52.44, 66.67)]

## parameter value
values = [
    [0.11, 0.53, 0.70, 27.66, 1.05, 6.84, 84.62, 4.56, 2.22, 5.93, 8.88, 64.29],   ## for Sergino Dest
    [0.07, 0.36, 0.16, 32.14, 1.04, 7.37, 74.46, 3.68, 2.40, 6.87, 8.97, 61.14]    ## for Nelson Semedo
]

## title
title = dict(
    title_name='Sergiño Dest',
    title_color='#B6282F',
    subtitle_name='AFC Ajax',
    subtitle_color='#B6282F',
    title_name_2='Nelson Semedo',
    title_color_2='#344D94',
    subtitle_name_2='Barcelona',
    subtitle_color_2='#344D94',
    title_fontsize=18,
    subtitle_fontsize=15,
)

## endnote 
endnote = "Visualization made by: Anmol Durgapal(@slothfulwave612)\nAll units are in per90"

## instantiate object
radar = Radar()

## plot radar -- compare
fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values, 
                           radar_color=['#B6282F', '#344D94'], 
                           title=title, endnote=endnote,
                           compare=True)






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
    
