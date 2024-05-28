import time
from cadastro import cadastro
from crude_pratos import mostrar_pratos

#função do crude entradas 
from crude_entradas import cadastrar_entradas
from crude_entradas import listar_entradas
from crude_entradas import editar_entradas
from crude_entradas import excluir_entradas

#função do crude pratos 
from crude_pratos import cadastrar_pratos
from crude_pratos import listar_pratos
from crude_pratos import editar_pratos
from crude_pratos import excluir_pratos

#função do crude bebidas
from crude_bebidas import cadastrar_bebidas
from crude_bebidas import listar_bebidas
from crude_bebidas import editar_bebidas
from crude_bebidas import excluir_bebidas

#função do crude sobremesas
from crude_sobremesas import cadastrar_sobremesas
from crude_sobremesas import listar_sobremesas
from crude_sobremesas import editar_sobremesas
from crude_sobremesas import excluir_sobremesas

print("------  BeatPoints  ------")
print("\n 1. Sem se identificar\n 2. Se identificar para ganhar pontos\n")

def main():
  #print('Oiii')
  #cadastro()
  
  #chamando a função para Entradas
  cadastrar_entradas()
  listar_entradas()
  editar_entradas()
  #excluir_entradas()
  
  #chamando a função para pratos
  #cadastrar_pratos() 
  #listar_pratos()
  #editar_pratos()
  #excluir_pratos()
  mostrar_pratos()
  
  #chamando a função para bebidas
  #cadastrar_bebidas()
  #listar_bebidas()
  #editar_bebidas()
  #excluir_bebidas()
  
  #chamando a função para sobremesas
  #cadastrar_sobremesas()
  #listar_sobremesas()
  #editar_sobremesas()
  #excluir_sobremesas()

  
 

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
