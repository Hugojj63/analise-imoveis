import json
from pathlib import Path
from fastapi import APIRouter, HTTPException

router = APIRouter()

CAMINHO_DADOS = Path(__file__).resolve().parent.parent / "data" / "imoveis.json"

@router.get("/sobre")
def inicio():
	return {"mensagem": "API de imóveis"}


@router.get("/imoveis")

def listar_imoveis(cidade: str | None = None, pagina: int = 1, limite: int = 10):
    if limite < 1 or pagina < 1:
        raise HTTPException(
            status_code=400,
            detail="A página e o limite devem ser maiores que zero"
    )
    if limite > 100:
        raise HTTPException(
			status_code=400,
			detail="O limite máximo é 100 imóveis por requisição"
	)
    
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
