import json
import os

def cadastrar_bebidas():
    print("\n\n----- Cadastro de Bebidas -----")
 
    bebida_json = os.path.join(os.path.dirname(__file__), 'bebida.json')

    if not os.path.exists(bebida_json):
        with open(bebida_json, 'w') as f:
            json.dump([], f)

    if os.path.getsize(bebida_json) > 0:
        with open(bebida_json, 'r') as f:
            bebidas = json.load(f)
    else:
        bebidas = []

    nome_bebida = input("\nDigite o nome do bebida: ")
    
    # Determinando o ID do novo bebida
    if bebidas:
        novo_id = max(bebida.get('id', 0) for bebida in bebidas) + 1 #Caso ja tenha produto cadastro incrementa mais 1 no id do novo bebida
    else:
        novo_id = 1

    novo_bebida = {'id': novo_id, 'nome': nome_bebida}
    bebidas.append(novo_bebida)

    with open(bebida_json, 'w') as f:
        json.dump(bebidas, f, indent=2)

    print(f"\nbebida '{nome_bebida}' cadastrado com ID {novo_id}.")


def listar_bebidas():
    print("\n\n----- Lista de Bebibas -----")
  
    bebida_json = os.path.join(os.path.dirname(__file__), 'bebida.json')

    if not os.path.exists(bebida_json) or os.path.getsize(bebida_json) == 0:
        print("Nenhum bebida cadastrado.")
        return

    with open(bebida_json, 'r') as f:
        bebidas = json.load(f)

    print("Lista de bebidas:")
    for bebida in bebidas:
        if 'id' in bebida and 'nome' in bebida:
            print(f"{bebida['id']}. {bebida['nome']}")
        else:
            print("bebida inválido: ", bebida)

def editar_bebidas():
    print("\n\n----- Editar Bebida -----")
   
    bebida_json = os.path.join(os.path.dirname(__file__), 'bebida.json')

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

            bebidas[opcao - 1]['nome'] = novo_nome

            with open(bebida_json, 'w') as f:
                json.dump(bebidas, f, indent=2)

            print("bebida editado com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")

    # Após a edição, voltar ao menu principal
    return


def excluir_bebidas():
    print("\n\n----- Excluir Bebida -----")

    bebida_json = os.path.join(os.path.dirname(__file__), 'bebida.json')

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
        
        
while True:
    print("\n\nEscolha uma opção:")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Editar")
    print("4. Excluir")
    print("5. Sair")
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == '1':
        cadastrar_bebidas()
    elif opcao == '2':
        listar_bebidas()
    elif opcao == '3':
        editar_bebidas()
    elif opcao == '4':
        excluir_bebidas()
    elif opcao == '5':
        print("\nAté mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
