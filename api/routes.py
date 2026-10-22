
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
    tipo: Literal["Apartamento", "Casa", "Terreno", "Kitnet"] | None = None,
    preco_max: int | None = Query(
        default=None,
        ge=0,
		description="filtrar por preco maximo "
	),
	preco_min: int | None = Query(
        default=None,
        ge=0,
		description="filtrar por preco minimo"
	),
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
    ordem: Literal["id", "menor_preco", "maior_preco"] = Query(
    default="id",
    description="Ordenação dos imóveis por ID ou preço"
    ),  
):
    imoveis_filtrados = []

    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        imoveis = json.load(arquivo)
    cidades = sorted(set(imovel["cidade"] for imovel in imoveis))

    if cidade is not None and cidade not in cidades:
        raise HTTPException(
            status_code=404,
            detail={
                "mensagem": "Cidade não encontrada",
                "cidades_cadastradas": cidades
        }
    )

    if cidade is None:
        imoveis_filtrados = imoveis
    else:
        for linha in imoveis:
            if linha["cidade"] == cidade:
                imoveis_filtrados.append(linha)

    if tipo is not None:
        imoveis_por_tipo = []
        for linha in imoveis_filtrados:
            
            if linha["tipo"] == tipo:
                imoveis_por_tipo.append(linha)
        imoveis_filtrados = imoveis_por_tipo


    if preco_min is not None:
        imoveis_por_preco_min = []
        for linha in imoveis_filtrados:		
            if linha["preco"] >= preco_min:
                imoveis_por_preco_min.append(linha)
        imoveis_filtrados = imoveis_por_preco_min

    if preco_max is not None:
        imoveis_por_preco_max = []
        for linha in imoveis_filtrados:
            if linha["preco"] <= preco_max:
                imoveis_por_preco_max.append(linha)
        imoveis_filtrados = imoveis_por_preco_max




    if ordem == "id":
        imoveis_ordenados = sorted(
            imoveis_filtrados,
            key=lambda item: item["id"]
    )
    elif ordem == "menor_preco":
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
