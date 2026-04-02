class Node:
  def __init__(self, d, n=None, p=None):
    self.data = d
    self.next_node = n
    self.prev_node = p
    
  def __str__(self):
    return ('(' + str(self.data) + ')')
  
# Regular (singly) LinkedList
class LinkedList:
  def __init__(self, r = None):
    self.root = r
    self.size = 0
    
  def add(self, d):
    # inserting this node at the very beginning of list, 
    # so current root node is going to be the seconde node. 
    new_node = Node(d, self.root)
    # change the root node to the new node.
    self.root = new_node
    self.size += 1
    
  def find(self, d):
    this_node = self.root
    # as long as it is valid node, iterate.
    while this_node is not None:
      if this_node.data == d:
        return d
      else:
        this_node = this_node.next_node
    return None
  
  def remove(self, d):
    this_node = self.root
    prev_node = None
    
    while this_node is not None:
      if this_node.data == d:
        if prev_node is not None: # data is in non-root.
          prev_node.next_node = this_node.next_node
        else: # data is in root node
          self.root = this_node.next_node
        self.size -= 1
        return True # data removed
      else:
        prev_node = this_node
        this_node = this_node.next_node
    return False # data not found
  
  def print_list(self):
    this_node = self.root
    while this_node is not None:
      print(this_node, end='->')
      this_node = this_node.next_node
    print('None')
    
# Test code for LinkedList Class
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list() # (12)->(8)->(5)->None

print("size="+str(myList.size)) # siz=3
myList.remove(8) 
print("size="+str(myList.size)) # siz=2
print(myList.find(5)) # 5
print(myList.root) # (12)

# Circular LinkedList
class CircularLinkedList:
  def __init__(self, r = None):
    self.root = r
    self.size = 0
    
  def add(self, d):
    if self.size == 0:
      # if the list is empty, add the first node then make its next node point to itself.
      self.root = Node(d)
      self.root.next_node = self.root
    else:
      # if already at least one node in the list, create a new node 
      # and insert it into the number two position right after the root
      # and change the root; next node to point to this new node. 
      new_node = Node(d, self.root.next_node)
      self.root.next_node = new_node
    self.size += 1
    
  def find(self, d):
    this_node = self.root
    while True:
      if this_node.data == d:
        return d
      # Unlike regular linkedlist, we have to check if we've circled all the wayback to the root node again
      elif this_node.next_node == self.root:
        return False
      this_node = this_node.next_node
    
  def remove(self, d):
    this_node = self.root
    prev_node = None
    
    while True:
      if this_node.data == d: # found
        if prev_node is not None:          
          prev_node.next_node = this_node.next_node
        else: # if we need to delete the root
          # use while loop to find the very last node in the list 
          # so that we can update its next node to point to the new root.
          while this_node.next_node != self.root:
            this_node = this_node.next_node
          this_node.next_node = self.root.next_node
          self.root = self.root.next_node
        self.size -= 1
        return True # data removed
      elif this_node.next_node == self.root:
        return False # data not found
      prev_node = this_node
      this_node = this_node.next_node
      
  def print_list(self):
    if self.root is None:
      return
    this_node = self.root
    print(this_node, end='->')
    while this_node.next_node != self.root:
      this_node = this_node.next_node
      print(this_node, end='->')
    print()

# Test code for CircularLinkedList Class
cll = CircularLinkedList()
for i in [5,7,3,8,9]:
  cll.add(i)

print('size='+str(cll.size)) # size=5
print(cll.find(8)) # 8
print(cll.find(12)) # False

my_node = cll.root
print(my_node, end='->')
for i in range(8):
  my_node = my_node.next_node
  print(my_node, end='->')
print() # (5)->(9)->(8)->(3)->(7)->(5)->(9)->(8)->(3)->

cll.print_list() # (5)->(9)->(8)->(3)->(7)->
cll.remove(8)
print(cll.remove(15)) # False
print('size='+str(cll.size)) # size=4
cll.remove(5) # delete root node 
cll.print_list() # (9)->(3)->(7)

# Doubly LinkedList
class DoublyLinkedList:
  def __init__(self, r = None):
    self.root = r
    self.last = r
    self.size = 0
    
  def add(self, d):
    if self.size == 0:
      self.root = Node(d)
      self.last = self.root
    else:
      new_node = Node(d, self.root)
      self.root.prev_node = new_node
      self.root = new_node
    self.size += 1
    
  def find(self, d):
    this_node = self.root
    while this_node is not None:
      if this_node.data == d:
        return d
      elif this_node.next_node == None:
        return False
      else:
        this_node = this_node.next_node
        
  def remove(self, d):
    this_node = self.root
    while this_node is not None:
      if this_node.data == d: 
        if this_node.prev_node is not None:  
          # the node is not in either root or in the last node, change the previous node next-pointer and the next node previous-pointer 
          if this_node.next_node is not None: # deletea middle node    
            this_node.prev_node.next_node = this_node.next_node
            this_node.next_node.prev_node = this_node.prev_node
          else: # delete last node
            # change the second last node next-pointer to None
            this_node.prev_node.next_node = None
            self.last = this_node.prev_node
        else: # delete root node
          # change the root pointer to point to the second node 
          self.root = this_node.next_node
          this_node.next_node.prev_node = self.root
        self.size -= 1
        return True # data removed
      else:
        this_node = this_node.next_node
    return False # data not found
    
  def print_list(self):
    if self.root is None:
      return
    this_node = self.root
    print(this_node, end='->')
    while this_node.next_node is not None:
      this_node = this_node.next_node
      print(this_node, end='->')
    print()

# Test code for DoublyLinkedList Class
dll = DoublyLinkedList()
for i in [5,9,3,8,9]:
  dll.add(i)
  
print('size='+str(dll.size)) # size=5
dll.print_list() # (9)->(8)->(3)->(9)->(5)->
dll.remove(8)
print('size='+str(dll.size)) # size=4

print(dll.remove(15)) # False
print(dll.find(15)) # False
dll.add(21)
dll.add(22)
dll.remove(5)
dll.print_list() # (22)->(21)->(9)->(3)->(9)->
print(dll.last.prev_node) # (3)
