# pass an argument in terminal -> python -i linked_list.py -> This is going to run the python repo, the read evaluate print loop in the console.
class Node:
  """
  An object for storing a sigle node of a linked list.
  Models two attributes - data and the link to the next node in the list
  """
  data = None
  next_node = None
  
  def __init__(self, data):
    self.data = data
    
  def __repr__(self):
    # String representation of what we want printed to the console when we inspect that object inside of a console.
    return "<Node data: %s>" % self.data
  
class LinkedList:
  """
  Singly linked list
  """
  
  def __init__(self):
    # This head attribute models the only node that the list will have a reference to. since every node points to the next node to find a particular node, we can go from one node to the next in, a process is called "Traversal".
    self.head = None
    
  def is_empty(self):
    # If this condition evaluates true, it indicates the list is empty.
    return self.head == None
  
  # how many items we have -> visit each node and call next until we hit the tail node.
  def size(self):
    """
    Returns the number of nodesin the list.
    Takes O(n) time.
    """
    # start by getting a reference to the head
    current = self.head
    # count: initial value of 0 taht will increment every time we visit a node
    count = 0
    
    while current:
      count += 1
      # assign the next node in the list to current.
      current = current.next_node
      
    return count