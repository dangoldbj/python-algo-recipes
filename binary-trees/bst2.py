class BSTNode:
    def __init__(self, parent, key):
        self.parent = parent
        self.key = key

    def find(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            return self.left and self.left.find(key)
        else:
            return self.right and self.right.find(key)

    def find_min(self):
        if self.left is None:
            return self
        
        return self.left.find_min()

    def next_larger(self):
        if self.right is not None:
            return self.right.find_min()
        
        current = self
        while current is not None and current is current.parent.right:
            current = current.parent

        return current.parent

            
    def insert(self, node):
        if node is None:
            return
        
        if node.key < self.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)
        return node

    def delete(self):
        if self.left is None or self.right is None:
            node = self.left or self.right
            if node is not None:
                node.parent = self.parent
            if self is self.parent.left:
                self.parent.left = node
            else:
                self.parent.right = node
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()


class MinBSTNode(BSTNode):
    def __init__(self, parent, key):
        super().__init__(parent, key)
        self.min = self
    
    def find_min(self):
        return self.min

    def insert(self, node):
        if node is None:
            return
        
        if node.key < self.key:
            if node.key < self.min.key:
                self.min = node
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
                    self.parent.min = self.parent.left.min
                else:
                    self.parent.min = self.parent
                c = self.parent
                while c is not None and c is c.parent.left:
                    c.parent.min = c.min
                    c = c.parent

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
        self.klass = klass

    def find(self, k):
        node = self.klass(None, k)
        return self.root and self.root.find(node)

    def insert(self, k):
        node = self.klass(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        return node

    def next_larger(self, k):
        node = self.find(k)
        return node and node.next_larger()

    def delete(self, k):
        node = self.find(k)

        if node is None:
            return

        if node is self.root:
            pseudoroot = self.klass(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
            # now pseudoroot gets garbage collected
            return deleted
        else:
            return node.delete()


class MinBST(BST):
    def __init__(self):
        super().__init__(MinBSTNode)