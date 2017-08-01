from ListNode import Node

class Linklist(object):
    
    def __init__(self):
        self.head = Node(None)
        
    def addnode(self,data,nextvalue):
        if nextvalue.value == None:
            newNode = None