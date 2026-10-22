import json
from pathlib import Path
from fastapi import FastAPI

app = FastAPI()

CAMINHO_DADOS = Path(__file__).resolve().parent.parent / "data" / "imoveis.json"

@app.get("/sobre")
def inicio():
	return {"mensagem": "API de imóveis"}



@app.get("/imoveis")
def listar_imoveis():
    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        imoveis = json.load(arquivo)

    return imoveis