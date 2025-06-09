import streamlit as st
import pandas as pd
import datetime
import altair as alt

# --- CONFIGURACIÓ GENERAL ---
st.set_page_config(page_title="Gestor de Càrrega i Prevenció de Lesions", layout="wide")
st.title("🏋️ Gestor de Càrrega d'Entrenament i Prevenció de Lesions")

# --- INICIALITZACIÓ DE DADES ---
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["Data", "Nom", "Durada", "RPE", "Tipus", "Càrrega"])

# --- FORMULARI D'ENTRENAMENT ---
with st.expander("📥​ Tracking Data", expanded=False):
    st.subheader("📥​ Registrar una nova sessió")
    with st.form("formulari"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom del jugador", "")
            data = st.date_input("Data", datetime.date.today())
            tipus = st.selectbox("Tipus d'entrenament", ["Físic + Pista","Pista", "Físic", "Partit", "Altres"])
        with col2:
            durada = st.select_slider("Durada (min)", options=[30, 60, 90, 120, 140, 160], value=90)
            rpe = st.select_slider("RPE (1-10)", options=list(range(1, 11)), value=5)
        enviar = st.form_submit_button("Guardar")
        if enviar:
            carrega = int(durada) * int(rpe)
            nou = pd.DataFrame([[data, nom, durada, rpe, tipus, carrega]],
                               columns=["Data", "Nom", "Durada", "RPE", "Tipus", "Càrrega"])
            st.session_state["data"] = pd.concat([st.session_state["data"], nou], ignore_index=True)
            st.success("Sessio registrada correctament")

# --- MOSTRAR DADES ---
with st.expander("📅 Dataset", expanded=False):
    st.subheader("📅 Registre")
    df = st.session_state["data"].copy()
    df["Data"] = pd.to_datetime(df["Data"])
    df = df.sort_values("Data")

    # --- FILTRE PER NOM ---
    noms_disponibles = df["Nom"].unique().tolist()
    nom_seleccionat = st.selectbox("Filtrar per nom de jugadora", ["Totes"] + noms_disponibles)
    if nom_seleccionat != "Totes":
        df = df[df["Nom"] == nom_seleccionat]

    st.dataframe(df, use_container_width=True)

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
            st.error("⚠️ ACWR molt alt! Risc de lesió elevat. Considera descans o sessions més lleugeres.")
        elif acwr_actual > 1.3:
            st.warning("⚠️ ACWR elevat. Revisa la càrrega i parla amb la jugadora si té molèsties.")
        elif acwr_actual < 0.8:
            st.info("ℹ️ ACWR baix. Pot indicar desentrenament. Considera augmentar l'activitat progressivament.")
        else:
            st.success("✅ ACWR en zona segura.")
