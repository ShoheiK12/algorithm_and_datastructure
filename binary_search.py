def binary_search(list, target):
  # beginning of the array -> index of list starts at 0.
  first = 0
  # end of the array -> ex) [1,2,3,4,5] Index of the last element of this list os 4. 
  last = len(list) - 1
  # keep executing loop until the value of first is less than or equal to the value of last.
  while first <= last:
    # calculate midpoint -> first step of binary search
    midpoint = (first + last) // 2
    
    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      # don't care about any values lower than the midpoint and redefine first to point to the value after the midpoint.
      first = midpoint + 1
    else:
      # discard the value after the midpoint and redefine last to point to the value prior to the midpoint.
      last = midpoint - 1
  
  return None

def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in list")
    
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)