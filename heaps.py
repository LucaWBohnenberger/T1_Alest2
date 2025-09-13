class MaxHeap:
    def __init__(self):
        self.list = [None]
        
    def swim(self, index):
        while True:
            id_child = index
            
            if id_child == 1:
                break
            
            id_father = id_child // 2
            father = self.list[id_father]
            
            child = self.list[id_child]
            
            # Mudar no min_heap
            if father < child:
                self.list[id_father], self.list[id_child] = child, father
                id_child = id_father
            else:
                break
        
    def insert(self, ordem):
        self.list.append(ordem)
        self.swim(len(self.list) - 1) 

        
    def sink(self, index):
        """Desce o elemento no heap até a posição correta"""
        n = len(self.list) - 1
        while index * 2 <= n:
            id_left = index * 2
            id_right = id_left + 1

            # escolhe o filho maior
            if id_right > n or self.list[id_left] > self.list[id_right]:
                id_val = id_left
            else:
                id_val = id_right

            if self.list[id_val] > self.list[index]:
                self.list[index], self.list[id_val] = self.list[id_val], self.list[index]
                index = id_val
            else:
                break

    def remove(self):
        """Remove e retorna o elemento máximo"""
        if len(self.list) == 1:
            return None  # heap vazio
        elif len(self.list) == 2:
            return self.list.pop()  # apenas um elemento

        max_order = self.list[1]
        last = self.list.pop()
        self.list[1] = last
        self.sink(1)
        return max_order
    
    
class MinHeap:
    def __init__(self):
        self.list = [None]
        
    def swim(self, index):
        while True:
            id_child = index
            
            if id_child == 1:
                break
            
            id_father = id_child // 2
            father = self.list[id_father]
            
            child = self.list[id_child]
            
            # Mudar no min_heap
            if father > child:
                self.list[id_father], self.list[id_child] = child, father
                id_child = id_father
            else:
                break
        
    def insert(self, ordem):
        self.list.append(ordem)
        self.swim(len(self.list) - 1) 

        
    def sink(self, index):
        """Desce o elemento até a posição correta"""
        n = len(self.list) - 1
        while index * 2 <= n:
            id_left = index * 2
            id_right = id_left + 1

            # escolhe o filho menor
            if id_right > n or self.list[id_left] < self.list[id_right]:
                id_val = id_left
            else:
                id_val = id_right

            # se filho menor < pai, troca
            if self.list[id_val] < self.list[index]:
                self.list[index], self.list[id_val] = self.list[id_val], self.list[index]
                index = id_val
            else:
                break

    def remove(self):
        """Remove e retorna o elemento mínimo"""
        if len(self.list) == 1:
            return None  # heap vazio
        elif len(self.list) == 2:
            return self.list.pop()  # apenas um elemento

        min_ordem = self.list[1]
        last = self.list.pop()
        self.list[1] = last
        self.sink(1)
        return min_ordem


                
            

    
        
    
    
    

                
    
        