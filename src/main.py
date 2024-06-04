from cadastro import cadastro
from cliente.carrinho import adicionar_carrinho, remover_carrinho, esvaziar_carrinho, listar_carrinho
from entrar import entrar
from gerente.main import gerente_main

usuario_logado_cpf = None

def identificacao():
    opcao = input("Digite '1' para entrar ou '2' para se cadastrar: ")
    if opcao == '1':
        global usuario_logado_cpf
        usuario_logado_cpf = entrar()
    elif opcao == '2':
        cpf = cadastro()
        if cpf:
            print("Você ganhou 10 pontos! 🎉")

def main():
    esvaziar_carrinho()
    name = input("Qual o tipo de usuário você é? (1 - Gerente / 2 - Cliente) ")
    if name == '1':
        gerente_main()
    else:
        print("------  BeatPoints  ------")
        print("\n 1. Sem se identificar\n 2. Se identificar para ganhar pontos\n")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            print("Você não irá ganhar pontos 😢")
        elif opcao == '2':
            identificacao()
        else:
            print("Opção inválida!")

main()
