
import pandas as pd


def transformar_imoveis(imoveis):
    print("[TRANSFORM] Iniciando transformação dos imóveis...")

    df = pd.DataFrame(imoveis)

    colunas_obrigatorias = [
        "id",
        "tipo",
        "cidade",
        "bairro",
        "preco",
        "area_m2",
        "quartos",
        "banheiros"
    ]

    for coluna in colunas_obrigatorias:
        if coluna not in df.columns:
            raise ValueError(
                f"Coluna obrigatória ausente: {coluna}"
            )

    quantidade_inicial = len(df)

    df = df.drop_duplicates(subset="id")

    print(
        f"[TRANSFORM] Registros recebidos: {quantidade_inicial}"
    )
    print(
        f"[TRANSFORM] Registros após remover IDs duplicados: {len(df)}"
    )

    colunas_numericas = [
        "id",
        "preco",
        "area_m2",
        "quartos",
        "banheiros"
    ]

    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(df[coluna],errors="raise")

    if df[colunas_obrigatorias].isnull().any().any():
        raise ValueError("Existem campos obrigatórios sem valores.")

    if (df["id"] <= 0).any():
        raise ValueError("Os IDs devem ser positivos.")

    if (df["preco"] < 0).any():
        raise ValueError("Os preços não podem ser negativos.")

    if (df["area_m2"] <= 0).any():
        raise ValueError("A área dos imóveis deve ser positiva.")

    if (df[["quartos", "banheiros"]] < 0).any().any():
        raise ValueError(
            "Quartos e banheiros não podem ser negativos."
        )

    imoveis_tratados = df.to_dict(orient="records")

    print(
        f"[TRANSFORM] Transformação concluída: "
        f"{len(imoveis_tratados)} imóveis preparados."
    )

    return imoveis_tratados
