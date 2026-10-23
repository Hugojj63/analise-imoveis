
from fastapi.testclient import TestClient
from api.main import app
import pytest

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


def test_filtrar_imoveis_por_cidade():
    resposta = client.get("/imoveis", params={"cidade": "Curitiba"})
    assert resposta.status_code == 200
    assert len(resposta.json()) > 0
    for imovel in resposta.json():
        assert imovel["cidade"] == "Curitiba"


def test_filtrar_imoveis_por_tipo():
    resposta = client.get("/imoveis", params={"tipo": "Apartamento"})
    assert resposta.status_code == 200
    assert len(resposta.json()) > 0
    for imovel in resposta.json():
        assert imovel["tipo"] == "Apartamento"


def test_filtrar_por_preco_minimo():
    resposta = client.get("/imoveis", params={"preco_min": 200000})
    assert resposta.status_code == 200
    for imovel in resposta.json():
        assert imovel["preco"] >= 200000


def test_filtrar_por_preco_maximo():
    resposta = client.get("/imoveis", params={"preco_max": 300000})
    assert resposta.status_code == 200
    for imovel in resposta.json():
        assert imovel["preco"] <= 300000


def test_paginacao():
    resposta = client.get("/imoveis", params={"pagina": 1, "limite": 5})
    assert resposta.status_code == 200
    assert len(resposta.json()) <= 5
    assert len(resposta.json()) > 0


def test_ordenar_por_menor_preco():
    resposta = client.get("/imoveis",params={"ordem": "menor_preco", "limite": 10})
    assert resposta.status_code == 200
    imoveis = resposta.json()
    precos = [imovel["preco"] for imovel in imoveis]
    assert precos == sorted(precos)


def test_ordenar_por_maior_preco():
    resposta = client.get("/imoveis",params={"ordem": "maior_preco", "limite": 10})
    assert resposta.status_code == 200
    precos = [imovel["preco"] for imovel in resposta.json()]
    assert precos == sorted(precos, reverse=True)


def test_rejeitar_tipo_invalido():
    resposta = client.get("/imoveis",params={"tipo": "Fazenda"})
    assert resposta.status_code == 422



def test_media_preco_por_cidade():
    resposta = client.get("/analises/preco-cidade")
    assert resposta.status_code == 200
    resultado = resposta.json()
    assert isinstance(resultado, dict)
    assert "Curitiba" in resultado
    assert resultado["Curitiba"] == pytest.approx(843554.8387)


def test_media_preco_por_bairro_ordenado():
    resposta = client.get("/analises/preco-bairro", params={"ordenado": True})
    assert resposta.status_code == 200
    medias = resposta.json()
    precos = list(medias.values())
    assert precos == sorted(precos, reverse=True)


def test_media_preco_m2_por_cidade():
    resposta = client.get("/analises/preco-m2-cidade")
    assert resposta.status_code == 200
    resultado = resposta.json()
    assert isinstance(resultado, dict)
    assert "Curitiba" in resultado
    assert resultado["Curitiba"] == pytest.approx(6673.804929)

def test_media_preco_ptest_media_preco_m2_por_bairro_ordenadoor_bairro_ordenado():
    resposta = client.get("/analises/preco-m2-bairro", params={"ordenado": True})
    assert resposta.status_code == 200
    medias = resposta.json()
    precos = list(medias.values())
    assert precos == sorted(precos, reverse=True)



