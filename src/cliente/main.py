from gerente.bebidas import cadastrar_bebidas, listar_bebidas
from gerente.entradas import cadastrar_entradas, listar_entradas
from gerente.pratos import cadastrar_pratos, listar_pratos
from gerente.sobremesas import cadastrar_sobremesas, listar_sobremesas
from cliente.cardapio import carregar_menu, exibir_opcoes

def adicionar_carrinho(carrinho, item):
    carrinho.append(item)
    print(f"Item adicionado ao carrinho: {item['nome']}")

def listar_carrinho(carrinho):
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        print("\nItens no carrinho:")
        for idx, item in enumerate(carrinho, 1):
            print(f"{idx}. {item['nome']} - {item['valor']}")

def remover_do_carrinho(carrinho):
    listar_carrinho(carrinho)
    if not carrinho:
        return
    idx_remover = int(input("Digite o número do item que deseja remover ou 0 para cancelar: "))
    if idx_remover == 0:
        return
    if 0 < idx_remover <= len(carrinho):
        item_removido = carrinho.pop(idx_remover - 1)
        print(f"Item removido do carrinho: {item_removido['nome']}")
    else:
        print("Índice inválido!")

def cliente_main():
    # Carrega os menus a partir dos arquivos JSON
    entradas = carregar_menu('entrada.json')
    pratos = carregar_menu('prato.json')
    bebidas = carregar_menu('bebida.json')
    sobremesas = carregar_menu('sobremesa.json')

    carrinho = []

    while True:
        print("\n------  BeatPoints  ------")
        print("Escolha uma opção:")
        print("1. Entradas")
        print("2. Pratos principais")
        print("3. Bebidas")
        print("4. Sobremesas")
        print("5. Ver carrinho")
        print("6. Remover item do carrinho")
        print("7. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            print("\nEntradas:")
            exibir_opcoes(entradas)
            sub_opcao = input("\nDigite o número(ID) do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue
            else: 
                for entrada in entradas:
                    if int(sub_opcao) == entrada["id"]:
                        adicionar_carrinho(carrinho, entrada)

        elif opcao == '2':
            print("\nPratos Principais:")
            exibir_opcoes(pratos)
            sub_opcao = input("Digite o número(ID) do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue
            else:
                for prato in pratos:
                    if int(sub_opcao) == prato["id"]:
                        adicionar_carrinho(carrinho, prato)

        elif opcao == '3':
            print("\nBebidas:")
            exibir_opcoes(bebidas)
            sub_opcao = input("Digite o número(ID) do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue
            else:
                for bebida in bebidas:
                    if int(sub_opcao) == bebida["id"]:
                        adicionar_carrinho(carrinho, bebida)

        elif opcao == '4':
            print("\nSobremesas:")
            exibir_opcoes(sobremesas)
            sub_opcao = input("Digite o número(ID) do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue
            else:
                for sobremesa in sobremesas:
                    if int(sub_opcao) == sobremesa["id"]:
                        adicionar_carrinho(carrinho, sobremesa)

        elif opcao == '5':
            listar_carrinho(carrinho)
            
            # dar a opção de chamar o carrinho e finalizar o pedido
            # chamar função adicionar no carrinho, listar, e remover

        elif opcao == '6':
            remover_do_carrinho(carrinho)
            
        elif opcao == '7':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!") 

