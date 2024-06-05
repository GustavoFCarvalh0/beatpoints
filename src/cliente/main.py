from cliente.cardapio import carregar_menu, exibir_opcoes
from cliente.carrinho import adicionar_carrinho, finalizar_compra, listar_carrinho, remover_carrinho
import sys
import os
import json

def cliente_main():
    # Carrega os menus a partir dos arquivos JSON
    entradas = carregar_menu('entrada.json')
    pratos = carregar_menu('prato.json')
    bebidas = carregar_menu('bebida.json')
    sobremesas = carregar_menu('sobremesa.json')

    while True:
        print("\n------  BeatPoints  ------")
        print("Escolha uma opção:")
        print("1. Entradas")
        print("2. Pratos principais")
        print("3. Bebidas")
        print("4. Sobremesas")
        print("5. Ver carrinho")
        print("6. Remover item do carrinho")
        print("7. Realizar Pagamento")
        print("8. Sair do programa")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            print("\nEntradas:")
            exibir_opcoes(entradas)
            sub_opcao = input("\nDigite o id do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue
            else: 
                for entrada in entradas:
                    if sub_opcao == entrada["id"]:
                        adicionar_carrinho(entrada, 1)
                        print('🎉 Entrada adicionada ao carrinho!')

        elif opcao == '2':
            print("\nPratos Principais:")
            exibir_opcoes(pratos)
            sub_opcao = input("Digite o id do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue
            else:
                for prato in pratos:
                    if sub_opcao == prato["id"]:
                        adicionar_carrinho(prato, 1)
                        print('🎉 Prato principal adicionado ao carrinho!')

        elif opcao == '3':
            print("\nBebidas:")
            exibir_opcoes(bebidas)
            sub_opcao = input("Digite o id do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue
            else:
                for bebida in bebidas:
                    if sub_opcao == bebida["id"]:
                        adicionar_carrinho(bebida, 1)
                        print('🎉 Bebida adicionada ao carrinho!')

        elif opcao == '4':
            print("\nSobremesas:")
            exibir_opcoes(sobremesas)
            sub_opcao = input("Digite o id do item desejado ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue
            else:
                for sobremesa in sobremesas:
                    if sub_opcao == sobremesa["id"]:
                        adicionar_carrinho(sobremesa, 1)
                        print('🎉 Sobremesa adicionada ao carrinho!')

        elif opcao == '5':
            listar_carrinho()

        elif opcao == '6':
            listar_carrinho()
            sub_opcao = input("Digite o id do item para remover ou 'v' para voltar: ")
            if sub_opcao.lower() == 'v':
                continue
            else:
                remover_carrinho(sub_opcao)
            
        elif opcao == '7':
            print("Realizar pagamento...")
            print("🎉 Pagamento realizado com sucesso!")
            usuario_cpf = pegar_usuario_logado_cpf()
            resultado = finalizar_compra()
            if (usuario_cpf):
                print(f"Valor total: {resultado["valor"]}")
                print(f"Quantidade total: {resultado["qtd"]}")
                print(f"Beatpoints total: {resultado["bp"]}")
                adicionar_beatpoints(resultado["bp"])
            else:
                print(f"Valor total: {resultado["valor"]}")
                print(f"Quantidade total: {resultado["qtd"]}")
            sys.exit()
        
        elif opcao == '8':
            print("Saindo...")
            print("🎉 Volte sempre!")
            sys.exit()

        else:
            print("Opção inválida!") 

def pegar_usuario_logado_cpf():
    caminho = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f'db/usuario_logado.json')
    with open(caminho, 'r') as f:
        usuario = json.load(f)

    if (usuario == {}):
        return None
    return usuario["cpf"]

def adicionar_beatpoints(bp):
    usuarios_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db/usuarios.json')
    with open(usuarios_json, 'r') as f:
        usuarios = json.load(f)
    
    usuario_cpf = pegar_usuario_logado_cpf()
    for usuario in usuarios:
        if usuario['cpf'] == usuario_cpf:
            usuario['beatpoints'] = usuario['beatpoints'] + bp
            break
    
    with open(usuarios_json, 'w') as f:
        json.dump(usuarios, f, indent=2)
        print("🎉 Beatpoints adicionados com sucesso!")
