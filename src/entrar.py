from typing import List, Dict, Any
import json
import os

def entrar():
  print("\n\n----- Entrar  -----")

  usuarios_json = os.path.join(os.path.dirname(__file__), 'db/usuarios.json')

  with open(usuarios_json, 'r') as f:
    usuarios: List[Dict[str, Any]] = json.load(f)

  cpf = input("\nDigite seu CPF: ")
  senha = input("\nCrie sua senha: ")

  for usuario in usuarios:
    if usuario['cpf'] == cpf and usuario['senha'] == senha:
      print("\nBem vindo!", usuario['nome'])
      return usuario['cpf']

  print("\nCredencias inválidas! Usuário não encontrado 😢")
  return ''
