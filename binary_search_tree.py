class Tree:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
    
  def insert(self, data):
    if self.data == data:
      return False # duplicate value
    elif self.data > data:
      # if data is less than the data in the current node, descend down the left subtree
      if self.left is not None:
        return self.left.insert(data)
      else:
        # if we reach the bottom level of the tree and we've found the right position to insert it,
        # it will create a new subtree with that piece of data and set it up as the left subtree of its parent node.
        # and return True
        self.left = Tree(data)
        return True
    else:
      if self.right is not None:
        return self.right.insert(data)
      else:
        self.right = Tree(data)
        return True
      
  def find(self, data):
    if self.data == data:
      return data
    elif self.data > data:
      if self.left is None:
        return False
      else:
        return self.left.find(data)
    elif self.data < data:
      if self.right is None:
        return False
      else:
        return self.right.find(data)
  
  def get_size(self):
    if self.left is not None and self.right is not None:
      return 1 + self.left.get_size() + self.right.get_size()
    elif self.left:
      return 1 + self.left.get_size()
    elif self.right:
      return 1 + self.right.get_size()
    else:
      return 1
    
  def preorder(self):
    if self is not None:
      print(self.data, end=' ')
      if self.left is not None:
        self.left.preorder()
      if self.right is not None:
        self.right.preorder()
        
  def inorder(self):
    if self is not None:
      if self.left is not None:
        self.left.inorder()
      print(self.data, end=' ')
      if self.right is not None:
        self.right.inorder()
        
# Test code for Tree Class
tree = Tree(7)
tree.insert(9)
for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]:
  tree.insert(i)
for i in range(16):
  print(tree.find(i), end=' ') # False 1 2 3 4 False 6 7 False 9 10 11 12 13 14 15
print('\n', tree.get_size()) #  13

tree.preorder()
print() # 7 2 1 3 6 4 9 15 10 12 11 13 14
tree.inorder()
print() # 1 2 3 4 6 7 9 10 11 12 13 14 15