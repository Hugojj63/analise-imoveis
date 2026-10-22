
import json
from pathlib import Path
from fastapi import APIRouter, Query

router = APIRouter()

CAMINHO_DADOS = Path(__file__).resolve().parent.parent / "data" / "imoveis.json"


@router.get("/sobre")
def inicio():
    return {"mensagem": "API de imóveis"}


@router.get("/imoveis")
def listar_imoveis(cidade: str | None = None,pagina: int = Query(default=1, ge=1,description="Número da página, começando em 1"),limite: int = Query(default=10,ge=1,le=100,description="Quantidade de imóveis por página (de 1 a 100)")):


    imoveis_filtrados = []

    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        imoveis = json.load(arquivo)

    if cidade is None:
        imoveis_filtrados = imoveis
    else:
        for linha in imoveis:
            if linha["cidade"] == cidade:
                imoveis_filtrados.append(linha)

    inicio = (pagina - 1) * limite
    fim = inicio + limite

    return imoveis_filtrados[inicio:fim]
