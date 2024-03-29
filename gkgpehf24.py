import streamlit as st
import pandas as pd
from PIL import Image

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
    
