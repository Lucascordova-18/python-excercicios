from salvar_produtos import Produto

produto1 = Produto("Arroz", 12, 4)
produto2 = Produto("Carne", 86, 14)
produto3 = Produto("Macarrão", 8, 10)

produtos = [produto1, produto2, produto3]

dicionario = []

for products in produtos:
    dicionario.append(products.__dict__)

print(dicionario)