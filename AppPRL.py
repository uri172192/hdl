import streamlit as st
import pandas as pd
import datetime
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Gestor de Càrrega i Prevenció de Lesions", layout="wide")
st.title("🏋️ Gestor de Càrrega d'Entrenament i Prevenció de Lesions")

COLS = ["ID", "Data", "Nom", "Durada", "RPE", "Tipus", "Càrrega"]

# ---------- Connexió a Google Sheets ----------
# Requereix configurar secrets a Streamlit Cloud:
# [connections.gsheets]
# spreadsheet = "https://docs.google.com/spreadsheets/d/<EL_TEUSHEET_ID>/edit"
# I el bloc [gcp_service_account] amb les credencials del compte de servei.
conn = st.connection("gsheets", type=GSheetsConnection)

# Llegir dades de la pestanya "Registres"; si està buida o li falten columnes, inicialitzar
sheet_df = conn.read(worksheet="Registres", ttl=5)
if sheet_df is None or sheet_df.empty:
    df = pd.DataFrame(columns=COLS)
else:
    df = sheet_df.copy()
    for c in COLS:
        if c not in df.columns:
            df[c] = None
    df = df[COLS]

# ---------- Utilitats ----------
def next_id(frame: pd.DataFrame) -> int:
    try:
        return int(pd.to_numeric(frame["ID"], errors="coerce").max()) + 1 if not frame.empty else 1
    except Exception:
        return 1

def guardar_a_sheets(frame: pd.DataFrame) -> None:
    # Normalitzar tipus i ordre de columnes abans d'escriure
    out = frame.copy()
    out["Data"] = pd.to_datetime(out["Data"], errors="coerce").dt.strftime("%Y-%m-%d")
    out["Durada"] = pd.to_numeric(out["Durada"], errors="coerce")
    out["RPE"] = pd.to_numeric(out["RPE"], errors="coerce")
    out["Càrrega"] = (out["Durada"].fillna(0) * out["RPE"].fillna(0)).astype(float)
    out = out[COLS]
    conn.update(worksheet="Registres", data=out)

# ---------- Formulari d'entrada ----------
with st.expander("📥 Tracking Data", expanded=True):
    st.subheader("Registrar una nova sessió")
    with st.form("formulari"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom del jugador", "")
            data = st.date_input("Data", datetime.date.today())
            tipus = st.selectbox("Tipus d'entrenament", ["Físic + Pista", "Pista", "Físic", "Partit", "Altres"])
        with col2:
            durada = st.slider("Durada (min)", 30, 180, 90, step=10)
            rpe = st.slider("RPE (1-10)", 1, 10, 5)

        enviar = st.form_submit_button("Guardar")

        if enviar:
            if not nom.strip():
                st.error("Cal indicar el nom del jugador.")
            else:
                nou = pd.DataFrame([
                    {
                        "ID": next_id(df),
                        "Data": data.strftime("%Y-%m-%d"),
                        "Nom": nom.strip(),
                        "Durada": int(durada),
                        "RPE": int(rpe),
                        "Tipus": tipus,
                        "Càrrega": float(durada * rpe),
                    }
                ], columns=COLS)
                df = pd.concat([df, nou], ignore_index=True)
                guardar_a_sheets(df)
                st.success("Sessió registrada i guardada a Google Sheets ✅")

# ---------- Visualització ----------
with st.expander("📅 Dataset complet", expanded=True):
    st.dataframe(df, use_container_width=True)
