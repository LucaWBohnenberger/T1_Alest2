class MaxHeap:
    def __init__(self):
        self.list = [None]
        
    def is_empty(self):
        return len(self.list) == 1
    
    def peek(self):
        if self.is_empty():
            return None
        return self.list[1]
        
    def swim(self, index):
        while index > 1 and self.list[index] > self.list[index // 2]:
            self.list[index], self.list[index // 2] = self.list[index // 2], self.list[index]
            index = index // 2
    
    def insert(self, ordem):
        self.list.append(ordem)
        self.swim(len(self.list) - 1) 
    
    def sink(self, index):
        n = len(self.list) - 1
        while index * 2 <= n:
            child_idx = index * 2
            if child_idx < n and self.list[child_idx] < self.list[child_idx + 1]:
                child_idx += 1
            
            if self.list[index] >= self.list[child_idx]:
                break
                
            self.list[index], self.list[child_idx] = self.list[child_idx], self.list[index]
            index = child_idx

    def remove(self):
        if self.is_empty():
            return None
        
        max_order = self.list[1]
        self.list[1] = self.list[-1]
        self.list.pop()
        
        if not self.is_empty():
            self.sink(1)
            
        return max_order

class MinHeap(MaxHeap): 
    def swim(self, index):
        while index > 1 and self.list[index] < self.list[index // 2]:
            self.list[index], self.list[index // 2] = self.list[index // 2], self.list[index]
            index = index // 2
            
    def sink(self, index):
        n = len(self.list) - 1
        while index * 2 <= n:
            child_idx = index * 2
            if child_idx < n and self.list[child_idx] > self.list[child_idx + 1]:
                child_idx += 1
            
            if self.list[index] <= self.list[child_idx]:
                break
                
            self.list[index], self.list[child_idx] = self.list[child_idx], self.list[index]
            index = child_idx