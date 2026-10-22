
import json
from pathlib import Path
from typing import Literal
from fastapi import APIRouter, Query, HTTPException

router = APIRouter()

CAMINHO_DADOS = Path(__file__).resolve().parent.parent / "data" / "imoveis.json"


@router.get("/sobre")
def inicio():
    return {"mensagem": "API de imóveis"}


@router.get("/imoveis")
def listar_imoveis(
    cidade: str | None = None,
    pagina: int = Query(
        default=1,
        ge=1,
        description="Número da página, começando em 1"
    ),
    limite: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Quantidade de imóveis por página (de 1 a 100)"
    ),
    ordem: Literal["menor_preco", "maior_preco"] = Query(
    default="menor_preco",
    description="Ordenação dos imóveis por preço"
)
):
    imoveis_filtrados = []

    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        imoveis = json.load(arquivo)

    if cidade is None:
        imoveis_filtrados = imoveis
    else:
        for linha in imoveis:
            if linha["cidade"] == cidade:
                imoveis_filtrados.append(linha)

    if ordem == "menor_preco":
        imoveis_ordenados = sorted(
            imoveis_filtrados,
            key=lambda item: item["preco"]
        )
    elif ordem == "maior_preco":
        imoveis_ordenados = sorted(
            imoveis_filtrados,
            key=lambda item: item["preco"],
            reverse=True
        )
        
    inicio = (pagina - 1) * limite
    fim = inicio + limite

    return imoveis_ordenados[inicio:fim]


@router.get("/imoveis/{imovel_id}")
def buscar_imovel(imovel_id: int):
    if imovel_id < 1:
        raise HTTPException(
            status_code=400,
            detail="O ID deve ser um número positivo"
        )

    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        imoveis = json.load(arquivo)

    for linha in imoveis:
        if linha["id"] == imovel_id:
            return linha

    raise HTTPException(
        status_code=404,
        detail="Imóvel não encontrado"
    )
