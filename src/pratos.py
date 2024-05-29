import json
import os


def cadastrar_pratos():
    prato_json = os.path.join(os.path.dirname(__file__), 'prato.json')
    
    print("\n\n----- Cadastro de Pratos -----")
    
    #verifica se o arquivo prato.json está vazio ou não existe.

    if not os.path.exists(prato_json) or os.path.getsize(prato_json) == 0: 
        with open(prato_json, 'w') as f:
            json.dump([], f)

    with open(prato_json, 'r') as f:
        pratos = json.load(f)

    nome_prato = input("\nDigite o nome do prato: ")
    valor_prato = float(input("Digite o valor do prato: "))
    beatpoints_prato = int(input("Digite os pontos BeatPoints do prato: "))
    
    # Determinando o ID do nova prato
    if pratos:
        #Caso ja tenha produto cadastro incrementa mais 1 no id do novo prato
        novo_id = max(prato.get('id', 0) for prato in pratos) + 1 
    else:
        novo_id = 1

    novo_prato = {'id': novo_id, 'nome': nome_prato, 'valor': valor_prato, 'beatpoints': beatpoints_prato}
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
        try:
            pratos = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Erro ao carregar dados do arquivo JSON: {e}")
            return

    if not pratos:
        print("Nenhum prato cadastrado.")
        return

    print("Lista de Pratos:")
    for prato in pratos:
        if isinstance(prato, dict) and all(key in prato for key in ['id', 'nome', 'valor', 'beatpoints']) and isinstance(prato['nome'], str) and isinstance(prato['valor'], (int, float)) and isinstance(prato['beatpoints'], int):
            print(f"Id: {prato['id']}, Nome: {prato['nome']}, Valor: {prato['valor']}, BeatPoints: {prato['beatpoints']}")
        else:
            print(f"Erro: Informações incompletas ou inválidas do prato: {prato}")
            
            
    


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
            novo_valor = float(input("Digite o novo valor do prato: "))
            novos_beatpoints = int(input("Digite os novos pontos BeatPoints do prato: "))

            pratos[opcao - 1]['nome'] = novo_nome
            pratos[opcao - 1]['valor'] = novo_valor
            pratos[opcao - 1]['beatpoints'] = novos_beatpoints

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
    
          
  
        
        
        

