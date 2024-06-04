from cadastro import cadastro
from entrar import entrar
import getpass
from gerente.main import gerente_main
from cliente.main import cliente_main

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
    name = input("Qual o tipo de usuário você é? (1 - Gerente / 2 - Cliente) ")
    if name == '1':
        codGerent = "equipe10"
        codGerent = getpass.getpass("\nDigite o código de acesso: ")
        if codGerent == "equipe10":
            gerente_main()
        else:
            print("\nVocê não tem permissão!")
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
        cliente_main()

resp = 's'
while resp.lower() != 'n':
    resp = input("\nDigite 'n' para finalizar: ")
    main()
    
print("Volte sempre!")
    
