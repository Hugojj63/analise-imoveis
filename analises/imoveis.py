from pathlib import Path
import pandas as pd

CAMINHO_DADOS = Path(__file__).resolve().parent.parent / "data" / "imoveis.json"


def carregar_dados(caminho):
    return pd.read_json(caminho)


def calcular_media_preco_cidade(df):
    return df.groupby("cidade")["preco"].mean()


def calcular_media_preco_bairro(df, ordenado=False):
    media_bairro = df.groupby("bairro")["preco"].mean()
    if ordenado:
        return media_bairro.sort_values(ascending=False)
    
    return media_bairro


def calcular_preco_m2(df):
    df["preco_m2"] = df["preco"] / df["area_m2"]
    return df


def calcular_media_preco_m2_cidade(df):
    return df.groupby("cidade")["preco_m2"].mean().sort_values(ascending=False)

def calcular_media_preco_m2_bairro(df, ordenado=False):
    media_bairro = df.groupby("bairro")["preco_m2"].mean()
    if ordenado:
        return media_bairro.sort_values(ascending=False)
    
    return media_bairro

def selecionar_top_bairros(df, maiores=True):
    media_bairro = df.groupby("bairro")["preco_m2"].mean()
    if maiores:
        return media_bairro.sort_values(ascending=False).head()
    else:
        return media_bairro.sort_values(ascending=True).head()



def main():
    df = carregar_dados(CAMINHO_DADOS)

    print(df.shape)
    print("----------------------------------------------------------------")
    df.info()
    print("----------------------------------------------------------------")
    print(df.head())
    print("----------------------------------------------------------------")
    print(calcular_media_preco_cidade(df))
    print("----------------------------------------------------------------")
    print(calcular_media_preco_bairro(df))
    print("----------------------------------------------------------------")
    print(calcular_media_preco_bairro(df, ordenado=True))
    print("----------------------------------------------------------------")
    df = calcular_preco_m2(df)
    print(df[["preco", "area_m2", "preco_m2"]].head())
    print("----------------------------------------------------------------")
    print(calcular_media_preco_m2_cidade(df))
    print("----------------------------------------------------------------")
    print(calcular_media_preco_m2_bairro(df, ordenado=True))
    print("----------------------------------------------------------------")
    print(selecionar_top_bairros(df, maiores=True).head())
    print("----------------------------------------------------------------")
    print(selecionar_top_bairros(df, maiores=False).head())


if __name__ == "__main__":
    main()