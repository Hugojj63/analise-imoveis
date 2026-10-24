# 🏠 Analista de Imóveis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

> Projeto de análise de dados imobiliários utilizando Python, Pandas, FastAPI e Streamlit.

---

## Sobre o projeto

O **Analista de Imóveis** é um projeto de portfólio desenvolvido para explorar dados do mercado imobiliário por meio de análise de dados, visualização de indicadores e disponibilização de informações por uma API REST.

A aplicação utiliza uma base de dados com 1.000 registros sintéticos de imóveis, permitindo analisar preços, áreas, tipos de imóveis, cidades e bairros.

O projeto reúne uma API desenvolvida com FastAPI e um dashboard interativo desenvolvido com Streamlit, permitindo consultar os dados, aplicar filtros e exportar os resultados para CSV.

## Funcionalidades

- Análise de uma base com 1.000 imóveis sintéticos.
- API REST desenvolvida com FastAPI.
- Documentação interativa da API com Swagger UI.
- Dashboard interativo com Streamlit.
- Filtros por cidade, tipo de imóvel e faixa de preço.
- Opção para visualizar imóveis de todas as cidades.
- Indicadores de quantidade de imóveis, preço médio, mediana dos preços e área média.
- Gráficos de preço médio e preço médio por metro quadrado por bairro.
- Botão para limpar os filtros e restaurar os valores padrão.
- Mensagem informativa quando os filtros não retornam resultados.
- Exportação dos imóveis filtrados para CSV.
- Testes automatizados da API com Pytest.

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal do projeto |
| Pandas | Manipulação, filtragem e análise dos dados |
| FastAPI | Desenvolvimento da API REST |
| Streamlit | Construção do dashboard interativo |
| Pytest | Testes automatizados |
| JSON | Armazenamento local dos dados dos imóveis |
| CSV | Exportação dos dados filtrados |
| Git e GitHub | Versionamento e hospedagem do código |

## Indicadores analisados

O dashboard apresenta indicadores e gráficos para explorar os dados imobiliários:

- **Total de imóveis:** quantidade de registros após a aplicação dos filtros.
- **Preço médio:** média dos preços dos imóveis selecionados.
- **Mediana dos preços:** valor central dos preços dos imóveis selecionados.
- **Área média:** média das áreas dos imóveis selecionados.
- **Preço médio por bairro:** comparação dos preços médios entre bairros.
- **Preço médio por m²:** comparação do preço por metro quadrado entre bairros.

Os indicadores e gráficos são atualizados de acordo com os filtros selecionados no dashboard.

## Estrutura do projeto

```text
Projeto Analista de Imóveis/
├── analises/
│   └── imoveis.py
├── api/
│   ├── main.py
│   └── routes.py
├── dashboard/
│   └── app.py
├── data/
│   └── imoveis.json
├── tests/
│   └── test_api.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar o projeto

### Pré-requisitos

- Python 3.12 ou uma versão compatível com as dependências do projeto.
- Git instalado.
- Um terminal, como o terminal integrado do VS Code.

### 1. Clone o repositório

```bash
git clone https://github.com/Hugojj63/analise-imoveis.git
cd analise-imoveis
```

### 2. Crie um ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

### 3. Ative o ambiente virtual

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

```powershell
python -m pip install -r requirements.txt
```

### 5. Execute o dashboard

Na raiz do projeto, execute:

```powershell
python -m streamlit run dashboard/app.py
```

O Streamlit disponibilizará o endereço local no terminal, normalmente:

http://localhost:8501

### 6. Execute a API

Abra outro terminal, mantendo o ambiente virtual ativado, e execute:

```powershell
uvicorn api.main:app --reload
```

A API ficará disponível localmente em:

http://127.0.0.1:8000

A documentação interativa pode ser acessada em:

http://127.0.0.1:8000/docs

### 7. Execute os testes automatizados

Na raiz do projeto, execute:

```powershell
python -m pytest
```

Os testes verificam os comportamentos definidos na suíte de testes da API.

## Exportação de dados

O dashboard permite baixar os imóveis correspondentes aos filtros selecionados em um arquivo CSV.

O arquivo pode ser aberto em ferramentas de planilhas, como Microsoft Excel, ou utilizado posteriormente em outras ferramentas de análise de dados.

## Próximas etapas

- Integrar os dados imobiliários ao Power BI.
- Desenvolver relatórios complementares de Business Intelligence.
- Explorar novas formas de consulta e análise dos dados.
- Avaliar a utilização de um banco de dados relacional em uma evolução futura do projeto.

## Objetivo do projeto

Este projeto tem como objetivo consolidar conhecimentos em Python, análise de dados, APIs REST, visualização de informações e testes automatizados, além de demonstrar a aplicação prática dessas tecnologias em um cenário de análise imobiliária.

---

**Status:** Em desenvolvimento.
