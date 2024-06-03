import json
import os

def carregar_menu():
    # Atribuindo a variável o caminho do arquivo .json dinamicamente
    caminho = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(_file_))), f'db/entrada.json')

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
        print(f"{opcao['id']}. {opcao['nome']} - R${opcao['preco']:.2f}")
        
        
def cardapio_main():
    # Carrega os menus a partir dos arquivos JSON
    entradas = carregar_menu('entradas.json')
    pratos = carregar_menu('pratos.json')
    bebidas = carregar_menu('bebidas.json')
    sobremesas = carregar_menu('sobremesas.json')

    while True:
        print("\n------  BeatPoints  ------")
        print("Escolha um item do menu:")
        print("1. Entradas")
        print("2. Pratos principais")
        print("3. Bebidas")
        print("4. Sobremesas")
        print("5. Voltar")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            print("\nEntradas:")
            exibir_opcoes(entradas)
            sub_opcao = input("Digite o número do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue

        elif opcao == '2':
            print("\nPratos Principais:")
            exibir_opcoes(pratos)
            sub_opcao = input("Digite o número do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue

        elif opcao == '3':
            print("\nBebidas:")
            exibir_opcoes(bebidas)
            sub_opcao = input("Digite o número do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue

        elif opcao == '4':
            print("\nSobremesas:")
            exibir_opcoes(sobremesas)
            sub_opcao = input("Digite o número do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue

        elif opcao == '5':
            break
        
        else:
            print("Opção inválida!")