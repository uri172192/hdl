import streamlit as st
import pandas as pd
import datetime
import altair as alt
import os

st.set_page_config(page_title="Gestor de Càrrega i Prevenció de Lesions", layout="wide")
st.title("🏋️ Gestor de Càrrega d'Entrenament i Prevenció de Lesions")

FITXER_EXCEL = "carrega_entrenaments.xlsx"

# --- CARREGAR DADES DE L'EXCEL SI EXISTEIX ---
if "data" not in st.session_state:
    if os.path.exists(FITXER_EXCEL):
        st.session_state["data"] = pd.read_excel(FITXER_EXCEL)
    else:
        st.session_state["data"] = pd.DataFrame(columns=["Data", "Nom", "Durada", "RPE", "Tipus", "Càrrega"])

# --- FORMULARI D'ENTRENAMENT ---
with st.expander("📥 Tracking Data", expanded=False):
    st.subheader("Registrar una nova sessió")
    with st.form("formulari"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom de la jugadora", "Carla")
            data = st.date_input("Data", datetime.date.today())
            tipus = st.selectbox("Tipus d'entrenament", ["Força", "Resistència", "Tècnica", "Partit", "Altres"])
        with col2:
            durada = st.number_input("Durada (min)", min_value=1, step=1)
            rpe = st.slider("RPE (1-10)", 1, 10, 5)
        enviar = st.form_submit_button("Guardar")

        if enviar:
            carrega = durada * rpe
            nou = pd.DataFrame([[data, nom, durada, rpe, tipus, carrega]],
                               columns=["Data", "Nom", "Durada", "RPE", "Tipus", "Càrrega"])
            st.session_state["data"] = pd.concat([st.session_state["data"], nou], ignore_index=True)
            st.success("Sessió registrada correctament ✅")

# --- MOSTRAR DADES ---
with st.expander("📅 Dataset", expanded=True):
    st.subheader("📅 Registre")
    df = st.session_state["data"].copy()
    if not df.empty:
        df["Data"] = pd.to_datetime(df["Data"])
        df = df.sort_values("Data")

        noms_disponibles = df["Nom"].unique().tolist()
        nom_seleccionat = st.selectbox("Filtrar per nom de jugadora", ["Totes"] + noms_disponibles)
        if nom_seleccionat != "Totes":
            df = df[df["Nom"] == nom_seleccionat]

        st.dataframe(df, use_container_width=True)

        # --- BOTÓ PER GUARDAR A EXCEL ---
        if st.button("💾 Guardar registres a Excel"):
            st.session_state["data"].to_excel(FITXER_EXCEL, index=False)
            st.success(f"Dades guardades a {FITXER_EXCEL} ✅")

# --- GRÀFIC DE CÀRREGA ---
if not df.empty:
    df_group = df.groupby("Data").agg({"Càrrega": "sum"}).reset_index()
    chart = alt.Chart(df_group).mark_area(opacity=0.5).encode(
        x="Data:T",
        y="Càrrega:Q"
    ).properties(title="📊 Evolució de la Càrrega d'Entrenament")
    st.altair_chart(chart, use_container_width=True)

    # --- CÀLCUL ACWR ---
    df_group = df_group.set_index("Data").resample("D").sum().fillna(0)
    df_group["Mitjana_7"] = df_group["Càrrega"].rolling(7).mean()
    df_group["Mitjana_28"] = df_group["Càrrega"].rolling(28).mean()
    df_group["ACWR"] = df_group["Mitjana_7"] / df_group["Mitjana_28"]

    st.subheader("🔄 ACWR (Acute:Chronic Workload Ratio)")
    st.line_chart(df_group[["ACWR"]])

    acwr_actual = df_group["ACWR"].iloc[-1]
    if pd.notna(acwr_actual):
        st.metric("ACWR actual", f"{acwr_actual:.2f}")

        if acwr_actual > 1.5:
            st.error("⚠️ ACWR molt alt! Risc de lesió elevat.")
        elif acwr_actual > 1.3:
            st.warning("⚠️ ACWR elevat. Revisa la càrrega.")
        elif acwr_actual < 0.8:
            st.info("ℹ️ ACWR baix. Pot indicar desentrenament.")
        else:
            st.success("✅ ACWR en zona segura.")
