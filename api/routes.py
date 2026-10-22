import json
from pathlib import Path
from fastapi import APIRouter

router = APIRouter()
CAMINHO_DADOS = Path(__file__).resolve().parent.parent / "data" / "imoveis.json"

@router.get("/sobre")
def inicio():
	return {"mensagem": "API de imóveis"}


@router.get("/imoveis")
def listar_imoveis():
    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        imoveis = json.load(arquivo)

    return imoveis