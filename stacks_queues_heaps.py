# Stack
# append()
my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print(my_stack) # [4,7,12,19]

# pop()
print(my_stack.pop()) # 19
print(my_stack.pop()) # 12
print(my_stack) # [4,7]

# Stack using List with a Wrapper Class
class Stack():
  def __init__(self):
    self.stack = list()
  def push(self, item):
    # appending item to the list
    self.stack.append(item)
  def pop(self):
    # if the list actually has items on the list, execute. 
    if len(self.stack) > 0:
      return self.stack.pop()
    else:
      # if the list is empty, return None.
      return None
  def peek(self):
    # peek function allows us to just look at the top item on the list and return the item.
    # but without removing it.
    # if the list actually has items on the list, execute. 
    if len(self.stack) > 0:
      return self.stack[len(self.stack)-1]
    else:
      # if the list is empty, return None.
      return None
  def __str__(self):
    # print out the stack by string representation.
    return str(self.stack)

# Test code for Stack Class
my_stack2 = Stack()
my_stack2.push(1)
my_stack2.push(3)
print(my_stack2) # [1,3]
print(my_stack2.pop()) # 3
print(my_stack2.peek()) # 1
print(my_stack2.pop()) # 1
print(my_stack2.pop()) # None

# Queue
# Dequeue
from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue) # deque([5, 10])
print(my_queue.popleft()) # 5

# Mav Heap
# Public function: push, peel, pop
# Private function: swap, __floatUp, __bubbleDown, __str
class MaxHeap():
  def __init__(self, items=[]):
    super().__init__()
    # put 0 in the firast element because we don'y use that -> we start our elements at index 1.
    self.heap = [0]
    for item in items:
      self.heap.append(item)
      self.__floatUp(len(self.heap) - 1)

  def push(self, data):
    self.heap.append(data)
    self.__floatUp(len(self.heap) - 1)
    
  def peek(self):
    # return the top item on the heap.
    if self.heap[1]:
      return self.heap[1]
    else:
      return False
    
  def pop(self):
    # if items in the list are more than two, swap the max itemw which is at index 1 with the last item.
    if len(self.heap) > 2:
      self.__swap(1, len(self.heap) - 1)
      # pop off the last item and assign it to variable max.
      max = self.heap.pop()
      # bubble down the first item that we moved into the top position.
      self.__bubbleDown(1)
    # The list has only 2 items, which those one is 0 (we're not using as part of our max heap).
    # so, only two items mean there's really just one item in our max heap. 
    elif len(self.heap) == 2:
      max = self.heap.pop()
    else:
      max = False
    return max
  
  def __swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
  def __floatUp(self, index):
    parent = index // 2
    # if index <= 1, it is already at the top position, then there is not floating up.
    if index <= 1:
      return
    # otherwise, compare it to its parent and if it's greater than its parent, those two need to swap places. 
    elif self.heap[index] > self.heap[parent]:
      self.__swap(index, parent)
      self.__floatUp(parent)
      
  def __bubbleDown(self, index):
    left = index * 2
    right = index * 2 + 1
    largest = index
    if len(self.heap) > left and self.heap[largest] < self.heap[left]:
      largest = left
    if len(self.heap) > right and self.heap[largest] < self.heap[right]:
      largest = right
    if largest != index:
      self.__swap(index, largest)
      self.__bubbleDown(largest)
      
  def __str__(self):
    return str(self.heap)
  
# Test code for MaxHeap Class
m = MaxHeap([95, 3, 21])
m.push(10)
print(m) # [0, 95, 10, 21, 3]
print(m.pop()) # 95
print(m.peek()) # 21