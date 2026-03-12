import json
from salvar_produtos import files, Produto

produtos_recebido = []

with open(files, "r") as file:
    for produto in json.load(file):
        novo_produto = Produto(**produto)
        produtos_recebido.append(novo_produto)

for produto in produtos_recebido:
    print(f"Produto: {produto.name}, Preço: {produto.price}, Quantidade: {produto.amount}")