import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar_banco():
    print("[LOAD] Conectando ao MySQL...")
    conexao = mysql.connector.connect(host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"))
    print("[LOAD] Conexão estabelecida com sucesso.")
    cursor = conexao.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS analista_imoveis")
    cursor.execute("USE analista_imoveis")
    print("[LOAD] Banco analista_imoveis preparado.")

    return {
        "conexao": conexao,
        "cursor": cursor
    }


def criar_tabela(banco_de_dados):
    print("[LOAD] Criando tabela imoveis...")

    banco_de_dados["cursor"].execute("""
        CREATE TABLE IF NOT EXISTS imoveis (
            id INT PRIMARY KEY,
            tipo VARCHAR(50),
            cidade VARCHAR(100),
            bairro VARCHAR(100),
            preco DECIMAL(12, 2),
            area_m2 DECIMAL(10, 2),
            quartos INT,
            banheiros INT)""")

    banco_de_dados["conexao"].commit()

    print("[LOAD] Tabela imoveis preparada.")



def inserir_imoveis(banco_de_dados, imoveis):
    sql = """
        INSERT INTO imoveis (
            id, tipo, cidade, bairro, preco,
            area_m2, quartos, banheiros
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            tipo = VALUES(tipo),
            cidade = VALUES(cidade),
            bairro = VALUES(bairro),
            preco = VALUES(preco),
            area_m2 = VALUES(area_m2),
            quartos = VALUES(quartos),
            banheiros = VALUES(banheiros)
    """

    dados = [
        (
            imovel["id"],
            imovel["tipo"],
            imovel["cidade"],
            imovel["bairro"],
            imovel["preco"],
            imovel["area_m2"],
            imovel["quartos"],
            imovel["banheiros"]
        )
        for imovel in imoveis
    ]

    print(f"[LOAD] Processando {len(dados)} imóveis...")

    banco_de_dados["cursor"].executemany(sql, dados)
    banco_de_dados["conexao"].commit()

    print("[LOAD] Carga de imóveis concluída.")



def carregar_imoveis(imoveis):
    banco_de_dados = None

    try:
        banco_de_dados = conectar_banco()

        criar_tabela(banco_de_dados)

        inserir_imoveis(banco_de_dados, imoveis)

        print("[LOAD] Processo finalizado com sucesso.")

    except mysql.connector.Error as erro:
        print(f"[LOAD] Erro no banco de dados: {erro}")
        raise

    finally:
        if banco_de_dados is not None:
            banco_de_dados["cursor"].close()
            banco_de_dados["conexao"].close()

            print("[LOAD] Conexão encerrada.")