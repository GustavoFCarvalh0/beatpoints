import json
import os

def cadastrar_entradas():
    print("\n\n----- Cadastro de Entradas -----")
    
    
    entrada_json = os.path.join(os.path.dirname(__file__), 'entrada.json')

    if not os.path.exists(entrada_json):
        with open(entrada_json, 'w') as f:
            json.dump([], f)

    if os.path.getsize(entrada_json) > 0:
        with open(entrada_json, 'r') as f:
            entradas = json.load(f)
    else:
        entradas = []

    nome_entrada = input("\nDigite o nome do entrada: ")
    
    # Determinando o ID do nova entrada
    if entradas:
        novo_id = max(entrada.get('id', 0) for entrada in entradas) + 1 #Caso ja tenha produto cadastro incrementa mais 1 no id do novo entrada
    else:
        novo_id = 1

    nova_entrada = {'id': novo_id, 'nome': nome_entrada}
    entradas.append(nova_entrada)

    with open(entrada_json, 'w') as f:
        json.dump(entradas, f, indent=2)

    print(f"\nentrada '{nome_entrada}' cadastrado com ID {novo_id}.")


def listar_entradas():
    print("\n\n----- Lista de Entradas -----")
    
    
    entrada_json = os.path.join(os.path.dirname(__file__), 'entrada.json')

    if not os.path.exists(entrada_json) or os.path.getsize(entrada_json) == 0:
        print("Nenhum entrada cadastrado.")
        return

    with open(entrada_json, 'r') as f:
        entradas = json.load(f)

    print("Lista de entradas:")
    for entrada in entradas:
        if 'id' in entrada and 'nome' in entrada:
            print(f"{entrada['id']}. {entrada['nome']}")
        else:
            print("entrada inválido: ", entrada)

def editar_entradas():
    print("\n\n----- Editar Entrada -----")

    entrada_json = os.path.join(os.path.dirname(__file__), 'entrada.json')

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

            entradas[opcao - 1]['nome'] = novo_nome

            with open(entrada_json, 'w') as f:
                json.dump(entradas, f, indent=2)

            print("entrada editado com sucesso!")
        else:
            print("\nOpção inválida!")
    except ValueError:
        print("\nOpção inválida! Digite um número inteiro.")

    # Após a edição, voltar ao menu principal
    return


def excluir_entradas():
    print("\n\n----- Excluir Entrada -----")

    entrada_json = os.path.join(os.path.dirname(__file__), 'entrada.json')

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
        
while True:
    print("\n\nEscolha uma opção:")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Editar")
    print("4. Excluir")
    print("5. Sair")
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == '1':
        cadastrar_entradas()
    elif opcao == '2':
        listar_entradas()
    elif opcao == '3':
        editar_entradas()
    elif opcao == '4':
        excluir_entradas()
    elif opcao == '5':
        print("\nAté mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
