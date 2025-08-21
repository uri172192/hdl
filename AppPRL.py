import streamlit as st
import pandas as pd
import datetime
import altair as alt
import os
import numpy as np

st.set_page_config(page_title="Gestor de Càrrega i Prevenció de Lesions", layout="wide")
st.title("🏋️ Gestor de Càrrega d'Entrenament i Prevenció de Lesions")

FITXER_EXCEL = "registres_entrenament.xlsx"
COLS = ["ID", "Data", "Nom", "Durada", "RPE", "Tipus", "Càrrega"]

# ---------- Utilitats ----------
def carregar_excel(path):
    if os.path.exists(path):
        df = pd.read_excel(path)
        # Garantir columnes i tipus
        for c in COLS:
            if c not in df.columns:
                df[c] = np.nan
        df = df[COLS]
        df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
        # IDs coherents
        if df["ID"].isna().any():
            # Reassignar IDs únics si falten
            df = df.reset_index(drop=True)
            df["ID"] = range(1, len(df) + 1)
    else:
        df = pd.DataFrame(columns=COLS)
    return df

def guardar_excel(df, path):
    # Recalcular càrrega abans de desar
    df["Durada"] = pd.to_numeric(df["Durada"], errors="coerce")
    df["RPE"] = pd.to_numeric(df["RPE"], errors="coerce")
    df["Càrrega"] = (df["Durada"].fillna(0) * df["RPE"].fillna(0)).astype(float)
    # Orden i tipus de data
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    df = df[COLS].sort_values("Data")
    df.to_excel(path, index=False)

def next_id(df):
    return (int(df["ID"].max()) + 1) if not df.empty else 1

# ---------- Inicialització ----------
if "data" not in st.session_state:
    st.session_state["data"] = carregar_excel(FITXER_EXCEL)

# ---------- Formulari d'entrada ----------
with st.expander("📥 Tracking Data", expanded=False):
    st.subheader("Registrar una nova sessió")
    with st.form("formulari"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom de la jugadora", "Carla")
            data = st.date_input("Data", datetime.date.today())
            tipus = st.selectbox("Tipus d'entrenament", ["Força", "Resistència", "Tècnica", "Partit", "Altres"])
        with col2:
            durada = st.slider("Durada (min)", 30, 180, 90, step=10)
            rpe = st.slider("RPE (1-10)", 1, 10, 5)

        enviar = st.form_submit_button("Guardar")

        if enviar:
            nou_id = next_id(st.session_state["data"])
            carrega = durada * rpe
            nou = pd.DataFrame([[nou_id, data, nom, durada, rpe, tipus, carrega]], columns=COLS)
            st.session_state["data"] = pd.concat([st.session_state["data"], nou], ignore_index=True)

            # 🔒 Desa immediatament a Excel
            guardar_excel(st.session_state["data"], FITXER_EXCEL)
            st.success("Sessió registrada i guardada en Excel ✅")

# ---------- Dataset editable + filtre ----------
with st.expander("📅 Dataset", expanded=True):
    st.subheader("📅 Registre (editable)")

    df_total = st.session_state["data"].copy()
    if not df_total.empty:
        df_total["Data"] = pd.to_datetime(df_total["Data"], errors="coerce")

        # Filtre per nom
        noms = df_total["Nom"].dropna().unique().tolist()
        nom_seleccionat = st.selectbox("Filtrar per nom de jugadora", ["Totes"] + sorted(noms))

        if nom_seleccionat != "Totes":
            df_view = df_total[df_total["Nom"] == nom_seleccionat].copy()
        else:
            df_view = df_total.copy()

        # Recordem quins IDs hi havia abans d'editar (per detectar eliminacions)
        ids_originals_view = set(df_view["ID"].astype(int).tolist())

        # Taula editable (fem ID i Càrrega no editables; Càrrega es recalcula)
        df_view_display = df_view[["Data", "Nom", "Durada", "RPE", "Tipus", "Càrrega", "ID"]].copy()

        df_editat = st.data_editor(
            df_view_display,
            num_rows="dynamic",
            use_container_width=True,
            column_config={
                "ID": st.column_config.Column("ID", help="Identificador intern (no editable)", disabled=True),
                "Càrrega": st.column_config.NumberColumn("Càrrega", help="Es calcula automàticament (Durada × RPE)", disabled=True),
                "Data": st.column_config.DateColumn("Data", format="YYYY-MM-DD")
            },
            hide_index=True
        )

        # Guardar canvis: reconciliar amb dataset global per ID
        if st.button("💾 Guardar canvis a Excel"):
            # Assegurar tipus
            df_editat["Data"] = pd.to_datetime(df_editat["Data"], errors="coerce")
            df_editat["Durada"] = pd.to_numeric(df_editat["Durada"], errors="coerce")
            df_editat["RPE"] = pd.to_numeric(df_editat["RPE"], errors="coerce")
            # Omple el Nom si s'està filtrant per una jugadora concreta i hi ha NaN
            if nom_seleccionat != "Totes":
                df_editat["Nom"] = df_editat["Nom"].fillna(nom_seleccionat)

            # IDs presents a l'edició (files mantingudes o noves)
            ids_editats = set(df_editat["ID"].dropna().astype(int).tolist())

            # 1) ELIMINACIONS (IDs que estaven a la vista i ja no hi són)
            ids_eliminats = ids_originals_view - ids_editats
            if ids_eliminats:
                st.session_state["data"] = st.session_state["data"][~st.session_state["data"]["ID"].isin(ids_eliminats)]

            # 2) ACTUALITZACIONS (files amb ID existent)
            amb_id = df_editat[~df_editat["ID"].isna()].copy()
            if not amb_id.empty:
                amb_id["ID"] = amb_id["ID"].astype(int)
                # Recalcula càrrega
                amb_id["Càrrega"] = amb_id["Durada"].fillna(0) * amb_id["RPE"].fillna(0)
                for _, fila in amb_id.iterrows():
                    st.session_state["data"].loc[st.session_state["data"]["ID"] == fila["ID"], ["Data", "Nom", "Durada", "RPE", "Tipus", "Càrrega"]] = [
                        fila["Data"], fila["Nom"], fila["Durada"], fila["RPE"], fila["Tipus"], fila["Càrrega"]
                    ]

            # 3) INSERCIÓ DE NOVES FILES (sense ID)
            sense_id = df_editat[df_editat["ID"].isna()].copy()
            if not sense_id.empty:
                # Assignar ID nous i calcular càrrega
                base_id = next_id(st.session_state["data"])
                nous = []
                for i, fila in sense_id.reset_index(drop=True).iterrows():
                    nou = {
                        "ID": base_id + i,
                        "Data": pd.to_datetime(fila["Data"], errors="coerce"),
                        "Nom": fila["Nom"],
                        "Durada": pd.to_numeric(fila["Durada"], errors="coerce"),
                        "RPE": pd.to_numeric(fila["RPE"], errors="coerce"),
                        "Tipus": fila["Tipus"],
                        "Càrrega": (pd.to_numeric(fila["Durada"], errors="coerce") or 0) * (pd.to_numeric(fila["RPE"], errors="coerce") or 0)
                    }
                    # Si s'edita en vista filtrada, omple "Nom" si cal
                    if pd.isna(nou["Nom"]) and nom_seleccionat != "Totes":
                        nou["Nom"] = nom_seleccionat
                    nous.append(nou)
                if nous:
                    st.session_state["data"] = pd.concat([st.session_state["data"], pd.DataFrame(nous)[COLS]], ignore_index=True)

            # Neteja final, recalcular càrrega i desar
            st.session_state["data"]["Data"] = pd.to_datetime(st.session_state["data"]["Data"], errors="coerce")
            st.session_state["data"]["Durada"] = pd.to_numeric(st.session_state["data"]["Durada"], errors="coerce")
            st.session_state["data"]["RPE"] = pd.to_numeric(st.session_state["data"]["RPE"], errors="coerce")
            st.session_state["data"]["Càrrega"] = st.session_state["data"]["Durada"].fillna(0) * st.session_state["data"]["RPE"].fillna(0)
            st.session_state["data"] = st.session_state["data"][COLS].drop_duplicates(subset=["ID"]).reset_index(drop=True)

            guardar_excel(st.session_state["data"], FITXER_EXCEL)
            st.success("Canvis guardats a l’Excel ✅")

# ---------- Gràfics i ACWR (amb filtre aplicat) ----------
# Fem servir df_view (si existeix) o df_total
if "df_view" in locals() and not df_view.empty:
    df_plot = df_view.copy()
elif not st.session_state["data"].empty:
    df_plot = st.session_state["data"].copy()
else:
    df_plot = pd.DataFrame(columns=COLS)

if not df_plot.empty:
    df_plot["Data"] = pd.to_datetime(df_plot["Data"], errors="coerce")
    df_plot = df_plot.dropna(subset=["Data"])
    df_group = df_plot.groupby("Data").agg({"Càrrega": "sum"}).reset_index()

    chart = alt.Chart(df_group).mark_area(opacity=0.5).encode(
        x="Data:T",
        y="Càrrega:Q"
    ).properties(title="📊 Evolució de la Càrrega d'Entrenament")
    st.altair_chart(chart, use_container_width=True)

    # ACWR
    df_acwr = df_group.set_index("Data").resample("D").sum().fillna(0)
    df_acwr["Mitjana_7"] = df_acwr["Càrrega"].rolling(7).mean()
    df_acwr["Mitjana_28"] = df_acwr["Càrrega"].rolling(28).mean()
    df_acwr["ACWR"] = df_acwr["Mitjana_7"] / df_acwr["Mitjana_28"]

    st.subheader("🔄 ACWR (Acute:Chronic Workload Ratio)")
    st.line_chart(df_acwr[["ACWR"]])

    acwr_actual = df_acwr["ACWR"].iloc[-1]
    if pd.notna(acwr_actual):
        st.metric("ACWR actual", f"{acwr_actual:.2f}")
