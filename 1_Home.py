import pandas as pd
import streamlit as st
import webbrowser
from datetime import datetime

# Abrindo o arquivo
caminho_arquivo = r"C:\Pessoal\Data_science\Projetos\fifa_2025\datasets\CLEAN_FIFA23_official_data.csv"

if "data" not in st.session_state:
    df_data = pd.read_csv(caminho_arquivo, index_col=0)
    
    # Converte a coluna para datetime
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)    
    st.session_state["data"] = df_data

# Boas-vindas
st.write("# FIFA 23 OFFICIAL DATASET! ⚽")

# Direito autoral
st.sidebar.markdown("Desenvolvido por [Stéfano Bruno](https://www.linkedin.com/in/stefano-bruno-mf/)")

# Criando o botão com o link do dataset
btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

# Passando informações iniciais do dataset
st.markdown(
    """
    O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes
    sobre jogadores de futebol profissional.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos dos
    jogadores, características físicas, estatísticas de jogo, detalhes do contrato e afiliações
    ao clube.
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para
    analistas, pesquisadores e entusiastas do futebol interessados em explorar vários aspectos
    do mundo do esporte, pois permite estudar atributos dos jogadores, métricas de desempenho,
    avaliação de mercado, análise de clubes, posicionamento dos jogadores e desenvolvimento do
    jogador ao longo do tempo.
    """
)