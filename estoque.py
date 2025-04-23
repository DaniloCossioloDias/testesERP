class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome] += quantidade
        else:
            self.produtos[nome] = quantidade
        return self.produtos[nome]

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos and self.produtos[nome] >= quantidade:
            self.produtos[nome] -= quantidade
            return self.produtos[nome]
        else:
            raise ValueError("Produto não encontrado ou quantidade insuficiente.")
