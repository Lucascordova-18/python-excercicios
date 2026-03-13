import json

class Produto():
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

files = ("text.json")

produtos = []
dicionario = []

def salvar_produtos():
    while True:
        entrada = input("Digite a sua entrada nessa ordem: (Name, price, amount)")
        name, price, amount = entrada.split()
        price = float(price)
        amount = int(amount)
        produtos.append(Produto(name, price, amount))
        sair = input("Deseja sair?")
        if sair.lower() == "sim":
                break

    for produto in produtos:
        dicionario.append(produto.__dict__)

    with open(files, "w") as file:
        json.dump(dicionario, file, ensure_ascii=False, indent=2)
    
if __name__ == "__main__":
    salvar_produtos()