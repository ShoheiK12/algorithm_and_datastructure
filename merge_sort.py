def merge_sort(list):
  """
  Sorts a list in ascending order.
  Returns a new sorted list.
  
  Divide: Find the midpoint of the list and divide into sublists.
  Conquer: Recursively sort the sublists created in previous step.
  Combine: Merge the sorted sublists created in previous step.
  """
  
  # stopping condition
  # The below is the recursive portion of our function. Divide and call merge sort on this divided sublist. Divide the list into two and call merge sort on it again until we reach our stopping condition.
  if len(list) <= 1:
    return list
  
  # divide the list into sublists
  # split: split the list we pass and returns two lists, split at the midpoint.
  left_half, right_half = split(list)
  # conquer: we sort each sublist and return a new sorted sublist.
  left = merge_sort(left_half)
  right = merge_sort(right_half)
  
  return merge(left, right)

def split(list):
  """
  Dovide the unsorted list at midpoint into sublists.
  Returns two sublists - left and right
  """
  
  mid = len(list) // 2
  # left: 0 to before midpoint (midpoint not included), right midpoint to the end (midpoint included).
  left = list[:mid]
  right = list[mid:]
  
  return left, right

def merge(left, right):
  """
  Merges two lists (arrays), sorting them in the process.
  Returns a new merged list.
  """
  
  l = []
  # create two local variables to keep track of index values that we're using for each list
  # i: index for left list, j: index for right list
  i = 0
  j = 0
  
  # keep sorting the values intil we've worked through both lists.
  while i < len(left) and j < len(right):
    # left[i] < right[j] means the value being compared in left is less than the value in the right and can be placed at position 0 in the new array l.
    if left[i] < right[j]:
       l.append(left[i])
       i += 1
    # else: we place the value at index j from the right list at the start of the new one (l).
    else:
      l.append(right[j])
      j += 1
      
  # right list is shorter than the left: previous loop terminates because we reach the end of the right list.
  while i < len(left):
    l.append(left[i])
    i += 1
    
  # left is shorter than the right.
  while j < len(right):
    l.append(right[j])
    j += 1
    
  return l

def verify_sorted(list):
  n = len(list)
  
  if n == 0 or n == 1:
    return True
  
  return list[0] < list[1] and verify_sorted(list[1:])
    
# Test
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
      
    
  
  
  