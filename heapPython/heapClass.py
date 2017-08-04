class myHeap(object):
    
    def __init__(self):
        self.array = []
        self.currentsize = 0
        
    def insert(self,value):
        self.array.append(value)
        self.currentsize += 1
        self.swapInsertion(self.currentsize-1)
        
    def swapInsertion(self,i):    
        flag = True
        if self.array[i] <= self.array[i//2]:
            flag = False
        else: self.array[i],self.array[i//2] = self.array[i//2], self.array[i]
        if flag: self.swapInsertion(i//2)
        
    def priorityDone(self):
        self.array[self.currentsize-1], self.array[0] = self.array[0], self.array[self.currentsize-1]
        if self.currentsize>1 :
            self.array.pop()
            i = 0
            self.currentsize -= 1
            self.prioritySwap(i)
        else: print("All tasks are completed assole.!!")
        
    def maxNum(self,index):
        if self.array[index*2+1] > self.array[index*2+2]: 
            self.swap(index,index*2+1)
            return index*2+1
        else:
            self.swap(index,index*2+2)
            return index*2 + 2
        
    def swap(self,index1,index2):
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]
    
    def prioritySwap(self,index):
        size = self.currentsize
        while index*2+2 < size:
            index =  self.maxNum(index)
            
            
        
        