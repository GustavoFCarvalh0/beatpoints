import time
from cadastro import cadastro

# Funções para o CRUD de entradas
from entradas import cadastrar_entradas, listar_entradas, editar_entradas, excluir_entrada

# Funções para o CRUD de pratos
from pratos import cadastrar_pratos, listar_pratos, editar_pratos, excluir_pratos

# Funções para o CRUD de bebidas
from bebidas import cadastrar_bebidas, listar_bebidas, editar_bebidas, excluir_bebidas

# Funções para o CRUD de sobremesas
from sobremesas import cadastrar_sobremesas, listar_sobremesas, editar_sobremesas, excluir_sobremesas

print("------  BeatPoints  ------")
print("\n 1. Sem se identificar\n 2. Se identificar para ganhar pontos\n")

def main():
    if __name__ == "__main__":
        while True:
            print("\nOpções:")
            print("1. Cadastrar")
            print("2. Listar")
            print("3. Editar")
            print("4. Excluir")
            print("5. Sair")

            opcao = input("Digite o número da opção desejada: ")

            if opcao == '1':
                print("\nOpções de cadastro:")
                print("1. Cadastrar Entradas")
                print("2. Cadastrar Pratos")
                print("3. Cadastrar Bebidas")
                print("4. Cadastrar Sobremesas")

                sub_opcao = input("Digite o número da opção desejada: ")
                if sub_opcao == '1':
                    cadastrar_entradas()
                elif sub_opcao == '2':
                    cadastrar_pratos()
                elif sub_opcao == '3':
                    cadastrar_bebidas()
                elif sub_opcao == '4':
                    cadastrar_sobremesas()
                else:
                    print("Opção inválida!")

            elif opcao == '2':
                print("\nOpções de listagem:")
                print("1. Listar Entradas")
                print("2. Listar Pratos")
                print("3. Listar Bebidas")
                print("4. Listar Sobremesas")

                sub_opcao = input("Digite o número da opção desejada: ")
                if sub_opcao == '1':
                    listar_entradas()
                elif sub_opcao == '2':
                    listar_pratos()
                elif sub_opcao == '3':
                    listar_bebidas()
                elif sub_opcao == '4':
                    listar_sobremesas()
                else:
                    print("Opção inválida!")

            elif opcao == '3':
                print("\nOpções de edição:")
                print("1. Editar Entradas")
                print("2. Editar Pratos")
                print("3. Editar Bebidas")
                print("4. Editar Sobremesas")

                sub_opcao = input("Digite o número da opção desejada: ")
                if sub_opcao == '1':
                    editar_entradas()
                elif sub_opcao == '2':
                    editar_pratos()
                elif sub_opcao == '3':
                    editar_bebidas()
                elif sub_opcao == '4':
                    editar_sobremesas()
                else:
                    print("Opção inválida!")

            elif opcao == '4':
                print("\nOpções de exclusão:")
                print("1. Excluir Entradas")
                print("2. Excluir Pratos")
                print("3. Excluir Bebidas")
                print("4. Excluir Sobremesas")

                sub_opcao = input("Digite o número da opção desejada: ")
                if sub_opcao == '1':
                    excluir_entrada()
                elif sub_opcao == '2':
                    excluir_pratos()
                elif sub_opcao == '3':
                    excluir_bebidas()
                elif sub_opcao == '4':
                    excluir_sobremesas()
                else:
                    print("Opção inválida!")

            elif opcao == '5':
                print("Saindo do programa...")
                break

            else:
                print("Opção inválida!")

if __name__ == "__main__":
    main()
    
# opcao_cadastro = int(input("Selecione uma opção: "))
# while opcao_cadastro != 1 and opcao_cadastro != 2:
#   print("\nOpção invalida, tente novamente!\n")
#   opcao_cadastro = int(input("Selecione uma opção: "))

# if opcao_cadastro == 2:
#     print("\n1. Fazer login\n 2. Cadastra-se\n")
#     opcao_login = int(input("Selecione uma opção: "))
#     if opcao_login == 1:
#         dados_planilha = pd.read_excel(planilha)
#         bdd_cpf = dados_planilha['CPF'].values
#         cpf_login = str(input("Digite seu CPF: "))
#         senha_login = str(input("Senha: "))
#         if cpf_login in str(bdd_cpf):
#             linha_cpf = dados_planilha[dados_planilha["CPF"] == cpf_login].index[0]
#             senha_match = dados_planilha.loc[linha_cpf, ["Senha"]]
#             if senha_match == senha_login:
#                 print("Login efetuado com sucesso!")
#                 time.sleep(2)
#                 print("Entrando...")

#     if opcao_login == 2:
#         print("\n\n-----  Tela de Cadastro  -----")
#         nome = str(input("\nDigite seu nome completo: "))
#         cpf = str(input("\nDigite seu CPF: "))
#         senha = str(input("\nCrie sua senha: "))
#         dados_planilha = pd.read_excel(planilha)
#         id_cliente = len(dados_planilha['ID Cliente'])
#         novos_dados = {'ID Cliente':[id_cliente],
#                     'Nome Completo':[nome],
#                     'CPF':[cpf],
#                     'Senha':[senha]}
#         novo_df = pd.DataFrame(novos_dados)
#         dados_atualizados = pd.concat([dados_planilha, novo_df], ignore_index=True)
#         dados_atualizados.to_excel(planilha, index=False)

# print("\n-----  Home  -----")
# print("\n1. Promoção do dia\n 2. Cardápio\n 3. Carrinho")
# opcao_home = int(input("Selecione uma opção: "))
# while opcao_home != 1 and opcao_home != 2 and opcao_home != 3:
#     print("\nOpção invalida, tente novamente!\n")
#     opcao_home = int(input("Selecione uma opção: "))
