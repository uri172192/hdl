import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#-----------------------------------------------
st.set_page_config(page_title="HDL", page_icon="favicon-32x32.png", layout="wide")

image = Image.open('HDL-blanc.png')
st.image(image)

st.subheader('📌Descripción HDL')
st.write('📢**Handball Data Lab** se presenta como una aplicación destinada al desarrollo y democratización del análisis de datos en balonmano. La finalidad es ayudar a los usuarios a **disfrutar, comprender y compartir los datos sobre el balonmano**. Actualmente, la web-app presenta varios contenidos analíticos de la Liga Profesional ASOBAL, la máxima competición del balonmano en España.')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    imageasobal = Image.open('apple-touch-icon.png')
    st.image(imageasobal)

st.divider()
st.subheader("📌Contenidos HDL")
st.write("🏐**Scorers**: visualiza los goleadores según equipo y posición")
st.write("🏹**Shooting Distances**: explora los máximos anotadores según la distancia del lanzamiento")
st.write("🎯**Players Shooting Performance**: escoge 2 jugadores y compara su rendimiento en el lanzamiento")
st.write("🕵️**Shooting Similiraty**: descubre los jugadores similares entre si según su eficacia en el lanzamiento")
st.write("🗂️**Data Consulting**: consulta los datos de los que disponemos sobre cada equipo en materia de lanzamientos")
st.divider()


