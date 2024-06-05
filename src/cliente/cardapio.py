import json
import os

def carregar_menu(caminho):
    # Atribuindo a variável o caminho do arquivo .json dinamicamente
    caminho = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f'db/{caminho}')

    # Verifica se o arquivo existe
    if not os.path.exists(caminho):
        print(f"Erro: O arquivo {caminho} não foi encontrado.")
        return []
    
    # Verifica se o arquivo está vazio
    if os.path.getsize(caminho) == 0:
        print(f"Erro: O arquivo {caminho} está vazio.")
        return []

    # Abre e lê o conteúdo do arquivo JSON
    with open(caminho, 'r') as f:
        return json.load(f)

def exibir_opcoes(opcoes):
    if not opcoes:
        print("Nenhuma opção disponível.")
        return
    for opcao in opcoes:
        print(f"Nome: {opcao['nome']}")
        print(f"\tId: {opcao['id']}")
        print(f"\tValor: {opcao['valor']}")
        print(f"\tBeatPoints: {opcao['beatpoints']}")

