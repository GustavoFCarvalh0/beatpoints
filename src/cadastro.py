import json
import os

def cadastro():
  print("\n\n----- Cadastro  -----")

  usuarios_json = os.path.join(os.path.dirname(__file__), 'db/usuarios.json')

  with open(usuarios_json, 'r') as f:
    usuarios = json.load(f)

  nome = input("\nDigite seu nome completo: ")
  cpf = input("\nDigite seu CPF: ")
  senha = input("\nCrie sua senha: ")

  usuarios.append({ 'nome': nome, 'cpf': cpf, 'senha': senha })
  with open(usuarios_json, 'w') as f:
    json.dump(usuarios, f, indent=2)
  
  print("\nUsuário criado com sucesso!")
  

