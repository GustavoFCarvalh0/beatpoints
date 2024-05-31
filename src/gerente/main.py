from gerente.bebidas import cadastrar_bebidas, editar_bebidas, excluir_bebidas, listar_bebidas
from gerente.entradas import cadastrar_entradas, editar_entradas, excluir_entradas, listar_entradas
from gerente.pratos import cadastrar_pratos, editar_pratos, excluir_pratos, listar_pratos
from gerente.sobremesas import cadastrar_sobremesas, editar_sobremesas, excluir_sobremesas, listar_sobremesas

def gerente_main():
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
          excluir_entradas()
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