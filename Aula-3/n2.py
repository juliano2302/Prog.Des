class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        novo_preco = self.preco - (self.preco * percentual / 100)
        return novo_preco

produto1 = Produto("Notebook", 3500.00)
produto2 = Produto("Mouse", 100.00)

print("Produto:", produto1.nome)
print("Preço com 15% de desconto: R$", produto1.desconto(15))

print("Produto:", produto2.nome)
print("Preço com 10% de desconto: R$", produto2.desconto(10))