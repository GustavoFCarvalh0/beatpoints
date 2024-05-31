import json
import os


def cadastrar_bebidas():
    bebida_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db/bebida.json')
    
    print("\n\n----- Cadastro de Bebida -----")
    
    #verifica se o arquivo db/bebida.json está vazio ou não existe.

    if not os.path.exists(bebida_json) or os.path.getsize(bebida_json) == 0: 
        with open(bebida_json, 'w') as f:
            json.dump([], f)

    with open(bebida_json, 'r') as f:
        bebidas = json.load(f)

    nome_bebida = input("\nDigite o nome do bebida: ")
    valor_bebida = float(input("Digite o valor do bebida: "))
    beatpoints_bebida = int(input("Digite os pontos BeatPoints do bebida: "))
    
    # Determinando o ID do nova bebida
    if bebidas:
        #Caso ja tenha produto cadastro incrementa mais 1 no id do novo bebida
        novo_id = max(bebida.get('id', 0) for bebida in bebidas) + 1 
    else:
        novo_id = 1

    novo_bebida = {'id': novo_id, 'nome': nome_bebida, 'valor': valor_bebida, 'beatpoints': beatpoints_bebida}
    bebidas.append(novo_bebida)

    with open(bebida_json, 'w') as f:
        json.dump(bebidas, f, indent=2)

    print(f"\nbebida '{nome_bebida}' cadastrado com ID {novo_id}.")


def listar_bebidas():
    print("\n\n----- Lista de Bebidas -----")
    
    bebida_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db/bebida.json')
    
    if not os.path.exists(bebida_json) or os.path.getsize(bebida_json) == 0:
        print("Nenhum bebida cadastrado.")
        return

    with open(bebida_json, 'r') as f:
        try:
            bebidas = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Erro ao carregar dados do arquivo JSON: {e}")
            return

    if not bebidas:
        print("Nenhum bebida cadastrado.")
        return

    print("Lista de bebidas:")
    for bebida in bebidas:
        if isinstance(bebida, dict) and all(key in bebida for key in ['id', 'nome', 'valor', 'beatpoints']) and isinstance(bebida['nome'], str) and isinstance(bebida['valor'], (int, float)) and isinstance(bebida['beatpoints'], int):
            print(f"Id: {bebida['id']}, Nome: {bebida['nome']}, Valor: {bebida['valor']}, BeatPoints: {bebida['beatpoints']}")
        else:
            print(f"Erro: Informações incompletas ou inválidas do bebida: {bebida}")
            
            
    


def editar_bebidas():
    
    print("\n\n----- Editar Bebida -----")
    bebida_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db/bebida.json')
    

    if not os.path.exists(bebida_json) or os.path.getsize(bebida_json) == 0:
        print("Nenhum bebida cadastrado para editar.")
        return

    with open(bebida_json, 'r') as f:
        bebidas = json.load(f)

    print("\nEscolha uma opção para editar:")
    for i, bebida in enumerate(bebidas, start=1):
        print(f"{i}. {bebida['nome']}")

    opcao = input("\nDigite o número do bebida que deseja editar: ")

    try:
        opcao = int(opcao)
        if 1 <= opcao <= len(bebidas):
            print(f"\nVocê selecionou editar o bebida '{bebidas[opcao - 1]['nome']}'.")
            
            novo_nome = input("Digite o novo nome do bebida: ")
            novo_valor = float(input("Digite o novo valor do bebida: "))
            novos_beatpoints = int(input("Digite os novos pontos BeatPoints do bebida: "))

            bebidas[opcao - 1]['nome'] = novo_nome
            bebidas[opcao - 1]['valor'] = novo_valor
            bebidas[opcao - 1]['beatpoints'] = novos_beatpoints

            with open(bebida_json, 'w') as f:
                json.dump(bebidas, f, indent=2)

            print("bebida editado com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")
        

def excluir_bebidas():
    print("\n\n----- Excluir Bebida -----")
    

    bebida_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db/bebida.json')
    
    if not os.path.exists(bebida_json) or os.path.getsize(bebida_json) == 0:
        print("Nenhum bebida cadastrado.")
        return

    with open(bebida_json, 'r') as f:
        bebidas = json.load(f)

    print("\nLista de bebidas:")
    for i, bebida in enumerate(bebidas, start=1):
        print(f"{i}. {bebida['nome']}")

    opcao = input("\nDigite o número do bebida que deseja excluir: ")

    try:
        opcao = int(opcao)
        if 1 <= opcao <= len(bebidas):
            del bebidas[opcao - 1]
            with open(bebida_json, 'w') as f:
                json.dump(bebidas, f, indent=2)
            print("\nbebida excluído com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")
