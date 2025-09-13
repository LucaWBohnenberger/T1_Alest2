class MaxHeap:
    def __init__(self):
        self.list = [None]
        
    def swim(self, child):
        while True:
            id_child = self.list.index(child)
            
            if id_child == 1:
                break
            
            id_father = id_child // 2
            father = self.list[id_father]
            
            # Mudar no min_heap
            if father < child:
                self.list[id_father], self.list[id_child] = child, father
                child = father
            else:
                break
        
    def insert(self, ordem):
        self.list[len(ordem)] = ordem
        self.swim(ordem)
        
    def remove(self):
        if len(self.list) == 1:
            return None
        
        ordem = self.list[1]
        last = self.list.pop
        
    
        
    
    
    

                
    
        