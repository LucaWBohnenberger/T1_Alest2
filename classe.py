class Ordem:
    def __init__(self, quantidade, valor):
        self.quantidade = quantidade
        self.valor = valor

    def __lt__(self, other):
        return self.valor < other.valor
    
    def __gt__(self, other):
        return self.valor > other.valor

    def __le__(self, other):
        return self.valor <= other.valor

    def __ge__(self, other):
        return self.valor >= other.valor

    def __eq__(self, other):
        return self.valor == other.valor
    
    def __str__(self):
        return f"Quantidade: {self.quantidade}, Valor: {self.valor}"