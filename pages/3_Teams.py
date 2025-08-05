import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state["data"]

# Definindo os clubes únicos
clubes = sorted(df_data["Club"].dropna().unique())
club = st.sidebar.selectbox("Clube", clubes)

# Filtrando os jogadores dos clubes
df_filtered = df_data[df_data["Club"] == club].set_index("Name")

# Montando o cabeçalho
st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

# Selecionando as colunas que vamos trabalhar
colums = ["Kit Number", "Position", "Age", "Photo", "Flag", "Overall", "Potential", "Preferred Foot", "Value(£)", "Wage(£)", "Joined",
          "Height(cm.)", "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)", "Real Face"]

st.dataframe(df_filtered[colums],
             column_config={
                 "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
                 "Value(£)": st.column_config.NumberColumn(),
                 "Wage(£)": st.column_config.ProgressColumn("Pagamento Semanal", format="£%f",
                                                                min_value=0, max_value=df_filtered["Wage(£)"].max()),
                "Value(£)": st.column_config.ProgressColumn("Valor de Mercado", format="£%f",
                                                                min_value=0, max_value=df_filtered["Value(£)"].max()),
                "Release Clause(£)": st.column_config.ProgressColumn("Rescisão", format="£%f",
                                                                min_value=0, max_value=df_filtered["Release Clause(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             }, height=1000)