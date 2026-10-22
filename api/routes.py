import json
from pathlib import Path
from fastapi import APIRouter

router = APIRouter()

CAMINHO_DADOS = Path(__file__).resolve().parent.parent / "data" / "imoveis.json"

@router.get("/sobre")
def inicio():
	return {"mensagem": "API de imóveis"}


@router.get("/imoveis")
def listar_imoveis(cidade=None):
    imoveis_filtrados = []

    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        imoveis = json.load(arquivo)

    if cidade is None:
        return imoveis
    else:
        for linha in imoveis:
            if linha["cidade"] == cidade:
                imoveis_filtrados.append(linha)

    return imoveis_filtrados