class Employee:
    
    raise_amout = 1.04
    
    def __init__(self,first=None,last=None,pay=None):
        self.first = first
        self.last = last 
        self.pay = pay
        self.fullname = self.first + ' ' + self.last
        
    def newpay(self):
        return self.pay*self.raise_amout
    
    
    @classmethod
    def set_raise_amount(cls, amt):
        cls.raise_amout = amt
        
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split(",")
        return cls(first,last,pay)
    
class Developer(Employee):
    
    def __init__(self,first=None,last=None,pay=None,prog_lang=None):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        

class Manager(Employee):
    
    def __init__(self,first=None,last=None,pay=None,servants=None):
        super().__init__(first,last,pay)
        if servants != None:
            self.servants = servants
        else: self.servants = []
        
    def addServant(self,Employee):
        self.servants.append(Employee)
    
    def removeServant(self, emp):
        if emp in self.servants:
            self.servants.remove(emp)
    
    def printServants(self):
        for emp in self.servants:
            print("-->",emp.fullname)
            
    def __len__(self):
        return len(self.servants)
    
    
class Testinner:
    
    def __init__(self):
        self.my_var = 44
    def myprint(self):
        print(self.my_var)
        

