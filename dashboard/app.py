
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

df = pd.read_json(CAMINHO_DADOS)

total_imoveis = df.shape[0]

media_preco = df["preco"].mean()
media_area = df["area_m2"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total de imóveis", total_imoveis)
col2.metric("Preço médio", f"R$ {media_preco:,.2f}")
col3.metric("Área média", f"{media_area:,.2f} m²")

preco_por_cidade = df.groupby("cidade")["preco"].mean()

st.subheader("Preço médio dos imóveis por cidade")
st.bar_chart(preco_por_cidade)

df["preco_m2"] = df["preco"] / df["area_m2"]

preco_m2_por_bairro = df.groupby("bairro")["preco_m2"].mean()

st.subheader("Preço médio por metro quadrado por bairro")
st.bar_chart(preco_m2_por_bairro)

st.subheader("Dados dos imóveis")
st.dataframe(df)
