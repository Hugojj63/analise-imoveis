
from etl.extract import extrair_imoveis
from etl.transform import transformar_imoveis
from etl.load import carregar_imoveis


def executar_etl():
    print("[ETL] Iniciando pipeline de imóveis...")

    imoveis = extrair_imoveis()

    imoveis_tratados = transformar_imoveis(imoveis)

    carregar_imoveis(imoveis_tratados)

    print("[ETL] Pipeline finalizado com sucesso.")


if __name__ == "__main__":
    executar_etl()
