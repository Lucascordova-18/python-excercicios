class CarrinhoDeCompra:
    def __init__(self):
        self._produto = []

    def inserir_produto(self, *produtos):
        for produto in produtos:
            self._produto.append(produto)
    

    def valor_total(self):
        return sum([p.preco for p in self._produto])

    def listar(self):
        print("entrei no listar")
        for produto in self._produto:
            print(produto.nome, produto.preco)
    
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

c1 = CarrinhoDeCompra()
p1,p2 = Produto("Arroz", 12), Produto("Carne", 50)

c1.inserir_produto(p1)
c1.inserir_produto(p2)
c1.listar()
print(c1.valor_total())



