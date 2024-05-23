import time
from cadastro import cadastro

print("------  BeatPoints  ------")
print("\n 1. Sem se identificar\n 2. Se identificar para ganhar pontos\n")

def main():
  cadastro()

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
