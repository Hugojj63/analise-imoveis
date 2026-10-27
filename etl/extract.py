
import json
from pathlib import Path


CAMINHO_DADOS = (
    Path(__file__).resolve().parent.parent / "data" / "imoveis.json"
)


def extrair_imoveis():
    print("[EXTRACT] Lendo arquivo de imóveis...")

    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        imoveis = json.load(arquivo)

    print(f"[EXTRACT] {len(imoveis)} imóveis extraídos.")

    return imoveis
