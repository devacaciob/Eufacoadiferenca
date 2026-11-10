import json
from pathlib import Path

CAMINHO_DADOS = Path(__file__).parent / "dados.json"



def carregar_dados():

    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:

        dados = json.load(arquivo)

    return dados



def salvar_dados(dados):

    with open(CAMINHO_DADOS, "w", encoding="utf-8") as arquivo:

        json.dump(dados, arquivo, indent=4, ensure_ascii=False)