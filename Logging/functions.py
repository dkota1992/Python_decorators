class Calculator():
    
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
    
    def add(self):
        return self.x + self.y
    
    def multiply(self):
        return self.x*self.y
    
    def subtract(self):
        return Calculator.mod(self.x-self.y)
    
    def divide(self):
        return self.x//self.y
    
    def modulo(self):
        return self.x%self.y
    
    def __del__(self):
        print("Destructor enabled")
         
    @staticmethod
    def mod(num):
        if num>0: return num
        return -1*num