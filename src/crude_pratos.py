import json
import os

def cadastrar_pratos():
    
    prato_json = os.path.join(os.path.dirname(__file__), 'prato.json')
    
    print("\n\n----- Cadastro de Pratos -----")

    if not os.path.exists(prato_json):
        with open(prato_json, 'w') as f:
            json.dump([], f)

    if os.path.getsize(prato_json) > 0:
        with open(prato_json, 'r') as f:
            pratos = json.load(f)
    else:
        pratos = []

    nome_prato = input("\nDigite o nome do prato: ")
    
    # Determinando o ID do novo prato
    if pratos:
        novo_id = max(prato.get('id', 0) for prato in pratos) + 1 #Caso já tenha produto cadastrado, incrementa mais 1 no id do novo prato
    else:
        novo_id = 1

    novo_prato = {'id': novo_id, 'nome': nome_prato}
    pratos.append(novo_prato)

    with open(prato_json, 'w') as f:
        json.dump(pratos, f, indent=2)

    print(f"\nPrato '{nome_prato}' cadastrado com ID {novo_id}.")


def listar_pratos():
    print("\n\n----- Lista de Pratos -----")
    
    prato_json = os.path.join(os.path.dirname(__file__), 'prato.json')
    
    
    if not os.path.exists(prato_json) or os.path.getsize(prato_json) == 0:
        print("Nenhum prato cadastrado.")
        return

    with open(prato_json, 'r') as f:
        pratos = json.load(f)

    if not pratos:
        print("Nenhum prato cadastrado.")
        return

    print("Lista de Pratos:")
    for prato in pratos:
        if isinstance(prato, dict) and 'nome' in prato and isinstance(prato['nome'], str):
            print(f"{prato['nome']}")

def editar_pratos():
    
    print("\n\n----- Editar Prato -----")
    prato_json = os.path.join(os.path.dirname(__file__), 'prato.json')
    

    if not os.path.exists(prato_json) or os.path.getsize(prato_json) == 0:
        print("Nenhum prato cadastrado para editar.")
        return

    with open(prato_json, 'r') as f:
        pratos = json.load(f)

    print("\nEscolha uma opção para editar:")
    for i, prato in enumerate(pratos, start=1):
        print(f"{i}. {prato['nome']}")

    opcao = input("\nDigite o número do prato que deseja editar: ")

    try:
        opcao = int(opcao)
        if 1 <= opcao <= len(pratos):
            print(f"\nVocê selecionou editar o prato '{pratos[opcao - 1]['nome']}'.")
            
            novo_nome = input("Digite o novo nome do prato: ")

            pratos[opcao - 1]['nome'] = novo_nome

            with open(prato_json, 'w') as f:
                json.dump(pratos, f, indent=2)

            print("Prato editado com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")

def excluir_pratos():
    print("\n\n----- Excluir Prato -----")
    
    
    
    prato_json = os.path.join(os.path.dirname(__file__), 'prato.json')
    

    if not os.path.exists(prato_json) or os.path.getsize(prato_json) == 0:
        print("Nenhum prato cadastrado.")
        return

    with open(prato_json, 'r') as f:
        pratos = json.load(f)

    print("\nLista de Pratos:")
    for i, prato in enumerate(pratos, start=1):
        print(f"{i}. {prato['nome']}")

    opcao = input("\nDigite o número do prato que deseja excluir: ")

    try:
        opcao = int(opcao)
        if 1 <= opcao <= len(pratos):
            del pratos[opcao - 1]
            with open(prato_json, 'w') as f:
                json.dump(pratos, f, indent=2)
            print("\nPrato excluído com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")
        
def mostrar_pratos():      
    while True:
        print("\n\nEscolha uma opção:")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        print("5. Sair")
        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == '1':
            cadastrar_pratos()
        elif opcao == '2':
            listar_pratos()
        elif opcao == '3':
            editar_pratos()
        elif opcao == '4':
            excluir_pratos()
        elif opcao == '5':
            print("\nAté mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
        
        
        

