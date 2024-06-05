from cadastro import cadastro
from cliente .carrinho import esvaziar_carrinho
from entrar import entrar
import getpass
from gerente.main import gerente_main
from cliente.main import cliente_main
import sys
import os
import json

def identificacao():
    opcao = input("Digite '1' para entrar ou '2' para se cadastrar: ")
    if opcao == '1':
        entrar()
    elif opcao == '2':
        cadastro()

def deslogar_usuario():
    usuario_json = os.path.join(os.path.dirname(__file__), 'db/usuario_logado.json')
    with open(usuario_json, 'w') as f:
        json.dump({}, f)

def main():
    esvaziar_carrinho()
    deslogar_usuario()
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
        print("\n 1. Se identificar para ganhar pontos\n 2. Sem se identificar\n")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            identificacao()
        elif opcao == '2':
            print("😢 Você não irá ganhar pontos...")
        else:
            print("Opção inválida!")
            return
        cliente_main()

while True:
    main()
    resposta = input("\n😊 Deseja continuar o programa (S/N): ")
    if resposta.lower() == 'n':
        print("🎉 Volte sempre!")
        sys.exit()

