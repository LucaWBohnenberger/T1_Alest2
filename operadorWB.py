from heaps import MaxHeap, MinHeap
from classe import Ordem

class OWB:
    def __init__(self):
        self.compras = MaxHeap()
        self.vendas = MinHeap()
        self.lucro_total = 0
        self.acoes_negociadas = 0

    def _processar_compra(self, quantidade, valor):
        while (quantidade > 0 and 
               not self.vendas.is_empty() and 
               self.vendas.peek().valor <= valor):
            
            melhor_venda = self.vendas.remove()
            
            qtd_negociada = min(quantidade, melhor_venda.quantidade)
            
            self.acoes_negociadas += qtd_negociada
            self.lucro_total += qtd_negociada * (valor - melhor_venda.valor)
            
            quantidade -= qtd_negociada
            melhor_venda.quantidade -= qtd_negociada
            
            if melhor_venda.quantidade > 0:
                self.vendas.insert(melhor_venda)

        if quantidade > 0:
            self.compras.insert(Ordem(quantidade, valor))

    def _processar_venda(self, quantidade, valor):
        while (quantidade > 0 and 
               not self.compras.is_empty() and 
               self.compras.peek().valor >= valor):
            
            melhor_compra = self.compras.remove()
            
            qtd_negociada = min(quantidade, melhor_compra.quantidade)
            
            self.acoes_negociadas += qtd_negociada
            self.lucro_total += qtd_negociada * (melhor_compra.valor - valor)
            
            quantidade -= qtd_negociada
            melhor_compra.quantidade -= qtd_negociada
            
            if melhor_compra.quantidade > 0:
                self.compras.insert(melhor_compra)
        
        if quantidade > 0:
            self.vendas.insert(Ordem(quantidade, valor))

    def ler_arquivo_e_processar(self, caminho):
        with open(caminho, "r") as f:
            # Pula a primeira linha que contém o número de transações
            next(f, None)
            
            for linha in f:
                partes = linha.strip().split()
                if len(partes) != 3:
                    continue
                
                tipo = partes[0]
                qnt = int(partes[1])
                val = int(partes[2])
                
                if tipo == "C":
                    self._processar_compra(qnt, val)
                elif tipo == "V":
                    self._processar_venda(qnt, val)
    
    def resultados(self):
        """
        Calcula as quantidades restantes e exibe o resumo final.
        """
        ordens_compra_pendentes = len(self.compras.list) - 1
        ordens_venda_pendentes = len(self.vendas.list) - 1

        print(f"Lucro da empresa na simulação: ${self.lucro_total}")
        print(f"Quantidade de ações negociadas: {self.acoes_negociadas}")
        print(f"Ordens de compras ainda pendentes: {ordens_compra_pendentes}")
        print(f"Ordens de vendas ainda pendentes: {ordens_venda_pendentes}")
