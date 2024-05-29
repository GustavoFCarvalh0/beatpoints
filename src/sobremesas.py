import json
import os


def cadastrar_sobremesas():
    sobremesa_json = os.path.join(os.path.dirname(__file__), 'db/sobremesa.json')
    
    print("\n\n----- Cadastro de Sobremesa -----")
    
    #verifica se o arquivo sobremesa.json está vazio ou não existe.

    if not os.path.exists(sobremesa_json) or os.path.getsize(sobremesa_json) == 0: 
        with open(sobremesa_json, 'w') as f:
            json.dump([], f)

    with open(sobremesa_json, 'r') as f:
        sobremesas = json.load(f)

    nome_sobremesa = input("\nDigite o nome do sobremesa: ")
    valor_sobremesa = float(input("Digite o valor do sobremesa: "))
    beatpoints_sobremesa = int(input("Digite os pontos BeatPoints do sobremesa: "))
    
    # Determinando o ID do nova sobremesa
    if sobremesas:
        #Caso ja tenha produto cadastro incrementa mais 1 no id do novo sobremesa
        novo_id = max(sobremesa.get('id', 0) for sobremesa in sobremesas) + 1 
    else:
        novo_id = 1

    novo_sobremesa = {'id': novo_id, 'nome': nome_sobremesa, 'valor': valor_sobremesa, 'beatpoints': beatpoints_sobremesa}
    sobremesas.append(novo_sobremesa)

    with open(sobremesa_json, 'w') as f:
        json.dump(sobremesas, f, indent=2)

    print(f"\nsobremesa '{nome_sobremesa}' cadastrado com ID {novo_id}.")


def listar_sobremesas():
    print("\n\n----- Lista de Sobremesas -----")
    
    sobremesa_json = os.path.join(os.path.dirname(__file__), 'sobremesa.json')
    
    if not os.path.exists(sobremesa_json) or os.path.getsize(sobremesa_json) == 0:
        print("Nenhum sobremesa cadastrado.")
        return

    with open(sobremesa_json, 'r') as f:
        try:
            sobremesas = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Erro ao carregar dados do arquivo JSON: {e}")
            return

    if not sobremesas:
        print("Nenhum sobremesa cadastrado.")
        return

    print("Lista de sobremesas:")
    for sobremesa in sobremesas:
        if isinstance(sobremesa, dict) and all(key in sobremesa for key in ['id', 'nome', 'valor', 'beatpoints']) and isinstance(sobremesa['nome'], str) and isinstance(sobremesa['valor'], (int, float)) and isinstance(sobremesa['beatpoints'], int):
            print(f"Id: {sobremesa['id']}, Nome: {sobremesa['nome']}, Valor: {sobremesa['valor']}, BeatPoints: {sobremesa['beatpoints']}")
        else:
            print(f"Erro: Informações incompletas ou inválidas do sobremesa: {sobremesa}")
            
            
    


def editar_sobremesas():
    
    print("\n\n----- Editar sobremesa -----")
    sobremesa_json = os.path.join(os.path.dirname(__file__), 'sobremesa.json')
    

    if not os.path.exists(sobremesa_json) or os.path.getsize(sobremesa_json) == 0:
        print("Nenhum sobremesa cadastrado para editar.")
        return

    with open(sobremesa_json, 'r') as f:
        sobremesas = json.load(f)

    print("\nEscolha uma opção para editar:")
    for i, sobremesa in enumerate(sobremesas, start=1):
        print(f"{i}. {sobremesa['nome']}")

    opcao = input("\nDigite o número do sobremesa que deseja editar: ")

    try:
        opcao = int(opcao)
        if 1 <= opcao <= len(sobremesas):
            print(f"\nVocê selecionou editar o sobremesa '{sobremesas[opcao - 1]['nome']}'.")
            
            novo_nome = input("Digite o novo nome do sobremesa: ")
            novo_valor = float(input("Digite o novo valor do sobremesa: "))
            novos_beatpoints = int(input("Digite os novos pontos BeatPoints do sobremesa: "))

            sobremesas[opcao - 1]['nome'] = novo_nome
            sobremesas[opcao - 1]['valor'] = novo_valor
            sobremesas[opcao - 1]['beatpoints'] = novos_beatpoints

            with open(sobremesa_json, 'w') as f:
                json.dump(sobremesas, f, indent=2)

            print("sobremesa editado com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")
        

def excluir_sobremesas():
    print("\n\n----- Excluir Sobremesa -----")
    

    sobremesa_json = os.path.join(os.path.dirname(__file__), 'sobremesa.json')
    
    if not os.path.exists(sobremesa_json) or os.path.getsize(sobremesa_json) == 0:
        print("Nenhum sobremesa cadastrado.")
        return

    with open(sobremesa_json, 'r') as f:
        sobremesas = json.load(f)

    print("\nLista de sobremesas:")
    for i, sobremesa in enumerate(sobremesas, start=1):
        print(f"{i}. {sobremesa['nome']}")

    opcao = input("\nDigite o número do sobremesa que deseja excluir: ")

    try:
        opcao = int(opcao)
        if 1 <= opcao <= len(sobremesas):
            del sobremesas[opcao - 1]
            with open(sobremesa_json, 'w') as f:
                json.dump(sobremesas, f, indent=2)
            print("\nsobremesa excluído com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")
        
    
  
  
  
  
  
  