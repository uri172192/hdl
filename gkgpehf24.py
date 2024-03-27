import streamlit as st
import pandas as pd


st.set_page_config(page_title="TEST GK", layout="wide")
st.markdown("<h1 style='text-align: center;'>Goalkeeper EHF Group Phase</h1>", unsafe_allow_html=True)

df = pd.read_excel("dfgkgp.xlsx")

# Crear el expander
expander = st.expander("➕ **EHF GK TEAMS CONSULTORY**")

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
        st.write(f'GK Data EHF Team: {gkteam}')
        st.write(equipo_df)
    else:
        st.warning('Please, select an EHF team.')

# Crear el expander
expander = st.expander("➕ **EHF GK INDIVIDUAL CONSULTORY**")

# Dentro del expander, agregar el código para seleccionar un jugador
with expander:
    gk = st.selectbox('Select EHF GK:', 
                      (df['Name']), 
                      index=None, 
                      placeholder='Type GK name...')
    gk_selected = df[df['Name'] == gk]

    if not gk_selected.empty:
        st.write(f'GK Data EHF Team {gk}:')
        st.write(gk_selected)
    else:
        st.warning('Please, write a GK Name.')


# Mostrar el DataFrame completo + Search Bar:
st.write('GK EHF 23/24 Group Phase:', df)


st.caption("🔎Source: EHF")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**GC** = Goals Conceded")
expander.write("**NºMSA** = Number of Saves made by X distance")
expander.write("**NºMSO** = Number of Shots received by X distance")
expander.write("**WSA** = Number of saves made from wing shots")
expander.write("**WSO** = Number of wing shots received")
