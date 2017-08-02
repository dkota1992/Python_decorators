class TreeNode(object):
    
    def __init__(self,data=None):
        self.left = None
        self.data = data
        self.right = None
        self.parent = None

    def rightChild(self):
        return self.right
    
    def leftChild(self):
        return self.left
    
    def parentData(self):
        return self.parent
       
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                    self.left.parent = self
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = TreeNode(data)
                    self.right.parent = self
                else: self.right.insert(data)
        if self.data is None:
            self.data = data
    def view(self):
        if self.left is None:
            left = None
        else: left = self.left.data
        if self.right is None:
            right = None
        else: right = self.right.data
        if self.parent is None:
            parent = None
        else: parent = self.parent.data
        print ("Left Node: {}, Node: {}, Right Node: {}, Parent: {}".format(left,self.data,right,parent))
        
    def getMin(self):
        if self.left is None:
            return self.data
        else: return self.left.getMin()
        
    def getMax(self):
        if self.right is None:
            return self.data
        else: return self.right.getMax()
        
    def traverse(self):
        if self.left is not None:
            self.left.traverse()
        print(self.data)
        if self.right is not None:
            self.right.traverse()
    
    def getMinChild(self):
        if self.left is None:
            return self
        else: return self.left.getMinChild()
        
    def look(self,data):
        if data<self.data:
            if self.left is None:
                return TreeNode(None)
            return self.left.look(data)
        elif data>self.data:
            if self.right is None:
                return TreeNode(None)
            return self.right.look(data)
        elif self.data == data: return self
        return TreeNode()
        
            