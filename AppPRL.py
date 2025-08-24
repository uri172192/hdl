import streamlit as st
import pandas as pd
import datetime
import numpy as np
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Gestor de Càrrega i Prevenció de Lesions", layout="wide")
st.title("🏋️ Gestor de Càrrega d'Entrenament i Prevenció de Lesions")

COLS = ["ID", "Data", "Nom", "Durada", "RPE", "Tipus", "Càrrega"]

# ---------- Connexió a Google Sheets ----------
conn = st.connection("gsheets", type=GSheetsConnection)

# Llegim el full (pestanya "Registres")
df = conn.read(worksheet="Registres", ttl=5)

# Si el full està buit o li falten columnes, inicialitzem-lo
if df is None or df.empty or any(c not in df.columns for c in COLS):
    df = pd.DataFrame(columns=COLS)

# ---------- Funcions ----------
def next_id(df):
    return (int(df["ID"].max()) + 1) if not df.empty else 1

def guardar_a_sheets(df):
    conn.update(worksheet="Registres", data=df)

# ---------- Formulari d'entrada ----------
with st.expander("📥 Tracking Data", expanded=True):
    st.subheader("Registrar una nova sessió")
    with st.form("formulari"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom del jugador", "")
            data = st.date_input("Data", datetime.date.today())
            tipus = st.selectbox("Tipus d'entrenament", ["Físic + Pista","Pista", "Físic", "Partit", "Altres"])
        with col2:
            durada = st.slider("Durada (min)", 30, 180, 90, step=10)
            rpe = st.slider("RPE (1-10)", 1, 10, 5)

        enviar = st.form_submit_button("Guardar")

        if enviar and nom.strip():
            nou_id = next_id(df)
            carrega = durada * rpe
            nou = pd.DataFrame([[nou_id, data, nom, durada, rpe, tipus, carrega]], columns=COLS)
            df = pd.concat([df, nou], ignore_index=True)
            guardar_a_sheets(df)
            st.success("Sessió registrada i guardada a Google Sheets ✅")

# ---------- Visualització ----------
with st.expander("📅 Dataset complet", expanded=True):
    st.dataframe(df, use_container_width=True)
