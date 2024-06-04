import os
import json

def carregar_carrinho():
    # Atribuindo a variável o caminho do arquivo .json dinamicamente
    caminho = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f'db/carrinho.json')

    # Verifica se o arquivo existe
    if not os.path.exists(caminho):
        print(f"Erro: O arquivo {caminho} não foi encontrado.")
        return []
    
    # Verifica se o arquivo está vazio
    if os.path.getsize(caminho) == 0:
        print(f"Erro: O arquivo {caminho} está vazio.")
        return []

    # Abre e lê o conteúdo do arquivo JSON
    with open(caminho, 'r') as f:
        return json.load(f)
    
# Adicionar item ao carrinho
def adicionar_carrinho(produto, qtd = 1):
    caminho = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f'db/carrinho.json')
    carrinho = carregar_carrinho()
    # Verificando se o produto já existe no carrinho
    verificar_produto = [item for item in carrinho if item["id"] == produto["id"]]
    # Se o produto não existir 
    if len(verificar_produto) == 0:
        produto["qtd"] = qtd
        carrinho.append(produto)
        with open(caminho, 'w') as f:
            json.dump(carrinho, f, indent=2)
    # Se o produto já existir
    else:
        produto_selecionado = [item for item in carrinho if item["id"] == produto["id"]]
        produto_selecionado[0]["qtd"] = produto_selecionado[0]["qtd"] + qtd
        carrinho_sem_produto = [item for item in carrinho if item["id"] != produto["id"]]
        carrinho_sem_produto.append(produto_selecionado[0])
        with open(caminho, 'w') as f:
            json.dump(carrinho_sem_produto, f, indent=2)

# Remover item do carrinho
def remover_carrinho(id_produto, qtd = 1):
    caminho = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f'db/carrinho.json')
    carrinho = carregar_carrinho()
    # Verificando se o produto já existe no carrinho
    produto = [item for item in carrinho if item["id"] == id_produto]
    # Se o produto não existir 
    if len(produto) == 0:
        print("\nO produto não está no carrinho!\n")
    # Se o produto já existir
    else:
        produto = produto[0]
        if(produto["qtd"] < qtd):
            print("Você está tentando retirar uma quantidade maior do que tem no carrinho.")
        else:
            produto["qtd"] = produto["qtd"] - qtd
            if produto["qtd"] == 0:
                carrinho_sem_produto = [item for item in carrinho if item["id"] != id_produto]
            else:
                carrinho_sem_produto = [item for item in carrinho if item["id"] != id_produto]
                carrinho_sem_produto.append(produto)
            with open(caminho, 'w') as f:
                json.dump(carrinho_sem_produto, f, indent=2)

# Esvaziar carrinho
def esvaziar_carrinho():
    caminho = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f'db/carrinho.json')
    carrinho_vazio = []
    with open(caminho, 'w') as f:
        json.dump(carrinho_vazio, f, indent=2)

# Listar carrinho
def listar_carrinho():
    carrinho = carregar_carrinho()
    soma_valor = 0
    soma_beatpoints = 0
    soma_qtd = 0
    print("********CARRINHO********")
    for item in carrinho:
        print(f"Nome: {item["nome"]}")
        print(f"Valor: R$ {(item["valor"])}")
        print(f"Beatpoints: {item["beatpoints"]}")
        print(f"Quantidade: {item["qtd"]}")
        print("----------------------")
        soma_valor += item["valor"]
        soma_beatpoints += item["beatpoints"]
        soma_qtd += item["qtd"]
    print(f"Valor total: {soma_valor}")
    print(f"Beatpoints total: {soma_beatpoints}")
    print(f"Quantidade total: {soma_qtd}")
