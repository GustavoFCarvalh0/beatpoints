import json
import os

def cadastrar_sobremesas():
    print("\n\n----- Cadastro de Sobremesas -----")

    sobremesa_json = os.path.join(os.path.dirname(__file__), 'sobremesa.json')

    if not os.path.exists(sobremesa_json):
        with open(sobremesa_json, 'w') as f:
            json.dump([], f)

    if os.path.getsize(sobremesa_json) > 0:
        with open(sobremesa_json, 'r') as f:
            sobremesas = json.load(f)
    else:
        sobremesas = []

    nome_sobremesa = input("\nDigite o nome do sobremesa: ")
    
    # Determinando o ID do novo sobremesa
    if sobremesas:
        novo_id = max(sobremesa.get('id', 0) for sobremesa in sobremesas) + 1 #Caso ja tenha produto cadastro incrementa mais 1 no id do novo sobremesa
    else:
        novo_id = 1

    novo_sobremesa = {'id': novo_id, 'nome': nome_sobremesa}
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
        sobremesas = json.load(f)

    print("Lista de sobremesas:")
    for sobremesa in sobremesas:
        if 'id' in sobremesa and 'nome' in sobremesa:
            print(f"{sobremesa['id']}. {sobremesa['nome']}")
        else:
            print("sobremesa inválido: ", sobremesa)

def editar_sobremesas():
    print("\n\n----- Editar Sobremesa -----")

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

            sobremesas[opcao - 1]['nome'] = novo_nome

            with open(sobremesa_json, 'w') as f:
                json.dump(sobremesas, f, indent=2)

            print("sobremesa editado com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")

    # Após a edição, voltar ao menu principal
    return


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
        
        
while True:
    print("\n\nEscolha uma opção:")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Editar")
    print("4. Excluir")
    print("5. Sair")
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == '1':
        cadastrar_sobremesas()
    elif opcao == '2':
        listar_sobremesas()
    elif opcao == '3':
        editar_sobremesas()
    elif opcao == '4':
        excluir_sobremesas()
    elif opcao == '5':
        print("\nAté mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")

  
  
  
  
  
  