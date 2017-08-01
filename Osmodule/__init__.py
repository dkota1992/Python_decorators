import os
from datetime import datetime

def decorator_function(passed_function):
    def wrapper_function(*args, **kwargs):
        print("This is wrapper_function before {}".format(passed_function.__name__))
        return passed_function(*args, **kwargs)
    return wrapper_function

class Decorator_class(object):
 
    def __init__(self,passed_function):
        self.passed_function = passed_function 
        
    def __call__(self,*args,**kwargs):
        import logging
        logging.basicConfig(filename='{}.log'.format(self.passed_function.__name__),level=logging.INFO)
        logging.info('Ran with {} args and {} kwargs'.format(args,kwargs))
        return self.passed_function(*args,**kwargs)

class My_timer(object):
    
    def __init__(self,passed_function):
        self.passed_function = passed_function
    
    def __call__(self,*args,**kwargs):
        import time
        t1 = time.time()
        time.sleep(0.8)
        result = self.passed_function(*args,**kwargs)
        print("Time taken for {}".format(time.time()-t1))
        return result

@My_timer
@Decorator_class
def original_function(msg):
    print("This is the original message : {}".format(os.getcwd()))
    
print(os.environ.get(os.getcwd()))
print(os.path.basename("ddr/adkfj/kljda/kjj"))

