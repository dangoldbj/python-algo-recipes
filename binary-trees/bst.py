class BSTNode:
    def __init__(self, key, parent = None, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
    
    def find(self, key):
        if self.key == key:
            return self
        elif self.left is not None and key < self.key:
            return self.left.find(key)
        elif self.right is not None and key > self.key:
            return self.right.find(key)
        
        return None

    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            if self.left is not None:
                self.left.insert(node)
            else:
                self.left = node
                node.parent = self
        
        elif node.key > self.key:
            if self.right is not None:
                self.right.insert(node)
            else:
                self.right = node
                node.parent = self

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def next_larger(self):
        if self.right is not None:
            return self.right.find_min()
        
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        
        return current.parent

    def delete(self):
        # Handle root node that is self.parent = None in tree
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

class BST:
    def __init__(self, klass = BSTNode):
        self.root = None
    
    def find(self, key):
        return self.root and self.root.find(key)
    
    def find_min(self):
        return self.root and self.root.find_min()
    
    def insert(self, key):
        node = self.klass(key, parent = None)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        return node

    def delete(self, k):
        node = self.find(k)
        if node is None:
            return None
        
        if node is self.root:
            pseudoroot = self.klass(0, parent = None)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()

    def next_larger(self, k):
        node = self.find(k)
        return node and node.next_larger()

    

