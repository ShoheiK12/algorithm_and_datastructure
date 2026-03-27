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
  
  def add(self, data):
    """
    Adds new Node containing data at head of the list.
    Takes O(1) time
    """
    # hold on data
    new_node = Node(data)
    # Before we set the new node as the head of list, we need to pint the new node's next property at whatever node is currently at head = we don't lose a reference to the old head
    new_node.next_node = self.head
    # set the new node as the head of the node
    self.head = new_node
    
  def search(self, key):
    """
    Searches for the first containing data that matches the key.
    Returns the node of "None" if not found.
    
    Takes O(n) tiem.
    """
    current = self.head
    
    while current:
      # check if the data on that node matches the key that we're searching for
      if current.data == key:
        return current
      # If it doesn't match, we'll assign the next node in the list to current and check again
      else:
        current = current.next_node
      # once we hit the tail node and haven't found the key, current gets set to None and the while loop exists. 
    return None
  
  def insert(self, data, index):
    """
    Inserts a new Node containing data at index position.
    Insertion takes O(1) time but finding the node at the
    insertion point takes O(n) time.
    
    Takes overall O(n) time.
    """
    # index = 0 means we want to insert the new node at the head of the list = same as def add. So, don't need to repeat.
    if index == 0:
      self.add(data)
    # index > 0: we need to travase the listto find the current node at that index
    if index > 0:
      # first create a new node containing the data we want to insert
      new = Node(data)
      
      position = index
      current = self.head
      # every time we call current.next_node, meaning we're moving to the next node in the list we'll decrease the value of position by 1. when position is 0, we'll have arrived at the node that's currently at the position we want to insert in.
      while position > 1:
        # while position > 1, keep calling next node and reassigning the current node
        current = current.next_node
        # at the same time, we decrement position
        position -= 1
      
      prev_node = current
      next_node = current.next_node
      
      # insert new node between prev and next
      prev_node.next_node = new
      new.next_node = next_node
      
  def remove(self,key):
    """
    Removes Node containing data that matches the key.
    Returns the node of None if key doesn't exist
    Takes O(n) time.
    """
    current = self.head
    # Set to None to keep track of the previous node as we travase the list
    previous = None
    # found: serve as a stopping condition for the loop
    found = False
    
    while current and not found:
      # head doesn't have a previous node and it's the only node being by the list -> found = True = srop while loop
      if current.data == key and current is self.head:
        found = True
        # point head to the second node in the list which we can get by referencing the next node attribute on current.
        # = nothing point to that firs node so it's automatically removed.
        self.head = current.next_node
      elif current.data == key:
        # To remove the current node, we need to go to the previous node and modify its next node reference to point to the node after current
        found = True
        previous.next_node = current.next_node
      else:
        # else case means the current node we're evaluating doesn't contain the data that matches the key.
        # -> we make previous point to the current node and then set current to the next node.
        previous = current
        current = current.next_node
    
    return current
  
  def __repr__(self):
    """
    Returns a string representation of the list
    Takes O(n) time
    """
    
    nodes = []
    current = self.head
    
    while current:
      if current:
        if current is self.head:
          nodes.append("[Head: %s]" % current.data)
        elif current.next_node is None:
          nodes.append("[Tail: %s]" % current.data)
        else:
          nodes.append("[%s]" % current.data)
        
        current = current.next_node
    
    return '-> '.join(nodes)