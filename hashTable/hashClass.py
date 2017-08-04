class HashTable(object):
    
    def __init__(self,size):
        self.size = size
        self.slots = self.size*[None]
        self.data = self.size*[None]
        self.values = 0
        
    def __setitem__(self,key,value):
        self.put(key, value)
        
    def __getitem__(self,key):
        self.get(key)
        
    def put(self,key,value):
        hashValue = self.hashFunction(key)
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = value
            self.values += 1
        elif self.slots[hashValue] == key:
            self.data[hashValue] = value
        else:
            hashValue = self.reHash(hashValue)
            while self.slots[hashValue] != None and self.slots[hashValue] != key:
                hashValue = self.reHash(hashValue)
            self.slots[hashValue] = key
            self.data[hashValue] = value
            self.values += 1
                
        
    def reHash(self,oldValue):
        return (oldValue+1)%self.size
       
    def __len__(self):
        return self.values
    
    
    def get(self,key):
        hashValue = self.hashFunction(key)
        if self.slots[hashValue] == None:
            return "No Value associated"
        elif self.slots[hashValue] == key:
            return self.data[hashValue]
        
        
    def hashFunction(self,key):
        return key%self.size
    