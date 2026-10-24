
import streamlit as st
import pandas as pd
from pathlib import Path

CAMINHO_DADOS = Path(__file__).resolve().parent.parent / "data" / "imoveis.json"

st.set_page_config(
    page_title="Analista de Imóveis",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Dashboard de Análise de Imóveis")
st.write("Explore dados e indicadores do mercado imobiliário.")

@st.cache_data
def carregar_dados(caminho):
    df = pd.read_json(caminho)
    return df

df = carregar_dados(CAMINHO_DADOS)


maximo = df["preco"].max()
minimo = df["preco"].min()

df["preco_m2"] = df["preco"] / df["area_m2"]


cidades = df["cidade"].unique()
cidade_selecionada = st.selectbox("Selecione uma cidade", cidades)

tipos = df["tipo"].unique()

tipos = ["Todos"] + list(df["tipo"].unique())
tipo_selecionado = st.selectbox("Selecione um tipo", tipos)

faixa_preco = st.slider("Escolha a faixa de valor", minimo, maximo, (minimo, maximo))


if tipo_selecionado == "Todos":
    df_filtrado = df[(df["cidade"] == cidade_selecionada) & (df["preco"] >= faixa_preco[0]) & (df["preco"] <= faixa_preco[1])].copy()
else:
    df_filtrado = df[(df["cidade"] == cidade_selecionada) & (df["tipo"] == tipo_selecionado) & (df["preco"] >= faixa_preco[0]) & (df["preco"] <= faixa_preco[1])].copy()






total_imoveis = df_filtrado.shape[0]
media_preco = df_filtrado["preco"].mean()
mediana = df_filtrado["preco"].median()
media_area = df_filtrado["area_m2"].mean()


col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de imóveis", total_imoveis)
col2.metric("Preço médio", f"R$ {media_preco:,.2f}")
col3.metric("Área média", f"{media_area:,.2f} m²")
col4.metric("Mediana dos Preços", f"R$ {mediana:,.2f}")


preco_por_bairro = df_filtrado.groupby("bairro")["preco"].mean()
st.subheader("Preço médio por bairro")
st.bar_chart(preco_por_bairro)


preco_m2_por_bairro = df_filtrado.groupby("bairro")["preco_m2"].mean()
st.subheader("Preço médio por m² por bairro")
st.bar_chart(preco_m2_por_bairro)


st.subheader("Dados dos imóveis")
st.dataframe(df_filtrado)
