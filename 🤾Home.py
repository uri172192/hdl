import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#-----------------------------------------------
st.set_page_config(page_title="HDL", page_icon="favicon-32x32.png", layout="wide")
col1, col2 = st.columns(2)

with col1:
    image = Image.open('HDL-blanc.png')
    st.image(image) 
    imageasobal = Image.open('asobal.jpg')
    new_imageasobal = imageasobal.resize((300, 200))
    st.image(new_imageasobal)

with col2:
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


