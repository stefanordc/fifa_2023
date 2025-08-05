# streamlit_app.py  ───────────────────────────────────────────
import pathlib
from datetime import datetime

import pandas as pd
import streamlit as st
import webbrowser

# ────────────────────────── CONFIG ───────────────────────────
# localização do CSV *dentro* do repositório
BASE_DIR  = pathlib.Path(__file__).parent           # pasta onde está este arquivo
CSV_PATH  = BASE_DIR / "datasets" / "CLEAN_FIFA23_official_data.csv"

@st.cache_data
def load_data(csv_path: pathlib.Path) -> pd.DataFrame:
    """Lê o CSV uma única vez e armazena em cache."""
    df = pd.read_csv(csv_path, index_col=0)
    df["Contract Valid Until"] = pd.to_datetime(df["Contract Valid Until"],
                                                errors="coerce")
    # filtros iniciais
    df = df[df["Value(£)"] > 0]
    df = df.sort_values(by="Overall", ascending=False)
    return df

# carrega e guarda no session_state se ainda não existir
if "data" not in st.session_state:
    st.session_state["data"] = load_data(CSV_PATH)

df_data = st.session_state["data"]

# ────────────────────────── UI ───────────────────────────────
st.set_page_config(page_title="FIFA 23 Dataset", page_icon="⚽",
                   layout="wide")

st.write("# FIFA 23 OFFICIAL DATASET! ⚽")

st.sidebar.markdown("Desenvolvido por "
                    "[Stéfano Bruno](https://www.linkedin.com/in/stefano-bruno-mf/)")

st.sidebar.link_button("Acesse os dados no Kaggle", "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
    O conjunto de dados de jogadores de futebol **2017 → 2023** contém mais de
    **17 mil registros** com dados demográficos, atributos físicos, estatísticas
    de jogo, detalhes de contrato e afiliações de clube.
    """
)

st.dataframe(df_data, use_container_width=True)
# ─────────────────────────────────────────────────────────────
