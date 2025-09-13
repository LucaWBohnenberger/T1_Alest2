class Ordem:
    def __init__(self, quantidade, valor):
        self.quantidade = quantidade
        self.valor = valor
        
    def __lt__(self, other):
        return self.valor < other.valor