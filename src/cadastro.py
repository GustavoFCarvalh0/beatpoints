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

  usuarios.append({ 'nome': nome, 'cpf': cpf, 'senha': senha, 'beatpoints': 0 })
  with open(usuarios_json, 'w') as f:
    json.dump(usuarios, f, indent=2)
  
  logarUsuario(cpf)
  print("\n🎉 Usuário criado com sucesso!")


def logarUsuario(cpf: str):
  usuario_json = os.path.join(os.path.dirname(__file__), 'db/usuario_logado.json')

  with open(usuario_json, 'w') as f:
    json.dump({'cpf': cpf}, f)

  return {}