
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

# Carrega os dados
df = pd.read_json(CAMINHO_DADOS)

# Calcula o preço por metro quadrado
df["preco_m2"] = df["preco"] / df["area_m2"]

# Filtro por cidade
cidades = df["cidade"].unique()
cidade_selecionada = st.selectbox("Selecione uma cidade", cidades)

tipos = df["tipo"].unique()

tipos = ["Todos"] + list(df["tipo"].unique())
tipo_selecionado = st.selectbox("Selecione um tipo", tipos)

if tipo_selecionado == "Todos":
    df_filtrado = df[df["cidade"] == cidade_selecionada].copy()
else:
    df_filtrado = df[(df["cidade"] == cidade_selecionada) &(df["tipo"] == tipo_selecionado)].copy()


# Calcula os indicadores
total_imoveis = df_filtrado.shape[0]
media_preco = df_filtrado["preco"].mean()
media_area = df_filtrado["area_m2"].mean()

# Exibe os indicadores
col1, col2, col3 = st.columns(3)

col1.metric("Total de imóveis", total_imoveis)
col2.metric("Preço médio", f"R$ {media_preco:,.2f}")
col3.metric("Área média", f"{media_area:,.2f} m²")

# Gráfico de preço médio por bairro
preco_por_bairro = df_filtrado.groupby("bairro")["preco"].mean()

st.subheader("Preço médio por bairro")
st.bar_chart(preco_por_bairro)

# Gráfico de preço médio por metro quadrado
preco_m2_por_bairro = df_filtrado.groupby("bairro")["preco_m2"].mean()

st.subheader("Preço médio por m² por bairro")
st.bar_chart(preco_m2_por_bairro)

# Tabela de imóveis filtrados
st.subheader("Dados dos imóveis")
st.dataframe(df_filtrado)
