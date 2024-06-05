import json
import os
import uuid

def cadastrar_entradas():
    entrada_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db/entrada.json')
    
    print("\n\n----- Cadastro de Entradas -----")
    
    #verifica se o arquivo db/entrada.json está vazio ou não existe.

    if not os.path.exists(entrada_json) or os.path.getsize(entrada_json) == 0: 
        with open(entrada_json, 'w') as f:
            json.dump([], f)

    with open(entrada_json, 'r') as f:
        entradas = json.load(f)

    nome_entrada = input("\nDigite o nome do entrada: ")
    valor_entrada = float(input("Digite o valor do entrada: "))
    beatpoints_entrada = int(input("Digite os pontos BeatPoints do entrada: "))
    
    novo_id = str(uuid.uuid4())
    novo_entrada = {'id': novo_id, 'nome': nome_entrada, 'valor': valor_entrada, 'beatpoints': beatpoints_entrada}
    entradas.append(novo_entrada)

    with open(entrada_json, 'w') as f:
        json.dump(entradas, f, indent=2)

    print(f"\nentrada '{nome_entrada}' cadastrado com ID {novo_id}.")


def listar_entradas():
    print("\n\n----- Lista de Entradas -----")
    
    entrada_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db/entrada.json')
    if not os.path.exists(entrada_json) or os.path.getsize(entrada_json) == 0:
        print("Nenhum entrada cadastrado.")
        return

    with open(entrada_json, 'r') as f:
        try:
            entradas = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Erro ao carregar dados do arquivo JSON: {e}")
            return

    if not entradas:
        print("Nenhum entrada cadastrado.")
        return

    print("Lista de entradas:")
    for entrada in entradas:
        if isinstance(entrada, dict) and all(key in entrada for key in ['id', 'nome', 'valor', 'beatpoints']) and isinstance(entrada['nome'], str) and isinstance(entrada['valor'], (int, float)) and isinstance(entrada['beatpoints'], int):
            print(f"Id: {entrada['id']}, Nome: {entrada['nome']}, Valor: {entrada['valor']}, BeatPoints: {entrada['beatpoints']}")
        else:
            print(f"Erro: Informações incompletas ou inválidas do entrada: {entrada}")
            
            
    


def editar_entradas():
    
    print("\n\n----- Editar entrada -----")
    entrada_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db/entrada.json')
    

    if not os.path.exists(entrada_json) or os.path.getsize(entrada_json) == 0:
        print("Nenhum entrada cadastrado para editar.")
        return

    with open(entrada_json, 'r') as f:
        entradas = json.load(f)

    print("\nEscolha uma opção para editar:")
    for i, entrada in enumerate(entradas, start=1):
        print(f"{i}. {entrada['nome']}")

    opcao = input("\nDigite o número do entrada que deseja editar: ")

    try:
        opcao = int(opcao)
        if 1 <= opcao <= len(entradas):
            print(f"\nVocê selecionou editar o entrada '{entradas[opcao - 1]['nome']}'.")
            
            novo_nome = input("Digite o novo nome do entrada: ")
            novo_valor = float(input("Digite o novo valor do entrada: "))
            novos_beatpoints = int(input("Digite os novos pontos BeatPoints do entrada: "))

            entradas[opcao - 1]['nome'] = novo_nome
            entradas[opcao - 1]['valor'] = novo_valor
            entradas[opcao - 1]['beatpoints'] = novos_beatpoints

            with open(entrada_json, 'w') as f:
                json.dump(entradas, f, indent=2)

            print("entrada editado com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")
        

def excluir_entradas():
    print("\n\n----- Excluir Entrada -----")
    

    entrada_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db/entrada.json')
    
    if not os.path.exists(entrada_json) or os.path.getsize(entrada_json) == 0:
        print("Nenhum entrada cadastrado.")
        return

    with open(entrada_json, 'r') as f:
        entradas = json.load(f)

    print("\nLista de entradas:")
    for i, entrada in enumerate(entradas, start=1):
        print(f"{i}. {entrada['nome']}")

    opcao = input("\nDigite o número do entrada que deseja excluir: ")

    try:
        opcao = int(opcao)
        if 1 <= opcao <= len(entradas):
            del entradas[opcao - 1]
            with open(entrada_json, 'w') as f:
                json.dump(entradas, f, indent=2)
            print("\nentrada excluído com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")

