
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_sobre():
    resposta = client.get("/sobre")

    assert resposta.status_code == 200
    assert resposta.json() == {"mensagem": "API de imóveis"}

def test_listar_imoveis():
    resposta = client.get("/imoveis")

    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)
    assert len(resposta.json()) > 0


def test_buscar_imovel_existente():
    resposta = client.get("/imoveis/1")

    assert resposta.status_code == 200
    assert resposta.json()["id"] == 1


def test_buscar_imovel_inexistente():
    resposta = client.get("/imoveis/999999")

    assert resposta.status_code == 404
